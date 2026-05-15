import pandas as pd
import json

class EMAIL_TRANSFORMER:

    def __init__(self, raw_email_data):
        self.raw_email_data = raw_email_data

    
    def convert_to_df(self):
        d = {
            "subject" : [],
            "body" : [],
            "from" : [],
            "has_attachment" : []
            }
        array_len = len(self.raw_email_data)

        for i in range(array_len):
            d['subject'].append(self.raw_email_data[i]['subject'])
            d['body'].append(self.raw_email_data[i]['body'])
            d['from'].append(self.raw_email_data[i]['from'])
            d['has_attachment'].append(self.raw_email_data[i]['has_attachment'])

        df = pd.DataFrame(d)

        return df
    
    def read_json_file(self):
        return json.dumps(self.raw_email_data, indent=2)
    
    def convert_response_to_dict(self, ai_response):
        results = json.loads(ai_response)
        return results
        
    def convert_response_to_dataframe(self, ai_response):
        
        results = json.loads(ai_response)
        df = pd.DataFrame(results).reset_index(drop=True)
        return df



    

    