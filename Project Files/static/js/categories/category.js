function postNewCategory(name, description) {
    //set 
    const newCat = JSON.stringify({
        name: name.trim(),
        description: description.trim()
    });

    let jqxhr = $.ajax({
            url: "/categories",
            type: "POST",
            contentType: "applcation/json; charset=utf-8",
            dataType: "applcation/json; charset=utf-8",
            cache: false,
            data: newCat     
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