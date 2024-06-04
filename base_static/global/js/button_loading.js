function startLoading(){
    var button = document.getElementById("loadingButton");
    button.classList.add("loading");

    setTimeout(function(){
        button.classList.remove("loading");
    }, 5000);
}