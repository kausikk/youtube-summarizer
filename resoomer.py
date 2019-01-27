import requests

class get_summary:
    self.API_KEY =  "4A85F76E758693632041F21373D5B23D"
    self.URL = "https://resoomer.pro/summarizer/size"

    def __init__(self, text, size):
        self.my_text = text;

    def get_summary(self):
        data = {"API_KEY" : self.API_KEY, "size" : size}
        self.response = requests.post(URL, data)
        return self.response.status_code;

    def parse(self):
        #need to parse json file
        '''
        format
        {
        "ok":1,
        "message":"ok",
        "text":{
        "size":45,
        "total_words":219,
        "content":"Your text summarize to 45%..."
        },
        "codeResponse":200
        }
        '''
        return 0;
