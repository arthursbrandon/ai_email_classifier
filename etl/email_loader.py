class EMAIL_LOADER:

    def __init__(self):
        pass

    def convert_to_csv(self, ai_response):
        ai_response.to_csv("./categorized_emails/caegorized_emails.csv")
