//Edge show speedUp_muted_bq() undefined

//enable right click;
//document.oncontextmenu = document.onselectstart = document.body.onselectstart = document.oncopy = document.body.oncopy = ""
function speedUp_muted_bq() {

    $(".speedTab15")[0].click();
    setTimeout(function() {
        document.getElementById("vjs_mediaplayer_html5_api").muted = true;
    }, 1000);
    $(".line1bq")[0].click();
}

function autoChooseTest() {
    //check if the test window is open
    var video = document.getElementById("vjs_mediaplayer_html5_api");
    if (!video.paused) {
        console.log(video.paused);
        return;
    } else {
        try {
            //choose right answer
            var myradio = document.getElementById("tmDialog_iframe").contentWindow.document.getElementsByClassName("answerOption");
            for (var i = 0; i < myradio.length; i++) {
                if (myradio[i].getElementsByTagName("input")[0].getAttribute("_correctanswer") == "1") {
                    $(".popbtn_cancel")[0].click();
                    myradio[i].getElementsByTagName("input")[0].click();
                }
                //double  click checked;
                if (myradio[i].getElementsByTagName("input")[0].getAttribute("checked") == "checked") {
                    myradio[i].getElementsByTagName("input")[0].click();
                }
            }
        } catch (err) {
            console.log(err);
        }
    }
}

function nextVideo() {
    var video = document.getElementById("vjs_mediaplayer_html5_api");
    //testTest if it has accelerated
    if (video.playbackRate != 1.5) {
        setTimeout(function() {
            speedUp_muted_bq();
        }, 1500);
    }
    var p = document.getElementsByClassName("progressbar")[0];
    var width = document.defaultView.getComputedStyle(p, null).width;

    var str = p.getAttribute("style");
    var regex = new RegExp("[0-9]+");
    var obj = regex.exec(str);
    var isProcessFinish = false;
    if (obj != undefined) {
        console.log(obj);
        if (parseInt(obj[0]) >= 100) {
            isProcessFinish = true;
        } else {
            isProcessFinish = false;
        }
    }

    if ((video.currentTime / video.duration) >= 1 || isProcessFinish) {
        console.log("Finish");
        $(".tm_next_lesson")[0].click();
        setTimeout(function() {
            speedUp_muted_bq();
        }, 1500);
    }
}

speedUp_muted_bq();
var myInterval = setInterval(function() {
    autoChooseTest();
    nextVideo();
}, 5000);