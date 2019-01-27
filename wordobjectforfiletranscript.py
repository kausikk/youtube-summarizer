#word object with timestamp
class Word(object):
    def __init__(self, word, timestamp):
        self.word = word
        self.timestamp = timestamp

#time object
class TimeStamp(object):
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __init__(self, seconds):
        self.hours = seconds % 3600
        seconds = int(seconds / 3600)
        self.minutes = seconds % 60
        seconds = int(seconds / 60)
        self.seconds = seconds

    def __str__(self):
        return (str(self.hours) + ':' + str(self.minutes) + ':' + str(self.seconds))

#returns a list of words with timestamps from youtube api
def parse_transcript_into_words(transcript):
    for entry in transcript: 
        timestamp = TimeStamp(entry['start'])
        sentence = get_words_from_sentence(entry['text'])
        wordList = []
        for word in sentence:
            wordList.append(Word(word, timestamp))
    return wordList

#returns a list of words with timestamps from a text file
def parse_transcript_into_words_from_file(fileName):
    transcript = open(fileName)
    wordList = []
    for line1, line2 in zip(*[iter(transcript.readlines())]*2):
        line1 = line1.strip('\n')
        line2 = line2.strip('\n')
        timestamp = get_timestamp_from_file(line1)
        sentence = get_words_from_sentence(line2)
        for word in sentence: 
            wordList.append(Word(word, timestamp))
    return wordList

#reads timestamp as a line
def get_timestamp_from_file(line):
    splitTime = line.split(':')
    if len(splitTime) == 2:
        ts = TimeStamp(0, splitTime[0], splitTime[1])
    else:
        ts = TimeStamp(splitTime[0], splitTime[1], splitTime[2])
    return ts

#splits sentence
def get_words_from_sentence(line):
    return line.split()

test = parse_transcript_into_words_from_file('./ltttranscripts/ltttranscript.txt')

for word in test:
    print(word.word)
    print(str(word.timestamp))