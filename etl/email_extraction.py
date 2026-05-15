import json

class EMAIL_EXTRACTOR:

    def __init__(self,email_file):
        self.email_file = email_file
        

    def read_file(self):
        with open(self.email_file,'r') as file:
            response = json.load(file)
        
        return response
    
