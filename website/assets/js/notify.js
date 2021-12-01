$("#pds-notification-modal").on("click", ".btn", function() {
    let target = $(this).data("target");
    if ($(this).attr("type") == "submit") {
        $.cookie("notify", $(`#${target}`).data("cookie"), {expires: 1000000});
    }
    $(`#${target}`).modal("hide");
});

$( document ).ready(function() {
    $.get( "/news/important_message.txt", function( data, status, xhr ) {
        //console.log( xhr.getResponseHeader("Last-Modified") );
        // if the lastMod stored in the cookie is different than the
        // current last mod of the file, display the message
        let cookie = xhr.getResponseHeader("Last-Modified");
        if ($.cookie("notify") != cookie) {
            //$("#pds-notification-modal .modal-body").html(data);
            //$("#pds-notification-modal").modal("show");
            //$("#pds-notification-modal").data("cookie", cookie);
            $(".notification").html(data);
        }
    })
    .fail(function() {
        // and just null out the cookie if the file is gone...
        $.cookie("notify", null);
    });
});
