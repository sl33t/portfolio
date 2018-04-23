var isDropDownOpen = false;

function dropdown() {
    var nav = document.getElementById("nav");
    if (isDropDownOpen){
        nav.style.display = "none";
    }
    else {
        nav.style.display = "block";
    }
    isDropDownOpen = !isDropDownOpen;
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