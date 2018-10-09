function click(e) {
    chrome.tabs.executeScript(null, { file: "jquery-3.3.1.slim.js" }, function() {
        if (e.target.id == "selectSubmit") {
            chrome.tabs.executeScript(null, { file: "randomjs.js" });
            chrome.tabs.executeScript(null, { code: "setTimeout(\"$('#submit_button').click()\", 300)" });
        } else if (e.target.id == "selectAll") {
            chrome.tabs.executeScript(null, { file: "randomjs.js" });
        } else if (e.target.id == "submit") {
            chrome.tabs.executeScript(null, { code: "$('#submit_button').click()" });
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    var divs = document.querySelectorAll('button');
    for (var i = 0; i < divs.length; i++) {
        divs[i].addEventListener('click', click);
    }
});