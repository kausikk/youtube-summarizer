from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from youtube_transcript_api import get_transcript_from_url

# Create your views here.

def get_summary(request, ytube_id):
    transcript = get_transcript_from_url(ytube_id)
    if(transcript == 'Not available'):
        return HttpResponse("Caption not available")
    transcript_whole_string = parse_transcript_into_string(transcript)
