
import os

# Imports the Selenium libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Imports the Google Cloud client library
import io
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Imports Youtube Caption API
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(ytube_id):
    ytube_url = 'https://www.youtube.com/watch?v=' + ytube_id
    return get_transcript_from_url(ytube_url)

# Private helpers------------------------------------------------
def get_transcript_from_url(ytube_url):
    result = 'Not available'
    try:
        result = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        pass
    return results

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

def get_transcript_from_ogg(ogg_name):

    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(__file__),
        ogg_name)

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=48000,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))

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
