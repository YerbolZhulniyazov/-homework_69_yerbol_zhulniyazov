$(document).ready(function () {
    $('button').click(function () {
        let $button = $(this);
        let action = $button.data('action');
        $.ajax({
            type: 'POST',
            url: '/' + action + '/',
            data: JSON.stringify({
                'A': $('#A').val(),
                'B': $('#B').val(),
            }),
            success: function (response) {
                $('#result').text(response.answer).css('color', 'green');
            },
            error: function (response) {
                $('#result').text(response.responseJSON.error).css('color', 'red');
            }
        });
    });
});