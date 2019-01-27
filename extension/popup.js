document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('button').addEventListener('click', initializeSummary);
});

var port = chrome.extension.connect({
    name: "Sample Communication"
});

function initializeSummary(tab) {
  console.log("Summary initialized.");
  port.postMessage("wantURL");
}

port.onMessage.addListener(function(msg) {
    console.log("message recieved" + msg);
});
