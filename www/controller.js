$(document).ready(function () {
    


    // Display speak message
    Element.expose(displaymessage);
    function displaymessage(message){

        $(".siri-messge li:first").text(message);

        $('.siri-message').textillate('start');
    }
});