function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



const ajaxLike = (postID,type) =>{
    const form = $(`#post${postID}`)
    let post= postID.replace('/[^\d]/gi','')
    const handleSuccess = data =>{
        const likeCount = $(`#like-count${postID}`)
        const button = $(`#button${postID}`)
        const prevVal = parseInt(likeCount.text())
        likeCount.text(data.likes)
        if (prevVal < data.likes){
            button.removeClass().addClass("btn btn-danger")
            button.html('Unlike')
        }else{
            button.removeClass().addClass("btn btn-success")
            button.html('Like')
 
        }
        
    }
    token = $('input[name=csrfmiddlewaretoken]').val()
    console.log('token',token);
    $.ajax({
        type: "POST",
        url: `http://localhost:8000/like/${post}/`,
        data: form.serialize(),
        dataType:'json',
        headers: { "X-CSRFToken": token },
        success: data=>handleSuccess(data)
      });
}