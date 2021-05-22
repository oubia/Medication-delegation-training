$(function($) {
    $.ajax({
        url: '',
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