function click(e) {
    if (e.target.id == "selectSubmit") {
        chrome.tabs.executeScript(null, { file: "randomjs.js" });
        chrome.tabs.executeScript(null, { code: "setTimeout(\"document.getElementById('submit_button').click()\", 300)" });
    } else if (e.target.id == "selectAll") {
        chrome.tabs.executeScript(null, { file: "randomjs.js" });
    } else if (e.target.id == "submit") {
        chrome.tabs.executeScript(null, { code: "document.getElementById('submit_button').click()" });
    }
}

function isreDreact(tabs) {
    let currentURL = tabs[0].url;
    console.log(currentURL);
    var pat = /(https:\/\/www\.wjx\.cn\/)(jq|m)(.*)/g;
    var obj = pat.exec(currentURL);

    if (obj && obj.length >= 4) {
        if (obj[2] == "m") {
            console.log("redirect now");
            chrome.tabs.query({ active: true, currentWindow: true }, function() {
                let js = "window.location.href ='" + obj[1] + "jq" + obj[3] + "'";
                console.log(js);
                chrome.tabs.executeScript(null, { code: js });
            });
        } else {
            console.log("do!");
        }
    }
}



document.addEventListener('DOMContentLoaded', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, isreDreact);
    chrome.tabs.executeScript(null, { file: "randomjs.js" });
    chrome.tabs.executeScript(null, { file: "inject.js" });
    var divs = document.querySelectorAll('button');
    for (var i = 0; i < divs.length; i++) {
        divs[i].addEventListener('click', click);
    }
});