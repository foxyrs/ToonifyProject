
$(document).ready(function () {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    let getUrl = window.location;
    let baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
    let baseUrl2 = getUrl .protocol + "//" + getUrl.host;

    $('#sendToonifyForm').on('click', function(){
        let data = [];
        let element = $(this);
        let span = element.children('span');
        element.prop('disabled', true);
        span.removeAttr('hidden');

        data['element'] = element;
        data['span'] = span;
        data['url'] = baseUrl + "/api/toonify";
        readURL (document.getElementById("imageInput"), data);
    });

    let readURL = function (input, data) {
        if (input.files && input.files[0]) {
            let reader = new FileReader();

            reader.readAsDataURL(input.files[0]);

            let fd = new FormData();
            let files = input.files;

            let url = data['url'];

            console.log(files[0]);

            fd.append('image', files[0]);
            $.ajax({
                type: 'post',
                headers: {'X-CSRFToken': csrftoken},
                mode: 'same-origin',
                url: url,
                data: fd,
                processData: false,
                contentType: false,
                success: function (response) {
                    console.log(response);
                    input.value = "";
                    let linkHTML = '<div class="row"><img style="max-width: 300px" src="'+baseUrl2+response+'" alt="result"></div><div class="row"><a download="" href="'+baseUrl2+response+'" target="_blank">Download</a></div>';
                    $("#toonifiedImgContainer").html(linkHTML);
                    if(data['element'] !== undefined) data['element'].prop('disabled', false);
                    if(data['span'] !== undefined) data['span'].attr('hidden','hidden');
                },
            });

        } else {
            console.log("no file selected");
            $("#toonifyForm")[0].reportValidity();
            if(data['element'] !== undefined) data['element'].prop('disabled', false);
            if(data['span'] !== undefined) data['span'].attr('hidden','hidden');
        }
        
    }
});
