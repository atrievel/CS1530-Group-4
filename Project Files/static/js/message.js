function postNewMessage(user, body) {
    const new_message = JSON.stringify({
        title: title.trim(),
        body: body.trim(),
    });

    console.log(new_message);

    let jqxhr = $.ajax({
        url: "/messages/post",
        type: "POST",
        contentType: "applcation/json; charset=utf-8",
        dataType: "applcation/json; charset=utf-8",
        cache: false,
        data: new_message
    })

    .always(function (data, textStatus) {
        if (textStatus !== 'success') {
            console.log(textStatus);
        }

        //switch on the HTTP status code
        switch (jqxhr.status) {
            case 200:
                console.log("All good");

                swal({
                    type: 'success',
                    title: 'Awesome!',
                    text: 'Your message was sent',
                  });

                break;
            case 403:
                console.log("Insert of post failed");

                swal({
                    type: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong. Try submitting the request again',
                  });

                break;
            case 405:
                console.log("Try connecting to Flask first. Or someone didn't add the POST method to this route");

                swal({
                    type: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong. Try submitting the request again',
                  });

                break;
            case 500:
                console.log("Backend team broke something");

                swal({
                    type: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong. Try submitting the request again',
                  });

                break;
            default:
                //probably won't need this in production, but here's where we get the response (undefined if error)
                console.log(data.responseJSON);
                break;
        }
    });
}
