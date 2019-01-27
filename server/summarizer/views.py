from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from ytube_transcript import get_transcript_from_url
from wordobjectforfiletranscript import parse_transcript
from punctuator import punctuate
from summarizer import Summary
import json

# Create your views here.

transcript = ""

def check(request, ytube_id):
    global transcript
    transcript = get_transcript_from_url(ytube_id)
    if(transcript == "Not available"):
        return HttpResponse(False)
    else:
        return HttpResponse(True)


def execute(request, ytube_id, percent):
    transcript = get_transcript_from_url(ytube_id)
    transcript_raw, word_list = parse_transcript(transcript)
    transcript_raw = transcript_raw.replace('.', '*')
    punctuated_transcript = punctuate(transcript_raw)
    sentence_list = split_by_sentence(punctuated_transcript)
    size = int(len(sentence_list)*percent)
    sentence_time_dict = time_match(sentence_list, word_list)
    summarizer = Summary(size)
    summarized_list = summarizer.get_sentences(punctuated_transcript)
    time_stamp_dict = return_time_stamp(sentence_time_dict, summarized_list)
    return HttpResponse(json.dumps(time_stamp_dict, default = dumper, indent = 2))

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__.copy()


print json.dumps(obj, default=dumper, indent=2)

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
