console.log("content.js runs");
//
//
// chrome.runtime.onMessage.addListener(gotMessage);
//
// function gotMessage(message, sender, sendResponse) {
//   console.log(message);
// }

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
      sendResponse({action: "okay"});
  });
