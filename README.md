# youtube-summarizer
Made by Vala Vakilian, Thong Nguyen, Pedram Amani, Kausik Krishnakumar, and Fisher Xue for nwHacks 2019!

#What it is:
-

#How to use:
- Set up a virtual environment in an appropriate location
- Activate the virtual environment and install dependencies
```
pip install -r requirement.txt
```
- Open up chrome://extensions/ and switch on Developer mode
- Select load unpacked and select the extension folder in this repo
- Open up Youtube and summarizing again !


# Dependencies:

# 1. For getting Youtube captions 
- pip install youtube_transcript_api
# 2. # For getting audio from Youtube url with headless browser: 
- https://sites.google.com/a/chromium.org/chromedriver/downloads
- pip install selenium
- Add current repo directory to PATH to allow Selenium to access the chromedriver.exe
# 3. For transcribing audio
- pip install --upgrade google-cloud-speech
- Make GOOGLE_APPLICATION_CREDENTIALS environment variable and point to credentials.json file
# 4. For converting mp3 to ogg
- pip install --upgrade pydub
# 5. For uploading ogg to Google Cloud Storage
- pip install --upgrade google-cloud-storage
- https://cloud.google.com/storage/docs/reference/libraries#client-libraries-install-python
