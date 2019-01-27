import requests
import json
from punctuator import punctuate

#usage: make a Summary object with the desired size, call get_sentences(transcript)

class Summary(object):
    API_KEY =  "4A85F76E758693632041F21373D5B23D"
    URL = "https://resoomer.pro/summarizer/size"

    def __init__(self, size):
        self.size = size

    def get_summary(self, text):
        data = {"API_KEY" : Summary.API_KEY, "text" : text, "size" : self.size}
        self.response = requests.post(Summary.URL, data)
        return self.response.status_code;
 
    def parse(self):
        #need to parse json file
        resp = self.response.json()
        result = resp['text']['content']
        result = result[:-6]
        return result
        #json = json.loads(self.response)

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
        return 0
    
    #punctuates and summarizes
    def get_sentences(self, transcript):
        summarizer = Summary(self.size)
        summarizer.get_summary(transcript)
        summary = summarizer.parse()

        summary = summary.replace("... ", ', ')
        summary = summary.replace('? ', '. ')
        sentences = summary.split('. ')  
        return sentences

def run(url):
    from ytube_transcript import get_transcript_from_url
    from wordobjectforfiletranscript import parse_transcript_into_string
    transcript = get_transcript_from_url(url)
    transcripted = parse_transcript_into_string(transcript)
    uTranscript = open('transcriptu.txt', 'w+')
    uTranscript.write(transcripted)
    summarizer = Summary(20)
    punctuatedtranscript = punctuate(transcripted)
    pTranscript = open('transcriptp.txt', 'w+')
    pTranscript.write(punctuatedtranscript)
    final_sentences = summarizer.get_sentences(punctuatedtranscript)
    
    temp = ''
    for sentence in final_sentences:
        temp += sentence
        temp += ". \n"
    sTranscript = open('transcripts.txt', 'w+')    
    sTranscript.write(temp)