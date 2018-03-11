/*
* The AJAX requests for each route in order of declaration
* /category
* /category/post
* /category/post/add_comment
* /category/post/vote
* /category/post/comment/vote
*/
function postNewCategory(name, description) {
    const new_cat = JSON.stringify({
        name: name.trim(),
        description: description.trim()
    });

    console.log(new_cat);

    let jqxhr = $.ajax({
            url: "/categories",
            type: "POST",
            contentType: "applcation/json; charset=utf-8",
            dataType: "applcation/json; charset=utf-8",
            cache: false,
            data: new_cat     
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
                        text: 'Your new category was created',
                        footer: "<a href='/catgeory?category_id=?'>Click here to go to this category</a>",
                      });

                    break;
                case 403:
                    console.log("Category name is taken");

                    swal({
                        type: 'error',
                        title: 'Oh no!',
                        text: 'That catgeory already exists.',
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

function postNewPost(title, body, category_id) {
    const new_post = JSON.stringify({
        title: title.trim(),
        body: body.trim(),
        category_id: parseInt(category_id)
    });

    console.log(new_post);

    let jqxhr = $.ajax({
        url: "/category/post",
        type: "POST",
        contentType: "applcation/json; charset=utf-8",
        dataType: "applcation/json; charset=utf-8",
        cache: false,
        data: new_post    
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
                    text: 'Your new post was created',
                    footer: "<a href='/catgeory/post?post_id=?'>Click here to go to this post</a>",
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

function postNewComment(body, post_id) {
        const new_comment = JSON.stringify({
        body: body.trim(),
        post_id: parseInt(post_id)
    });

    console.log(new_comment);

    let jqxhr = $.ajax({
        url: "/category/post/add_comment",
        type: "POST",
        contentType: "applcation/json; charset=utf-8",
        dataType: "applcation/json; charset=utf-8",
        cache: false,
        data: new_comment     
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
                    text: 'Your new comment was created'
                  });

                break;
            case 403:
                console.log("Comment post failed");

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

function modifyPostVote(post_id, vote) {
    const new_vote = JSON.stringify({
        post_id: post_id,
        vote: vote
    });

    let jqxhr = $.ajax({
        url: "/category/post/vote",
        type: "POST",
        contentType: "applcation/json; charset=utf-8",
        dataType: "applcation/json; charset=utf-8",
        cache: false,
        data: new_comment     
    })

    .always(function (data, textStatus) {
        if (textStatus !== 'success') {
            console.log(textStatus);
        }
        
        //switch on the HTTP status code
        switch (jqxhr.status) {
            case 200:
                console.log("All good");
                break;
            case 403:
                console.log("Category name is taken");
                break;
            case 405:
                console.log("Try connecting to Flask first. Or someone didn't add the POST method to this route");
                break;
            case 500: 
                console.log("Backend team broke something");
                break;
            default:
                //probably won't need this in production, but here's where we get the response (undefined if error)
                console.log(data.responseJSON);
                break;
        }   
    });
}

function modifyCommentVote(post_id, comment_id, vote) {
    const new_vote = JSON.stringify({
        post_id: post_id,
        comment_id: comment_id,
        vote: vote
    });

    let jqxhr = $.ajax({
        url: "/category/post/comment/vote",
        type: "POST",
        contentType: "applcation/json; charset=utf-8",
        dataType: "applcation/json; charset=utf-8",
        cache: false,
        data: new_comment     
    })

    .always(function (data, textStatus) {
        if (textStatus !== 'success') {
            console.log(textStatus);
        }
        
        //switch on the HTTP status code
        switch (jqxhr.status) {
            case 200:
                console.log("All good");
                break;
            case 403:
                console.log("Category name is taken");
                break;
            case 405:
                console.log("Try connecting to Flask first. Or someone didn't add the POST method to this route");
                break;
            case 500: 
                console.log("Backend team broke something");
                break;
            default:
                //probably won't need this in production, but here's where we get the response (undefined if error)
                console.log(data.responseJSON);
                break;
        }   
    });
}

/*
* Helper functions used by the AJAX requests
*/
function getQueryStringValue(key) {  
    return decodeURIComponent(window.location.search.replace(new RegExp("^(?:.*[&\\?]" + encodeURIComponent(key).replace(/[\.\+\*]/g, "\\$&") + "(?:\\=([^&]*))?)?.*$", "i"), "$1"));  
}