var bg = document.body;

function onResizeEventHandler() {
    bg.setAttribute("height", document.documentElement.getAttribute("height"));
}

var el = window;
if (el.addEventListener)
    el.addEventListener("resize", onResizeEventHandler, false);   
else if (el.attachEvent)
    el.attachEvent("resize", onResizeEventHandler); 

onResizeEventHandler();