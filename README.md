**AI Email Classifier**

**About**
- AI-powered email classification system that categorizes and prioritizes incoming emails.

**Features**
- Classifies emails into one of the 6 categories 
  - sales_lead
  - support_ticket
  - complaint
  - inquiry
  - internal
  - spam
- Assigns priority (low/medium/high) based on urgency
- Preserves all original email content
- Exports to CSV for CRM integration
- Built with Groq Llama 3.1

**Tech Stack**
- Python 3.12
- Groq API (Llama 3.1) | Requires Groq API key
- Pandas for data processing
- ETL pipeline architecture

**Screenshot of sample output**
<img width="1479" height="340" alt="Screenshot 2026-05-15 at 2 54 37 AM" src="https://github.com/user-attachments/assets/d961e735-e2b1-459f-87f6-c340ed0af81d" />
[categorized_emails.csv](https://github.com/user-attachments/files/27790043/categorized_emails.csv)

**Requirements**
- groq == 0.2.0
- python-dotenv == 1.2.2
- pandas == 3.0.3

**Installing requirements with pip:**
```
pip install -r requirements.txt
```

**Installation and Running**
```
git clone https://github.com/arthursbrandon/ai_email_classifier.git
cd ai_email_classifier
pip install -r requirements.txt
python main.py
```


