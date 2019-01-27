console.log("popup.js runs");

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('button').addEventListener('click', initializeSummary);
});

var port = chrome.extension.connect({
    name: "Port"
});

function initializeSummary(tab) {
  console.log("Summary initialized.");
  port.postMessage(40);
}

port.onMessage.addListener(function(msg) {
  if (msg == "noCaption") {
    console.log("No caption for this video!");
  }
});
