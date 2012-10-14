/* Author: Doers' Guild */

function initScrollSpy() {
    $("#mainNav").scrollspy();
    $('[data-spy="scroll"]').each(function() {
        $(this).scrollspy('refresh');
    });
}

function scroll2Hash() {
    if (window.location.hash.length > 0) {
        // $(window).scrollTop($(window.location.hash).scrollTop()-25);
        // $('html, body').scrollTop(0);

        $('html, body').animate({
            scrollTop : $(window.location.hash).offset().top - $("#mainNav").height()
        }, 1500);

        // $("[href='"+window.location.hash+"']").parent().addClass("active");
    }
}

function dropDownOnHover() {
    $(".dropdown").each(
    // Activate Dropdown on hover
    function() {
        if ($(this).find(".dropdown-toggle-hidden").length === 0) {
            $(this).append('<a class="dropdown-toggle-hidden" data-toggle="dropdown" data-target="#' + $(this).attr("id") + '" style="padding:0px;display:none;"/>');
        }
        $(this).on("mouseenter", function(e) {
            // $(this).attr("data-hover-fired", "true");
            $(this).find(".dropdown-toggle-hidden").trigger("click");
            // e.preventDefault();
            // return false;
        });
        $(this).on("mouseleave", function(e) {
            $(this).find(".dropdown-toggle-hidden").trigger("click");
            // e.preventDefault();
            // return false;
        });
    });
}

function showPage(page) {
    // Show a particular page-section hiding the rest of them
    if (page && $(page).attr("data-role") === "page") {
        var selected = $(page);
    } else {
        var selected = $(window.location.hash).closest("[data-role='page']");
    }
    if (selected.length > 0) {
        $("[data-role='page']").hide();
        selected.show();
        $("#mainNav").find("li").removeClass("active");
        $("#mainNav").find("a[href='" + window.location.hash + "']").closest("li").addClass("active");
    } else {
        $("[data-role='page']").hide();
        selected = $("[data-role='page']").first();
        selected.show();
        $("#mainNav").find("li").removeClass("active");
        $("#mainNav").find("a[href='#" + selected.attr("id") + "']").closest("li").addClass("active");
        // console.log(selected);
    }
}

/*
 $(document).ready(function() {
 showPage();
 $(window).hashchange(showPage);
 // dropDownOnHover();
 // initScrollSpy();
 // scroll2Hash();
 });

 if ($(window).hashchange)
 $(window).hashchange(showPage);*/