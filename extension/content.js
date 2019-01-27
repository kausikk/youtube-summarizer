console.log("content.js runs");

var LOADER_TEXT = "<div class='loader-text'>Obtaining summary</div>"
var LOADER_STYLE = "<style>.loader-text { height: 45px; width: 100%; font-size: x-large; text-align: center; color: var(--yt-spec-text-primary) !important } .sk-circle { width: 40px; height: 40px; position: relative; marign-top: 8px; margin-left: calc(50% - 20px); } .sk-circle .sk-child { width: 100%; height: 100%; position: absolute; left: 0; top: 0; } .sk-circle .sk-child:before { content: ''; display: block; margin: 0 auto; width: 15%; height: 15%; background-color: red !important; border-radius: 100%; -webkit-animation: sk-circleBounceDelay 1.2s infinite ease-in-out both; animation: sk-circleBounceDelay 1.2s infinite ease-in-out both; } .sk-circle .sk-circle2 { -webkit-transform: rotate(30deg); -ms-transform: rotate(30deg); transform: rotate(30deg); } .sk-circle .sk-circle3 { -webkit-transform: rotate(60deg); -ms-transform: rotate(60deg); transform: rotate(60deg); } .sk-circle .sk-circle4 { -webkit-transform: rotate(90deg); -ms-transform: rotate(90deg); transform: rotate(90deg); } .sk-circle .sk-circle5 { -webkit-transform: rotate(120deg); -ms-transform: rotate(120deg); transform: rotate(120deg); } .sk-circle .sk-circle6 { -webkit-transform: rotate(150deg); -ms-transform: rotate(150deg); transform: rotate(150deg); } .sk-circle .sk-circle7 { -webkit-transform: rotate(180deg); -ms-transform: rotate(180deg); transform: rotate(180deg); } .sk-circle .sk-circle8 { -webkit-transform: rotate(210deg); -ms-transform: rotate(210deg); transform: rotate(210deg); } .sk-circle .sk-circle9 { -webkit-transform: rotate(240deg); -ms-transform: rotate(240deg); transform: rotate(240deg); } .sk-circle .sk-circle10 { -webkit-transform: rotate(270deg); -ms-transform: rotate(270deg); transform: rotate(270deg); } .sk-circle .sk-circle11 { -webkit-transform: rotate(300deg); -ms-transform: rotate(300deg); transform: rotate(300deg); } .sk-circle .sk-circle12 { -webkit-transform: rotate(330deg); -ms-transform: rotate(330deg); transform: rotate(330deg); } .sk-circle .sk-circle2:before { -webkit-animation-delay: -1.1s; animation-delay: -1.1s; } .sk-circle .sk-circle3:before { -webkit-animation-delay: -1s; animation-delay: -1s; } .sk-circle .sk-circle4:before { -webkit-animation-delay: -0.9s; animation-delay: -0.9s; } .sk-circle .sk-circle5:before { -webkit-animation-delay: -0.8s; animation-delay: -0.8s; } .sk-circle .sk-circle6:before { -webkit-animation-delay: -0.7s; animation-delay: -0.7s; } .sk-circle .sk-circle7:before { -webkit-animation-delay: -0.6s; animation-delay: -0.6s; } .sk-circle .sk-circle8:before { -webkit-animation-delay: -0.5s; animation-delay: -0.5s; } .sk-circle .sk-circle9:before { -webkit-animation-delay: -0.4s; animation-delay: -0.4s; } .sk-circle .sk-circle10:before { -webkit-animation-delay: -0.3s; animation-delay: -0.3s; } .sk-circle .sk-circle11:before { -webkit-animation-delay: -0.2s; animation-delay: -0.2s; } .sk-circle .sk-circle12:before { -webkit-animation-delay: -0.1s; animation-delay: -0.1s; } @-webkit-keyframes sk-circleBounceDelay { 0%, 80%, 100% { -webkit-transform: scale(0); transform: scale(0); } 40% { -webkit-transform: scale(1); transform: scale(1); } } @keyframes sk-circleBounceDelay { 0%, 80%, 100% { -webkit-transform: scale(0); transform: scale(0); } 40% { -webkit-transform: scale(1); transform: scale(1); } }</style>"
var LOADER_ELEM = '<div class="sk-circle"> <div class="sk-circle1 sk-child"></div> <div class="sk-circle2 sk-child"></div> <div class="sk-circle3 sk-child"></div> <div class="sk-circle4 sk-child"></div> <div class="sk-circle5 sk-child"></div> <div class="sk-circle6 sk-child"></div> <div class="sk-circle7 sk-child"></div> <div class="sk-circle8 sk-child"></div> <div class="sk-circle9 sk-child"></div> <div class="sk-circle10 sk-child"></div> <div class="sk-circle11 sk-child"></div> <div class="sk-circle12 sk-child"></div> </div>'

