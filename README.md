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
<img width="1465" height="311" alt="image" src="https://github.com/user-attachments/assets/a1327d78-d77e-4812-aa4f-287656825ca2" />
[caegorized_emails.csv](https://github.com/user-attachments/files/27789776/caegorized_emails.csv)


**Requirements**
- groq == 0.2.0
- python-dotenv == 1.2.2
- pandas == 3.0.3

**Installing requirements with pip:**
pip install -r requirements.txt

**Installation and Running**


