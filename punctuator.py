import requests

def punctuate(transcript):
    url = 'http://bark.phon.ioc.ee/punctuator'
    transcript = transcript.replace('\n', ' ')
    text = {'text' : transcript}

    r = requests.post(url, data=text)

    return r.text
