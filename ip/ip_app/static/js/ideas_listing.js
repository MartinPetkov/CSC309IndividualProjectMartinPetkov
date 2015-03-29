function csrfSafeMethod(method) {
    return(/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$(document).ready(function() {
    // Get the csrf token for the AJAX call later
    var csrftoken = $.cookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if(!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // Code for Like button
    $('.like-button').click(function() {
        var idea_id;
        idea_id = $(this).attr("idea-id");
        this_idea_img = $(this).find("img");
        $.post('/ip_app/likeIdea/', {'idea_id': idea_id}, function(data) {
            var new_src;
            if(data == 1) {
                new_src = "/static/images/like-like.png";
            } else {
                new_src = "/static/images/neutral-like.png";
            }

            this_idea_img.attr("src", new_src);
        });
    });
});
