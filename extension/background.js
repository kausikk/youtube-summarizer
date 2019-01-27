'use strict';
console.log("background.js runs");

var prevUrl = '';
var prevSummary = '';

chrome.extension.onMessage.addListener(function(msg, sender, sendResponse) {
    if (msg.action == "initializeSummary") {
      chrome.tabs.query({active: true, lastFocusedWindow: true}, (tabs) => {
        if (tabs[0] == null) {
          chrome.runtime.sendMessage({action: "respondToButton", result: "Not a youtube video"});
          return;
        }
        var videoId = tabs[0].url.match('(?<=watch[?]v=).{11}');
        if (videoId != null) {
          console.log(videoId[0]);
          isCaptionAvailable(videoId[0], msg.percent);
        } else {
          chrome.runtime.sendMessage({action: "respondToButton", result: "Not a youtube video"});
        }
      });
    }
});

function isCaptionAvailable(videoId, percent) {
  console.log(videoId, percent);

  var oReq = new XMLHttpRequest();
  oReq.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      if (this.responseText == 'true') {
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
          chrome.tabs.sendMessage(tabs[0].id, {action: "startLoadingWindow"});
        });
        getSummary(videoId, percent)
      } else {
        chrome.runtime.sendMessage({action: "respondToButton", result: "No caption available"});
      }
    }
  };

  oReq.open("GET", "http://127.0.0.1:8000/summarizer/check/" + videoId, true);
  oReq.send();
}

function getSummary(videoId, percentage) {
  console.log("Starting to obtain summary")
  var oReq = new XMLHttpRequest();
  oReq.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var json = this.responseText;
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
          chrome.tabs.sendMessage(tabs[0].id, {action: "obtainedSummary", result: json, vidId: videoId});
        });
      }
  };

  oReq.open("GET", "http://127.0.0.1:8000/summarizer/execute/" + videoId + "/" + percentage, true);
  oReq.send();
}
