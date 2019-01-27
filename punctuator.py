import requests

url = 'http://bark.phon.ioc.ee/punctuator'

file = open('testFile.txt', 'r').read().replace('\n', ' ')

text = {'text' : file}

r = requests.post(url, data=text)

newFile = open('dest.txt', 'w+')
newFile.write(r.text)