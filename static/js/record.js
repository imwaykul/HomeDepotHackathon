$(document).ready(function() {

    console.log("Page Loaded!");
    startPic();

    $("#stopButton").click(function() {
        snap();
    });

    $("#redoButton").click(function() {
        startPic();
    });

    $("#uploadButton").click(function() {
        upload();
    });

    function startPic() {
        Webcam.set({
            id : "who",
            width: 550,
            height: 350,
            image_format: 'jpeg',
            jpeg_quality: 100
        });
        $('#myPicture').innerHTML = '';
        Webcam.attach('#myPicture');
    }

    function snap() {
        console.log("Snapped!");
        Webcam.snap( function(data_uri) {
            // display results in page
            $("#myPicture")[0].innerHTML = '<img id="res" src="'+data_uri+'"/>';
        });
    }

    function upload() {
        var formData = $('#res')[0].src;
        var sendData = {'data' : formData}
        //send form data via AJAX
        
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: sendData,
            success: function(response){
                document.write(response);
            },
            error: function(error){
                console.log(error);
            }
        });   
    }
})
