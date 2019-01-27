console.log("content.js runs");

chrome.extension.onMessage.addListener(function(msg, sender, sendResponse) {
  if (msg.action == 'startLoadingWindow') {
    // Start loading window
  }
});
