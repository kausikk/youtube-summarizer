console.log("popup.js runs");

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('button').addEventListener('click', initializeSummary);
});

function initializeSummary() {
  var dropdown = document.getElementById('percent-dropdown')
  value = dropdown.options[dropdown.selectedIndex].text
  console.log(value)
  if (value == 'Summary Percentage') {
    return;
  }
  chrome.runtime.sendMessage({action: "initializeSummary", percent: value}, (response) => {});
}

chrome.extension.onMessage.addListener(function(msg, sender, sendResponse) {
    if (msg.action == "respondToButton") {
      document.getElementById('text-out').innerHTML = msg.result
    }
});