var SENT_TIME_PAIR_ELEM = '<div style="color: var(--yt-spec-text-primary); width: 100%; font-size: medium; margin: 15px auto; display: flex; justify-content: space-between"><a style="color: #de5f5f; vertical-align: top; width: 8%;">{1}</a><div style="width: 90%; margin-right: 5px;">{2}</div></div>'

var box = null;
chrome.extension.onMessage.addListener(function(msg, sender, sendResponse) {
    console.log("Hello!!!")
    if (msg.action == "startLoadingWindow") {
      if (box == null) {
        var sum_style = document.createElement('style');
        sum_style.innerHTML = '#youtube-summarizer{overflow-y: scroll; margin-top: 20px;}';
        document.body.appendChild(sum_style);

        box = document.createElement('div');
        box.id = "youtube-summarizer";
        box.style.height = '100px';
        box.innerHTML = LOADER_TEXT + LOADER_ELEM + LOADER_STYLE;

        var column = document.getElementById('primary-inner');
        column.insertBefore(box, column.children[2]);
      }
    } else if (msg.action == "obtainedSummary" && box != null) {
      box.style.height = '200px';
      box.innerHTML = '';

      var json = JSON.parse(msg.result)
      var relative_url = '/watch?v=' + msg.vidId + '&t='
      for (const [sentence, timestamp] of Object.entries(json)) {
        //var seconds = Math.round(timestamp.hours * 60 * 60 + timestamp.minutes * 60 + timestamp.seconds);

        var time = timestamp.hours > 0 ? timestamp.hours.toString() + ":" : ''
        time += timestamp.minutes + ":"
        var seconds = Math.round(timestamp.seconds).toString()
        time += seconds.length == 2 ? seconds : "0" + seconds

        box.innerHTML += SENT_TIME_PAIR_ELEM.replace('{1}', time).replace('{2}', sentence);
      }
    }
});

