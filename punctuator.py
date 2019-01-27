import requests

def punctuate(fileName):
    url = 'http://bark.phon.ioc.ee/punctuator'
    file = open(fileName, 'r').read().replace('\n', ' ')
    text = {'text' : file}

    r = requests.post(url, data=text)

    newFile = open(fileName, 'w+')
    newFile.write(r.text)
    return 0