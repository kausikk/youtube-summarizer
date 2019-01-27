import requests
import json
from summarizer.punctuator import punctuate

#usage: make a Summary object with the desired size, call get_sentences(transcript)
#to get a transcript
#basically, this sets up a way to interface with the resoomer API
class Summary(object):
    API_KEY =  "570E046C8BDC6F1135C159A938F6A528"
    URL = "https://resoomer.pro/summarizer/size/"

    def __init__(self, size):
        self.size = size

    #queries resoomer and stores response into this object
    def get_summary(self, text):
        data = {"API_KEY" : Summary.API_KEY, "size": self.size, "text" : text}
        self.response = requests.post(Summary.URL, data)
        status_code = self.response.status_code
        self.response = self.response.json()
        return status_code

    #parses the response, must be used after get_summary
    #extracts the contents
    def parse(self):
        #need to parse json file
        resp = self.response
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

    #summarizes a transcript by calling the appropriate functions
    #should be punctuated first
    def get_sentences(self, transcript):
        self.get_summary(transcript)
        summary = self.parse()

        #reformatting string
        summary = summary.replace("... ", ', ')
        summary = summary.replace('? ', '. ')
        summary = summary.replace("<br /><br />", "")
        summary = summary.replace("<br />", "")
        sentences = summary.split('. ')
        for sentence in sentences:
            if len(sentence) < 3:
                sentences.remove(sentence)

        return sentences

text = '''
Just time for a quick recap of the week - and it has been a dramatic one for President Trump - a flesh vessel possessed by the world's thirty dumbest ghosts on Wednesday, an unnamed senior White House official wrote an op-ed in The Times, claiming that Trump's actions are detrimental To the health of our republic, Trump immediately push back, tweeting treason in all caps and then attacks the anonymous writer at a rally. The latest act of resistors is the op-ed published in the failing New York Times by an anonymous, really ended anomalies. That was Howard. You know I don't like Trump's policies, ideas or demeanor, but I do like how he occasionally sounds like a Teddy Ruxpin someone fished out of a lake, reportedly obsessed with finding out the anonymous source. His problem is, it seems like it could be. Almost anyone who works for it, because this week also saw explosive excerpts from Bob Woodward's upcoming book, in which general mattis is quoted as saying Trump has the understanding of a fifth or sixth grader and John Kelly reportedly says we're in crazy town. I don't even know why any of us are here. This is the worst job I've ever had now. Now both men deny making those statements absolutely sure that Kelly loves his job. He seems so happy whenever you see the books most incredible claim. Is that John doubt the president's then lawyer went directly to robert muller and told him trump was such a disaster during a practice interrogation that he couldn't possibly allow him to testify? Woodward quotes dad is saying during a march 5th meeting with muller, i'm not going to sit there and let him look like an idiot and you published that transcript, because everything leaks in washington and the guys overseas are going to say. I told you he was an idiot, i told you he was a goddamn dumbbell, [ Applause, ] prosecutor, a prosecutor that his client will be so stupid under questioning it would be a genuine national security concern. Well, Dowd also denied those comments. Let'S just appreciate for a moment how charming it is to call anyone a god, damn dumbbell, it's so much more delightful than idiot or dipshit or fucking. Moron dumbbell just puts a fun cartoon image in your head anyway, the president said disaster and we're all gon na die. Meanwhile, meanwhile, the week
'''
summarizer = Summary(20)
print(summarizer.get_sentences(text))

#example way to go from url to summary
def run(url):
    from ytube_transcript import get_transcript_from_url
    from wordobjectforfiletranscript import parse_transcript_into_string
    transcriptResponse = get_transcript_from_url(url) #gets the transcript response from api
    transcriptRaw = parse_transcript_into_string(transcriptResponse) #the raw transcript data
    #raw data is available here
    uTranscript = open('transcriptu.txt', 'w+')
    uTranscript.write(transcriptRaw)
    summarizer = Summary(20) #create summary object
    punctuatedtranscript = punctuate(transcriptRaw) #punctuate transcript
    #punctuated data available here
    pTranscript = open('transcriptp.txt', 'w+')
    pTranscript.write(punctuatedtranscript)
    final_sentences = summarizer.get_sentences(punctuatedtranscript) #the resultant sentences from the summarizer
    #a list, one sentence per entry

    #the final summarized
    temp = ''
    for sentence in final_sentences:
        temp += sentence
        temp += ". \n"
    sTranscript = open('transcripts.txt', 'w+')
    sTranscript.write(temp)
