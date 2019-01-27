'use strict';
console.log("background.js runs")
//
// chrome.runtime.onInstalled.addListener(setup);
// function setup() {
//   var sumPercent = 30;
//
//   chrome.storage.local.get(['key'], function(result) {
//     if (result.key != null) {
//       sumPercent = result.key;
//     }
//   });
// }
//
//
// chrome.storage.local.set({key: value}, function() {
//   console.log('Value is set to ' + value);
// });
//
//



// var xhttp = new XMLHttpRequest();
// xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//        console.log("server response: " + xhttp.responseText);
//     }
// };
//
// xhttp.open("GET", "http://127.0.0.1:8000/summarizer", true);
// xhttp.send();
chrome.runtime.onMessage.addListener( function(request,sender,sendResponse)
{
    if( request.greeting === "GetURL" )
    {
        var tabURL = "Not set yet";
        chrome.tabs.query({active:true},function(tabs){
            if(tabs.length === 0) {
                sendResponse({});
                return;
            }
            tabURL = tabs[0].url;
            sendResponse( {navURL:tabURL} );
        });
    }
})


var prevUrl = ""
chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
  if (tab.status == "complete" && tab.url != prevUrl) {
    prevUrl = tab.url;
  }
});

// let msg = {
//   txt: "encrypted message!"
// }
// chrome.tabs.sendMessage(tab.id, msg);

// chrome.webNavigation.onCompleted.addListener(function() {
//   chrome.browserAction.setBadgeText({text: "ON"});
//   alert("This is my favorite website!");
// },
// {
//   url: [{urlMatches : 'https://www.youtube.com/*'}]
// });
//
//
//
// document.getElementById("summarizeButton").addEventListener('click', initializeSummary);



// function saveTabData(tab) {
//   if (tab.incognito) {
//     return;
//   } else {
//     chrome.storage.local.set({data: tab.url});
//   }
// }
//

// function buttonClicked(tab) {
//   console.log("button clicked!");
//   console.log(tab);
//
//   let msg = {
//     txt: "encrypted message!"
//   }
// chrome.tabs.sendMessage(tab.id, "heyo!");
