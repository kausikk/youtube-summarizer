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
    print('**********word list***********\n')
    print(word_list)
    print('**********punctuate**********\n')
    punctuated_transcript = punctuate(transcript_raw)
    print(punctuated_transcript)
    print('**********split sentence**********\n')
    sentence_list = split_by_sentence(transcript_raw)
    print(sentence_list)
    print('**********get percent**********\n')
    size = int(len(sentence_list)*percent)
    print(size)
    print('**********match time stamp**********\n')
    sentence_time_dict = time_match(sentence_list, word_list)
    print(sentence_time_dict)
    print('**********initialize summarizer**********\n')
    summarizer = Summary(size)
    print('**********summarized list**********\n')
    summarized_list = summarizer.get_sentences(punctuated_transcript)
    print(summarized_list)
    print('**********get final time stamp dict**********\n')
    time_stamp_dict = return_time_stamp(sentence_time_dict, summarized_list)
    print(time_stamp_dict)

def time_match(sentences, words):
    response = {}
    while len(words) != 0:
        ordered_pair = words.popleft()
        word = ordered_pair.word
        sentence = sentences.popleft()
        sentence_array = sentence.split()
        response[sentence] = ordered_pair.timestamp
        for i in range(len(sentence_array)):
            words.popleft()
    return response

def split_by_sentence(text):
    mod_text = text.replace('?', '.').replace('...',',').replace('!', '.')
    sentence_list = mod_text.split('.')
    return sentence_list

def return_time_stamp(sentence_dict, summary):
    time_stamp_dict = {}
    for sentence in summary:
        time_stamp_dict[sentence] = sentence_dict[sentence]
    return time_stamp_list

execute("9aULhzn37DE", 0.4)
