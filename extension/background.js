'use strict';
console.log("background.js runs");

chrome.extension.onMessage.addListener(function(msg, sender, sendResponse) {
    if (msg.action == "initializeSummary") {
      chrome.tabs.query({active: true, lastFocusedWindow: true}, (tabs) => {
        if (tabs[0] == null) {
          chrome.runtime.sendMessage({action: "respondToButton", result: "Weird error"});
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

// var port;
// chrome.extension.onConnect.addListener(function(newPort) {
//       console.log("Connected .....");
//       port = newPort;
//       port.onMessage.addListener(function(percent) {
//         chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
//            var videoId = tabs[0].url.match('(?<=watch[?]v=).{11}');
//            if (videoId != null) {
//              //isCaptionAvailable(videoId[0], percent);
//              //port.postMessage("noCaption");
//              console.log(videoId[0]);
//              chrome.tabs.sendMessage(tabs[0].id, {action: startLoadingWindow"});
//            }
//          });
//       });
//  })

function isCaptionAvailable(videoId, percentage) {
  console.log(videoId, percent);
  chrome.tabs.sendMessage(tabs[0].id, {action: "startLoadingWindow"});

  // var oReq = new XMLHttpRequest();
  // oReq.onreadystatechange = function() {
  //     if (this.readyState == 4 && this.status == 200) {
  //       if (true) {
  //         chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  //           chrome.tabs.sendMessage(tabs[0].id, {action: "startLoadingWindow"});
  //         });
  //       } else {
  //         port.postMessage("noCaption");
  //     }
  };
//
//   oReq.open("GET", "http://127.0.0.1:8000/check?id=" + videoId, true);
//   oReq.send();
// }

// function getSummary(videoId, percentage) {
//   var oReq = new XMLHttpRequest();
//   oReq.onreadystatechange = function() {
//       if (this.readyState == 4 && this.status == 200) {
//
//       }
//   };
//
//   oReq.open("GET", "http://127.0.0.1:8000/execute?id=" + videoId + "&percentage=" + percentage, true);
//   oReq.send();
// }
