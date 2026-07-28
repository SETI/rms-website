---
---
const BASEURL = {{ site.baseurl | jsonify }};

(function($){

    window.Feedback={
        init:function(){

            if ($("#feedback-tab").length){
                return;
            }

            $("body").append(
                '<button id="feedback-tab">' +
                    '<p>Questions / Feedback</p>' +
                '</button>'
            );

            $("#feedback-tab").on("click",
                function(e){
                    e.preventDefault();
                    Feedback.open();
                }
            );
        },

        open:function(){
            if (
            $("#feedback-form").length
            ){
                return;
            }

            $.get(`${BASEURL}/feedback/feedback.html`,
                function(html) {
                    $("body").append(html);

                    $("input[name=location]")
                        .val(
                            window.location.href);

                    $(".feedback-close").click(Feedback.close);
                    $("#feedback-modal").click(function(e){
                        e.stopPropagation();
                    });

                    $("#feedback-form").on("submit", Feedback.submit);

            }).fail(function(jqXHR, textStatus, errorThrown) {
                console.error('Failed to load feedback form:', textStatus, errorThrown);
                alert('Unable to load feedback form. Please try again later.');
            });
         },


        close:function(e){
            if(e){
                e.preventDefault();
            }

            $("#feedback-modal")
                .remove();
        },

        submit:async function(event) {
            event.preventDefault();

            const submittedForm = event.currentTarget;
            const formData = new FormData($(submittedForm)[0]);
            const encodedBody = new URLSearchParams(formData).toString();

            try {
                const response = await fetch(submittedForm.action, {
                    method: 'POST',
                    credentials: 'omit',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                    },
                    body: encodedBody
                });

                const text = await response.text();

                if (!response.ok) {
                    throw new Error(text || `Server responded with status: ${response.status}`);
                }

                $(".feedback-content").text(
                    'Thank you for making the RMS Node a better site.' +
                    'If you provided an email address, ' +
                    'a representative will get back to you ' +
                    'as soon as possible.'
                );

            } catch (error) {
                console.error('Submission failed:', error.message);
                $(".feedback-error").remove();

                $(".feedback-body").prepend(
                    '<div class="feedback-error">' +
                            (error.message || 'Unable to send feedback.') +
                    '</div>'
                );
            }
        }
    };

    $(function () {
        Feedback.init();
    });

})(jQuery);