/*
<div id="youtube-summarizer" style="height: 200px;margin-top: 10px;overflow-y: scroll;padding: 5px;">

<div class="sent-time-pair" style="color: var(--yt-spec-text-primary);width: 100%;font-size: medium;margin: 15px auto;">
<a href="www.google.com" style="color: #de5f5f;display: inline-block;vertical-align: top;width: 10%;">0:01:34</a>
<div style="display: inline-block;width: 80%;">That actually makes my garments so when we made that outfit Alette without a mannequin to make the rest of my costumes, so we literally sacrifice sacrifice my might like my dress form and have to make a new one for that runway </div>
</div>




<div class="sent-time-pair" style="color: white;width: 100%;font-size: medium;margin: 15px auto;">
<a href="www.google.com" style="color: #de5f5f;display: inline-block;vertical-align: top;width: 10%;">0:01:34</a>
<div style="display: inline-block;width: 80%;">That actually makes my garments so when we made that outfit Alette without a mannequin to make the rest of my costumes, so we literally sacrifice sacrifice my might like my dress form and have to make a new one for that runway </div>

</div><div class="sent-time-pair" style="color: white;width: 100%;font-size: medium;margin: 15px auto;">
<a href="www.google.com" style="color: #de5f5f;display: inline-block;vertical-align: top;width: 10%;">{}</a>
<div style="display: inline-block;width: 80%;">{}</div>
</div>



<div class="sent-time-pair" style="color: white;width: 100%;font-size: medium;margin: 15px auto;">
<a href="www.google.com" style="color: #de5f5f;display: inline-block;vertical-align: top;width: 10%;">0:01:34</a>
<div style="display: inline-block;width: 80%;">That actually makes my garments so when we made that outfit Alette without a mannequin to make the rest of my costumes, so we literally sacrifice sacrifice my might like my dress form and have to make a new one for that runway </div>

</div><div class="sent-time-pair" style="color: white;width: 100%;font-size: medium;margin: 15px auto;">
<a href="www.google.com" style="color: #de5f5f;display: inline-block;vertical-align: top;width: 10%;">0:01:34</a>
<div style="display: inline-block;width: 80%;">That actually makes my garments so when we made that outfit Alette without a mannequin to make the rest of my costumes, so we literally sacrifice sacrifice my might like my dress form and have to make a new one for that runway </div>
</div>

</div>
*/




/*
<div id="youtube-summarizer" style="height: 200px;margin-top: 10px;overflow-y: scroll;padding: 5px;">

<div class="sent-time-pair" style="color: var(--yt-spec-text-primary);width: 100%;font-size: medium;margin: 15px auto;">
<a href="www.google.com" style="color: #de5f5f;display: inline-block;vertical-align: top;width: 10%;">0:01:34</a>
<div style="display: inline-block;width: 80%;">That actually makes my garments so when we made that outfit Alette without a mannequin to make the rest of my costumes, so we literally sacrifice sacrifice my might like my dress form and have to make a new one for that runway </div>
</div>




<div class="sent-time-pair" style="color: white;width: 100%;font-size: medium;margin: 15px auto;">
<a href="www.google.com" style="color: #de5f5f;display: inline-block;vertical-align: top;width: 10%;">0:01:34</a>
<div style="display: inline-block;width: 80%;">That actually makes my garments so when we made that outfit Alette without a mannequin to make the rest of my costumes, so we literally sacrifice sacrifice my might like my dress form and have to make a new one for that runway </div>
</div><div class="sent-time-pair" style="color: white;width: 100%;font-size: medium;margin: 15px auto;">
<a href="www.google.com" style="color: #de5f5f;display: inline-block;vertical-align: top;width: 10%;">0:01:34</a>
<div style="display: inline-block;width: 80%;">That actually makes my garments so when we made that outfit Alette without a mannequin to make the rest of my costumes, so we literally sacrifice sacrifice my might like my dress form and have to make a new one for that runway </div>
</div>



<div class="sent-time-pair" style="color: white;width: 100%;font-size: medium;margin: 15px auto;">
<a href="www.google.com" style="color: #de5f5f;display: inline-block;vertical-align: top;width: 10%;">0:01:34</a>
<div style="display: inline-block;width: 80%;">That actually makes my garments so when we made that outfit Alette without a mannequin to make the rest of my costumes, so we literally sacrifice sacrifice my might like my dress form and have to make a new one for that runway </div>
</div><div class="sent-time-pair" style="color: white;width: 100%;font-size: medium;margin: 15px auto;">
<a href="www.google.com" style="color: #de5f5f;display: inline-block;vertical-align: top;width: 10%;">0:01:34</a>
<div style="display: inline-block;width: 80%;">That actually makes my garments so when we made that outfit Alette without a mannequin to make the rest of my costumes, so we literally sacrifice sacrifice my might like my dress form and have to make a new one for that runway </div>
</div>

</div>
*/
