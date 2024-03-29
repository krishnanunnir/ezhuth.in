const likePost = async (element, slug) => {
    url = "/like/"+slug;
    var likes_number=document.getElementById(element +'-number');
    var value = parseInt(likes_number.innerHTML, 10);
    var likes_heart = document.getElementById(element);
    value = isNaN(value) ? 0 : value;
    let req = await fetchPage(url);
    status = await req.text();
    if(status.match("false")){
        likes_heart.src="/static/images/heart.svg";
        value--;
        likes_number.innerHTML = value;
    }else{
        likes_heart.src="/static/images/liked_heart.svg";
        value++;
        likes_number.innerHTML = value;
    }

}

const likeComment = async (element, id) => {
    url = "/like/comment/"+id;
    var likes_number=document.getElementById(element +'-number');
    var value = parseInt(likes_number.innerHTML, 10);
    var likes_heart = document.getElementById(element);
    value = isNaN(value) ? 0 : value;
    let req = await fetchPage(url);
    status = await req.text();
    if(status.match("false")){
        likes_heart.src="/static/images/heart.svg";
        value--;
        likes_number.innerHTML = value;
    }else{
        likes_heart.src="/static/images/liked_heart.svg";
        value++;
        likes_number.innerHTML = value;
    }

}
