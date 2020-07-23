$(document).ready(function() {
    // a custom character countdown for the message input field
    const maxMessage = 500,
        message = $('#id_message');

    $('#message-counter').text(`${maxMessage - message.val().length} characters left`);

    message.keyup(function () {
        $('#message-counter').text(`${maxMessage - message.val().length} characters left`);
    });
  });