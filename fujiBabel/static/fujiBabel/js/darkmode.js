$(document).ready(() => {
    // toggle darkmode
    $("#toogleButton:checkbox").change(function (e) { 
        e.preventDefault();
        console.log("test");
        if($("#toogleButton").is(":checked")){
            $("html").addClass("dark");
        }else{
            $("html").removeClass("dark");
        }
    });
});