from ytube_transcript import get_transcript_from_url
from wordobjectforfiletranscript import parse_transcript
from punctuator import punctuate
from summarizer import Summary


def execute(ytube_id, percent):
    print('********get transcript from url*******\n')
    transcript = get_transcript_from_url(ytube_id)
    print(transcript)
    print('**********raw transcript***********\n')
    transcript_raw, word_list = parse_transcript(transcript)
    print(transcript_raw)
    transcript_raw = transcript_raw.replace('.', '*')
    print('**********word list***********\n')
    for word in word_list:
        print(str(word))
    print('**********punctuate**********\n')
    punctuated_transcript = punctuate(transcript_raw)
    print(punctuated_transcript)
    print('**********split sentence**********\n')
    sentence_list = split_by_sentence(punctuated_transcript)
    print(sentence_list)
    print('**********get percent**********\n')
    size = int(len(sentence_list)*percent)
    print(size)
    print(len(sentence_list))
    print('**********match time stamp**********\n')
    sentence_time_dict = time_match(sentence_list, word_list)
    for key, value in sentence_time_dict.items():
        print (str(key) + " at " + str(value))
    print('**********initialize summarizer**********\n')
    summarizer = Summary(size)
    print('**********summarized list**********\n')
    summarized_list = summarizer.get_sentences(punctuated_transcript)
    print(summarized_list)
    print('**********get final time stamp dict**********\n')
    time_stamp_dict = return_time_stamp(sentence_time_dict, summarized_list)
    for key, value in time_stamp_dict.items():
        print (str(key) + " at " + str(value))

def time_match(sentences, words):
    response = {}
    while len(words) != 0:
        ordered_pair = words[0]
        del words[0]
        word = ordered_pair.word
        if (len(sentences) == 0):
            break
        sentence = sentences[0]
        del sentences[0]
        sentence_array = sentence.split()
        response[sentence] = ordered_pair.timestamp
        for i in range(len(sentence_array)-1):
            if(len(words)!= 0):
                del words[0]
            else:
                break
    return response

def split_by_sentence(text):
    mod_text = text.replace('?', '.').replace('...',',').replace('!', '.')
    sentence_list = mod_text.split('.')
    return sentence_list

def return_time_stamp(sentence_dict, summary):
    time_stamp_dict = {}
    sentence_dict_trim = {}
    for key, value in sentence_dict.items():
        trim_string = key.replace(' ', '')
        sentence_dict_trim[trim_string] = value
        print (trim_string)
    for sentence in summary:
        sentence_trim = sentence.replace(' ', '')
        try:
            time_stamp_dict[sentence] = sentence_dict_trim[sentence_trim]
        except:
            continue
    return time_stamp_dict

execute("9aULhzn37DE", 0.2)
