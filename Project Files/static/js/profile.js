function editProfile(name, email, bio) {
    const profile_info = JSON.stringify({
        name: name.trim(),
        email: email.trim(),
        bio: bio.trim()
    });

    console.log(profile_info);

    let jqxhr = $.ajax({
        url: "/profile",
        type: "POST",
        contentType: "application/json; charset=utf-8",
        dataType: "application/json; charset=utf-8",
        cache: false,
        data: profile_info
    })

    .always(function (data, textStatus) {
        if (textStatus !== 'success') {
            console.log(textStatus);
        }

        //switch on the HTTP status code
        switch (jqxhr.status) {
            case 200:
                console.log("All good");

                $('#name').html(name);
                $('#email').html(email);
                $('#bio').html(bio);

                swal({
                    type: 'success',
                    title: 'Awesome!',
                    text: 'Your profile was updated',
                  });

                break;
            case 403:
                console.log("Profile update failed");

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

function postNewMessage(user, body) {
    const new_message = JSON.stringify({
        user: user.trim(),
        body: body.trim(),
    });

    console.log(new_message);

    let jqxhr = $.ajax({
        url: "/profile/messages",
        type: "POST",
        contentType: "application/json; charset=utf-8",
        dataType: "application/json; charset=utf-8",
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
                console.log("Sending message failed");

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

function removeFriend(user) {
    const remove_friend = JSON.stringify({
        user2_id: user.trim()
    });

    console.log(remove_friend);

    let jqxhr = $.ajax({
        url: "/profile/friends",
        type: "DELETE",
        contentType: "application/json; charset=utf-8",
        dataType: "application/json; charset=utf-8",
        cache: false,
        data: remove_friend
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
                    title: 'Removed',
                    text: 'Friend successfully removed',
                  });

                break;
            case 403:
                console.log("Removing friend failed");

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

function addFriend(user) {
    const remove_friend = JSON.stringify({
        user2_id: user.trim()
    });

    console.log(remove_friend);

    let jqxhr = $.ajax({
        url: "/profile/friends",
        type: "POST",
        contentType: "application/json; charset=utf-8",
        dataType: "application/json; charset=utf-8",
        cache: false,
        data: remove_friend
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
                    text: 'Friend successfully added',
                  });

                break;
            case 403:
                console.log("Adding friend failed");

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

function acceptRequest(user) {
    const request = JSON.stringify({
        user1_id: user.trim()
    });

    console.log(request);

    let jqxhr = $.ajax({
        url: "/profile/friends/requests",
        type: "POST",
        contentType: "application/json; charset=utf-8",
        dataType: "application/json; charset=utf-8",
        cache: false,
        data: request
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
                    text: 'Friend request accepted',
                  });

                break;
            case 403:
                console.log("Adding friend failed");

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
