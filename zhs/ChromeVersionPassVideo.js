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
    if (!document.getElementById("tmDialog_iframe")) {
        return;
    } else {
        //choose right answer
        var myradio = document.getElementById("tmDialog_iframe").contentWindow.document.getElementsByClassName("answerOption");
        for (var i = 0; i < myradio.length; i++) {
            if (myradio[i].getElementsByTagName("input")[0].getAttribute("_correctanswer") == "1")
                myradio[i].getElementsByTagName("input")[0].click();
            //double  click checked;
            if (myradio[i].getElementsByTagName("input")[0].getAttribute("checked") == "checked")
                myradio[i].getElementsByTagName("input")[0].click();
        }
    }


    //close the window of answer
    for (var i = 0; i < $(".popbtn_cancel span").length; i++) {
        if ($(".popbtn_cancel span")[i].innerHTML == "关闭" || $(".popbtn_cancel span")[i].innerHTML == "Close") {
            $(".popbtn_cancel span")[i].click();
            //console.log($(".popbtn_cancel span")[i].innerHTML);
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
    if ((video.currentTime / video.duration) >= 1) {
        console.log("Finish");
        $(".tm_next_lesson")[0].click();
        setTimeout(function() {
            speedUp_muted_bq();
        }, 1500);
    }
    //If a chapter is finish, test if next video  is as same to the current video
}

//Start 
speedUp_muted_bq();
var myInterval = setInterval(function() {
    autoChooseTest();
    nextVideo();
}, 5000);