console.log("popup.js runs");

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('button').addEventListener('click', initializeSummary);
});

function initializeSummary() {
  chrome.runtime.sendMessage({action: "initializeSummary", percent: 2}, (response) => {});
}

chrome.extension.onMessage.addListener(function(msg, sender, sendResponse) {
    if (msg.action == "respondToButton") {
      console.log(msg.result);
    }
});
