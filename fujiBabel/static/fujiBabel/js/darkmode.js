$(document).ready(() => {
    // toggle darkmode
    $("#toogleButton:checkbox").change(function (e) { 
        e.preventDefault();
        if($("#toogleButton").is(":checked")){
            $("html").addClass("dark");
        }else{
            $("html").removeClass("dark");
        }
    });
});