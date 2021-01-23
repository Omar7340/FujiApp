$(document).ready(function () {
    //menu mobile
    $("#mobile-menu-button").click(function (e) { 
        e.preventDefault();
        if( $("#mobile-menu-button #svg-close").hasClass("block")){
            $("#mobile-menu-button #svg-close").removeClass("block").addClass("hidden");
            $("#mobile-menu-button #svg-open").removeClass("hidden").addClass("block");
            $("#mobile-menu").removeClass("hidden").addClass("block");
        }else{
            $("#mobile-menu-button #svg-close").removeClass("hidden").addClass("block");
            $("#mobile-menu-button #svg-open").removeClass("block").addClass("hidden");
            $("#mobile-menu").removeClass("block").addClass("hidden");
        }
    });
});