#Custom libraries===============================
from etl.email_extraction import EMAIL_EXTRACTOR
from etl.email_transformer import EMAIL_TRANSFORMER
from etl.email_loader import EMAIL_LOADER
#===============================================
import os
from groq import Groq
from dotenv import load_dotenv
import json
#=================================
#File path for sample email data
EMAILS_JSON_FILE = "./sample_emails.json"
#=================================
# Api Variables
load_dotenv()
api_key = os.getenv("api_key")
client = Groq(api_key=api_key)
#=================================

# Modular ETL pipeline
ee = EMAIL_EXTRACTOR(EMAILS_JSON_FILE)
et = EMAIL_TRANSFORMER(ee.read_file())
el = EMAIL_LOADER()
#=================================


#Takes sample emails and processes them through llama-3.1-8b-instant model | returns a json string
def email_classifier():
    try:
        prompt = f"""You are an email classification system. Your task is to analyze each email and add category and priority fields.

            ## CRITICAL RULES:

            1. **PRESERVE ALL ORIGINAL FIELDS** - You must keep every original field exactly as given:
            - subject (copy exactly, do not modify)
            - body (copy exactly, do not summarize or modify)
            - from (copy exactly)
            - has_attachment (keep as true/false)

            2. **ADD ONLY THESE TWO FIELDS** - Do not add any other fields:
            - category (choose ONE from the list below)
            - priority (choose ONE from high/medium/low)

            3. **DO NOT add** any of these: priority_level, urgency, score, confidence, id, index, or any other field not listed above.

            4. **DO NOT modify** original field names. Keep them as: subject, body, from, has_attachment

            ## CATEGORIES (choose exactly one):
            - sales_lead: Interested in buying, partnership, demo request, upgrade inquiry
            - support_ticket: Technical issues, login problems, API errors, feature requests
            - complaint: Product damage, refund request, billing dispute, missing items
            - inquiry: General questions about pricing, features, documentation
            - internal: Employee onboarding, internal team communication
            - spam: Unwanted marketing, irrelevant content

            ## PRIORITY GUIDELINES:
            - high: Refund requests, account access issues, system outages, security concerns, cancellation requests, billing disputes
            - medium: Feature requests, contract renewals, follow-ups on proposals
            - low: General inquiries, demo requests, pricing questions, partnership opportunities

            ## INPUT EMAILS:
            {et.read_json_file()}

            ## EXPECTED OUTPUT FORMAT (JSON array ONLY):

            [
            {{
                "subject": "original subject here",
                "body": "original body here",
                "from": "original sender here",
                "has_attachment": true,
                "category": "support_ticket",
                "priority": "high"
            }},
            {{
                "subject": "original subject here",
                "body": "original body here",
                "from": "original sender here",
                "has_attachment": false,
                "category": "inquiry",
                "priority": "low"
            }}
            ]

            ## FINAL INSTRUCTIONS:
            - Return ONLY valid JSON. No explanations, no markdown, no extra text.
            - The output must be a JSON array.
            - Every email in the input must appear in the output.
            - Do not add, remove, or rename any fields from the original email.
            - Only add "category" and "priority".

            Now process the emails above and return the JSON array."""

        response = client.chat.completions.create(
            model= "llama-3.1-8b-instant",
            messages=[
                    {
                        "role": "system", 
                        "content": "You are a deterministic JSON outputter. You always return valid JSON. You never add extra text, markdown, or explanations."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
            response_format={"type": "json_object"},
            temperature=0,
            seed=42,
            top_p=1,
            stop=["\n```", "```\n"]

        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling Groq API: {e}")
        return json.dumps({"error": str(e), "results": []})

def main():
    print("Title: AI Email Categorizer")
    print("\nStart\n")
    #Reads response from ai and turns it into a dataframe
    ai_response = email_classifier()
    response = et.convert_response_to_dataframe(ai_response)

    #Saves results in a csv file | ./categorized_emails/cat_emails.csv
    el.convert_to_csv(response)
    print("\nFinished\n")

if __name__ == "__main__":
    main()


















