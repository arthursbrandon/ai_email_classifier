**AI Email Classifier**

**About**
AI-powered email classification system that categorizes and prioritizes incoming emails.

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
- Groq API (Llama 3.1)
- Pandas for data processing
- ETL pipeline architecture

**Screenshot of sample output**
<img width="766" height="100" alt="image" src="https://github.com/user-attachments/assets/44301a32-4df1-4ee1-98e8-51fcfa3c036e" />

**Requirements**
- groq==0.2.0
- python-dotenv==1.2.2
- pandas==3.0.3

**Installing requirements with pip:**
pip install -r requirements.txt



