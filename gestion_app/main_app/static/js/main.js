$(function($) {
    $.ajax({
        url: 'http://127.0.0.1:8000/livraison/',
        type: 'get',
        data: {
            ready_text: $(this).text()
        },
        success: function(response) {
            var out = "";
            for (var i = 0; i < response.length; i++) {
                out += response[i];
            }
            console.log(out)

        }
    })
})