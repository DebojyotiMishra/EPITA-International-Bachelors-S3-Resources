document.getElementById("hamburger").addEventListener("click", function() {
    document.getElementById("nav-menu").classList.add("open");
    document.getElementById("hamburger").classList.add("hide");
    document.getElementById("close-menu").style.display = "block";
});

document.getElementById("close-menu").addEventListener("click", function() {
    document.getElementById("nav-menu").classList.remove("open");
    document.getElementById("hamburger").classList.remove("hide");
    document.getElementById("close-menu").style.display = "none";
});
