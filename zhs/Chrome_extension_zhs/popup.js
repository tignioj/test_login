function click(e) {
    chrome.tabs.executeScript(null, { file: "jquery-3.3.1.slim.js" }, function() {

        if (e.target.id == "SpeedUP") {
            chrome.tabs.executeScript(null, { file: "ChromeVersionPassVideo.js" });
            //chrome.tabs.executeScript(null, { file: "test.js" });
        } else if (e.target.id == "enableRightClick") {
            let s = '';
            list = ['$(".myschool_ewcon")[0]', 'document', 'document.body'];
            for (var i of list) {
                s += (i + '.addEventListener("contextmenu", function(e){ e.stopPropagation() }, true);');
                s += (i + '.addEventListener("selectstart", function(e){ e.stopPropagation() }, true);');
                s += (i + '.addEventListener("copy", function(e){ e.stopPropagation() }, true);');
            }
            chrome.tabs.executeScript(null, { code: s });
        } else if (e.target.id == "Restore") {
            let s = '';
            s = "clearInterval(myInterval);$('.speedTab05')[0].click();";
            chrome.tabs.executeScript(null, { code: s });
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    var divs = document.querySelectorAll('button');
    for (var i = 0; i < divs.length; i++) {
        divs[i].addEventListener('click', click);
    }
});