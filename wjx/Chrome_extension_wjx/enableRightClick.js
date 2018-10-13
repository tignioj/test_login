window.addEventListener("contextmenu",
    function(e) {
        e.stopPropagation();
    }, true);
window.addEventListener("selectstart",
    function(e) {
        e.stopPropagation();
    }, true);

window.addEventListener("copy",
    function(e) {
        e.stopPropagation();
    }, true);
document.oncontextmenu = document.onselectstart = document.body.onselectstart = document.oncopy = document.body.oncopy = ""