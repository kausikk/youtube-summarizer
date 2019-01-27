# youtube-summarizer

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
