#word wrapper with timestamp
class Word(object):
    def __init__(self, word, timestamp):
        self.word = word
        self.timestamp = timestamp
    def __str__(self):
        return str(self.word) + " at " + str(self.timestamp)

#timestamp wrapper
class TimeStamp(object):
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    #use this if you have raw seconds
    @classmethod
    def fromSeconds(cls, seconds):
        hours = seconds % 3600
        seconds = int(seconds / 3600)
        minutes = seconds % 60
        seconds = int(seconds / 60)
        seconds = seconds
        return TimeStamp(hours, minutes, seconds)

    #pretty printing
    def __str__(self):
        return (str(self.hours) + ':' + str(self.minutes) + ':' + str(self.seconds))

#does whatever tom says it does
def parse_transcript(transcript):
    result = ""
    word_list = []
    for entry in transcript:
        result += entry['text'] + ' '
        timestamp = TimeStamp.fromSeconds(entry['start'])
        sentence = get_words_from_sentence(entry['text'])
        for word in sentence:
            word_list.append(Word(word, timestamp))
    return result, word_list


#returns a list of words with timestamps from youtube api
def parse_transcript_into_words(transcript):
    for entry in transcript:
        timestamp = TimeStamp.fromSeconds(entry['start'])
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
