function postNewCategory(name, description) {
    const new_cat = JSON.stringify({
        name: name.trim(),
        description: description.trim()
    });

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

function postNewMessage(title, body, category_id) {
    const new_message = JSON.stringify({
        title: title.trim(),
        body: body.trim(),
        category_id: category_id
    });

    let jqxhr = $.ajax({
        url: "/category/post",
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

function postNewComment(body, post_id) {
        const new_comment = JSON.stringify({
        body: body.trim(),
        post_id: post_id
    });

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