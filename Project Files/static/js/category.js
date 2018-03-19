/*
* The AJAX requests for each route in order of declaration
* /category
* /category/thread
* /category/thread/add_comment
* /category/thread/vote
* /category/thread/comment/vote
*/
function postNewCategory(name, description) {
    const new_cat = JSON.stringify({
        name: name.trim(),
        description: description.trim()
    });

    console.log(new_cat);

    let jqxhr = $.ajax({
            url: "/category",
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

                    clearModalInputs("#modalNewCategory", ['#txtCategoryName', '#txtDescription']);

                    swal({
                        type: 'success',
                        title: 'Awesome!',
                        text: 'Your new category was created',
                        footer: "<a href='/catgeory?category_id=?'>Click here to go to this category</a>",
                      });

                    break;
                case 403:
                    console.log("Category name is taken");

                    $("#modalNewCategory").modal('show');

                    swal({
                        type: 'error',
                        title: 'Oh no!',
                        text: 'That catgeory already exists.',
                      });

                    break;
                case 405:
                    console.log("Try connecting to Flask first. Or someone didn't add the POST method to this route");

                    $("#modalNewCategory").modal('show');

                    swal({
                        type: 'error',
                        title: 'Oops...',
                        text: 'Something went wrong. Try submitting the request again',
                      });

                    break;
                case 500: 
                    console.log("Backend team broke something");

                    $("#modalNewCategory").modal('show');
                    
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

function postNewThread(title, body, category_id) {
    const new_thread = JSON.stringify({
        title: title.trim(),
        body: body.trim(),
        category_id: parseInt(category_id)
    });

    let jqxhr = $.ajax({
        url: "/category/thread",
        type: "POST",
        contentType: "applcation/json; charset=utf-8",
        dataType: "applcation/json; charset=utf-8",
        cache: false,
        data: new_thread  
    })

    .always(function (data, textStatus) {
        if (textStatus !== 'success') {
            console.log(textStatus);
        }
        
        //switch on the HTTP status code
        switch (jqxhr.status) {
            case 200:
                console.log("All good");

                clearModalInputs("#modalNewThread", ['#txtTitle', '#txtBody']);

                swal({
                    type: 'success',
                    title: 'Awesome!',
                    text: 'Your new thread was created',
                    footer: "<a href='/catgeory/thread?thread_id=?'>Click here to go to this thread</a>",
                  });

                break;
            case 403:
                console.log("Insert of thread failed");

                $("#modalNewthread").modal('show');

                swal({
                    type: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong. Try submitting the request again',
                  });

                break;
            case 405:
                console.log("Try connecting to Flask first. Or someone didn't add the POST method to this route");
                
                $("#modalNewThread").modal('show');

                swal({
                    type: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong. Try submitting the request again',
                  });

                break;
            case 500: 
                console.log("Backend team broke something");

                $("#modalNewThread").modal('show');

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

function postNewComment(body, thread_id) {
    const new_comment = JSON.stringify({
        body: body.trim(),
        thread_id: parseInt(thread_id)
    });


    let jqxhr = $.ajax({
        url: "/category/thread/add_comment",
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

                clearModalInputs("#modalNewComment", ['#txtBody']);

                swal({
                    type: 'success',
                    title: 'Awesome!',
                    text: 'Your new comment was created'
                  });

                break;
            case 403:
                console.log("Comment post failed");

                $("#modalNewComment").modal('show');

                swal({
                    type: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong. Try submitting the request again',
                  });


                break;
            case 405:
                console.log("Try connecting to Flask first. Or someone didn't add the POST method to this route");

                $("#modalNewComment").modal('show');

                swal({
                    type: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong. Try submitting the request again',
                  });

                break;
            case 500: 
                console.log("Backend team broke something");

                $("#modalNewComment").modal('show');

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

function modidyThreadVote(thread_id, vote) {
    const new_vote = JSON.stringify({
        thread_id: parseInt(thread_id),
        vote: parseInt(vote)
    });

    console.log(new_vote);

    let jqxhr = $.ajax({
        url: "/category/thread/vote",
        type: "POST",
        contentType: "applcation/json; charset=utf-8",
        dataType: "applcation/json; charset=utf-8",
        cache: false,
        data: new_vote     
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

function modifyCommentVote(thread_id, comment_id, vote) {
    const new_vote = JSON.stringify({
        thread_id: parseInt(thread_id),
        comment_id: parseInt(comment_id),
        vote: parseInt(vote)
    });

    console.log(new_vote);
    
    let jqxhr = $.ajax({
        url: "/category/thread/comment/vote",
        type: "POST",
        contentType: "applcation/json; charset=utf-8",
        dataType: "applcation/json; charset=utf-8",
        cache: false,
        data: new_vote     
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

function setupDataTable(table_id) {
    $("#" + table_id).DataTable ({
        scrollY: '50vh',
        scrollCollapse: true
    });
}

function setupVoteListeners(base_class, type) {
    const up_class = '.' + base_class + '-up';
    const down_class = '.' + base_class + '-down';

    $(up_class).on('click touch', function() {
        const other_id = this.id.replace("Up", "Down").trim();
        $(this).removeClass('animated-not-clicked');
        $(this).toggleClass('animated-clicked');
        document.getElementById(other_id).classList.add('animated-not-clicked');
        document.getElementById(other_id).classList.remove('animated-clicked');
        
        if(type === 'thread') {
            modifyThreadVote(this.id.replace(/\D/g,'').trim(), 1);
        }
        else if(type === 'comment') {
            modifyCommentVote(getQueryStringValue('thread_id'), this.id.replace(/\D/g,'').trim(), 1);
        }
    });

    $(down_class).on('click touch', function() {
        const other_id = this.id.replace("Down", "Up").trim();
        $(this).removeClass('animated-not-clicked');
        $(this).toggleClass('animated-clicked');
        document.getElementById(other_id).classList.add('animated-not-clicked');
        document.getElementById(other_id).classList.remove('animated-clicked');

        if(type === 'thread') {
            modifyThreadVote(this.id.replace(/\D/g,'').trim(), -1);
        }
        else if(type === 'comment') {
            modifyCommentVote(getQueryStringValue('thread_id'), this.id.replace(/\D/g,'').trim(), -1);
        }
    });
}

function clearModalInputs(modal, inputs) {
    $(modal).modal('hide');

    inputs.forEach(function(e) {
        $(e).val('');
        $(e).removeClass("is-valid");
        $(e).removeClass("is-invalid");
        console.log($(e));
    });
}
