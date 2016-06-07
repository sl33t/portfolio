function dropdown() {
    $(".dropdown").toggle();
}

window.onresize = function (event) {
    if (screen.width > 1280) {
        var mobilelinks = document.getElementsByClassName("mobilelinks");
        for (var i = 0; i < mobilelinks.length; i++) {
            mobilelinks[i].removeAttribute('style');
        }
        document.getElementById("nav").removeAttribute('style');
    }
};

function close_messages() {
    document.getElementById("messages_backdrop").style.display = "none";
}