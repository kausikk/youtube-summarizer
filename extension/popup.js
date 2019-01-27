document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('button').addEventListener('click', initializeSummary);
});

function initializeSummary(tab) {
  console.log("Summary initialized.");

  chrome.runtime.sendMessage({greeting: "GetURL"},
    function (response) {
        tabURL = response.navURL;
        $("#tabURL").text(tabURL);
    });
}
