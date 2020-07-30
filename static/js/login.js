(function(fun){
    window.addEventListener("load", fun);
})(function(){
    $("#userCreate").ajaxForm(function(data){
        console.log(data);
        location.href="../";
    });

    $("#login").ajaxForm(function(data){
        console.log(data);
        location.href="../";
    });
});