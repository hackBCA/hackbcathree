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

var icons = ["fa-heart", "fa-bolt", "fa-bug", "fa-fighter-jet", "fa-code", "fa-paw", "fa-rocket", "fa-wifi", "fa-terminal", "fa-trophy", "fa-scissors", "fa-star", "fa-cogs", "fa-code-fork", "fa-coffee", "fa-money", "fa-magic", "fa-headphones", "fa-anchor", "fa-flask"];


if (document.querySelector("#credit i")) {
    var prev_icon = icons[Math.floor(Math.random() * icons.length)];
    document.querySelector("#credit i").classList.add(prev_icon);

    setInterval(cycle, 1000);

    function cycle() {
        var new_icon = icons[Math.floor(Math.random() * icons.length)];
        document.querySelector("#credit i").classList.remove(prev_icon);
        document.querySelector("#credit i").classList.add(new_icon);
        prev_icon = new_icon;
    }
}

function labelSimulateClick () {
    var labels = document.querySelectorAll("label");
    console.log(labels);
    for (var i = 0; i < labels.length; i++) {
        labels[i].onclick = function() {
            var associated = this.getAttribute("for");
            document.getElementById(associated).click();
        }
    }
}

labelSimulateClick();