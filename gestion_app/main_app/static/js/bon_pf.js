$(document).ready(function() {
    $('.attendencecheckbox').click(function() {
        var txt = "";
        $('.attendencecheckbox:checked').each(function() {
            txt += $(this).val() + ","
        });
        $('#attendencevalueinput').val(txt);
    });
})