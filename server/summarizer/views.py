from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from ytube_transcript import get_transcript_from_url
from wordobjectforfiletranscript import parse_transcript
from punctuator import punctuate
from summarizer import Summary

# Create your views here.

transcript = ""

def check(request, ytube_id):
    global transcript
    transcript = get_transcript_from_url(ytube_id)
    if(transcript == "Not available"):
        return HttpResponse("Caption not available")
    else:
        return HttpResponse("Caption available")


def execute(request, ytube_id, percent):
    global transcript
    transcript_raw, word_list = parse_transcript(transcript)
    punctuated_transcript = punctuate(transcript_raw)
    sentence_list = split_by_sentence(transcript_raw)
    size = int(len(sentence_list)*percent)
    sentence_time_dict = time_match(sentence_list, word_list)
    summarizer = Summary(size)
    summarized_list = summarizer.get_sentences(punctuated_transcript)
    time_stamp_dict = return_time_stamp(sentence_time_dict, summarized_list)
    return HttpResponse(time_stamp_dict)
