$(document).ready(function() {
    
    // Set the token so that we are not rejected by server
    var csrf_token = $('meta[name=csrf-token]').attr('content');
    // Configure ajaxSetup so that the CSRF token is added to the header of every request
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });
    

    $("#open-pack-btn").on("click", function() {
        var packId = $(this).data('pack-id');
        console.log("Opening pack with id: " + packId);
        $.ajax({
            url: '/open_pack_response',
            type: 'POST',
            data: JSON.stringify({ 'packId': packId }),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response) {
                $('.big-card').remove();
                var gifElement = $('<img>', {
                    id: 'loading-gif',
                    src: '/static/images/explosion.gif', // Replace with your actual GIF path
                    alt: 'Loading...',
                });
                
                $('body').append(gifElement);
            
                // Show the GIF
                function showGif() {
                    $('#loading-gif').show();
                }
            
                // Hide the GIF
                function hideGif() {
                    $('#loading-gif').hide();
                }
                showGif();
                setTimeout(hideGif, 1500);
                
            // Update the html rendered to reflect the opened pack items
                var resultsContainer = $('#pack-results');
                response.forEach(item => {
                    resultsContainer.append(`
                    <div class="${item.rarity_class}">
                        <div class="card-body-medium">
                        <h5 class="card-title">${item.name}</h5>
                        <img src="${item.image_url}" class="card-img" />
                        <p class="card-text">Rarity: ${item.rarity}</p>
                        <p class="card-text">Genre: ${item.genre}</p>
                        </div>
                    </div>`
                    );
                });
            },
            error: function(error) {
            console.log(error);
            }
        });
    });
});