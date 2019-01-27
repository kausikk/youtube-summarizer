
c// hrome.browserAction.onClicked.addListener(buttonClicked);

function buttonClicked(tab) {
  let sumInfo = JSON.stringify({
    url: tab.url,
    sumPercent: 10
  });

  xmlhttp.open("GET","127.0.0.1:8000/admin/");
  xmlhttp.send();
}



// let paragraphs = document.getElementsByTagName('p');
// for (elt of paragraphs) {
//   elt.style['background-color'] = '#FF00FF';
// }
// tab.url
// chrome.runtime.onMessage.addListener(gotMessage);
//
// function gotMessage(message, sender, sendResponse) {
//   console.log(message.txt);
// }
