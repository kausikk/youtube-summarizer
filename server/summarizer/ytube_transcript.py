"""
Library for obtaining/generating transcript for a youtube video
"""
import os

# Imports the Selenium libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
'''
# Imports the Google Cloud client library
import io
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Imports Google Cloud Storage
from google.cloud import storage
from google.cloud.storage import Blob
'''

# Imports Youtube Caption API
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(ytube_id):
    ytube_url = 'https://www.youtube.com/watch?v=' + ytube_id
    return get_transcript_from_url(ytube_url)

# Private helpers------------------------------------------------
def get_transcript_from_url(ytube_id):
    result = 'Not available'
    try:
        result = YouTubeTranscriptApi.get_transcript(ytube_id)
    except Exception as e:
        pass
    return result

def get_ytube_mp3(ytube_url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    result = ''
    driver.get("https://www.onlinevideoconverter.com/youtube-converter")

    driver.find_element_by_id('texturl').send_keys(ytube_url)
    driver.find_element_by_id('convert1').click()

    try:
        result = wait_for_dl_link(driver)
    except Exception as e:
        print(e)
        result = 'No link found'

    driver.quit()
    return result

def wait_for_dl_link(driver):
    i = 0
    result = ''
    while i < 10 and result == '':
        try:
            i += 1
            time.sleep(1)
            result = driver.find_element_by_id('downloadq').get_attribute('href')
        except Exception as e:
            print(e)
    return result

def get_transcript_from_ogg(ogg_name):
    # Instantiates a client
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri='gs://youtube-sum/' + ogg_name)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=48000,
        language_code='en-US')

    # Detects speech in the audio file
    operation = client.long_running_recognize(config, audio)
    response = operation.result()

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))

def upload_audio(ogg_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('youtube-sum')
    blob = bucket.blob(ogg_name)

    source_file_name = make_path_name(ogg_name)
    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to gs://youtube-sum/{}'.format(
        source_file_name,
        ogg_name))

def make_path_name(file_name):
    return os.path.join(
        os.path.dirname(__file__),
        file_name)
