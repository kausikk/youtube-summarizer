'use strict';

chrome.browserAction.onClicked.addListener(buttonClicked);

function buttonClicked(tab) {

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
         // Typical action to be performed when the document is ready:
         console.log(xhttp.responseText);
      }
  };
  xhttp.open("GET", "169.254.76.237:8000/helloworld", true);
  xhttp.send();

  console.log("button clicked!");
  console.log(tab);

  let msg = {
    txt: "encrypted message!"
  }
  chrome.tabs.sendMessage(tab.id, msg);
}


chrome.runtime.onInstalled.addListener(setup);

function setup() {
}

// chrome.webNavigation.onCompleted.addListener(function() {
//   chrome.browserAction.setBadgeText({text: "ON"});
//   alert("This is my favorite website!");
// },
// {
//   url: [{urlMatches : 'https://www.youtube.com/'}]
// });
