function createComments(){
    $.ajax({
        url : 'http://localhost:9000/api/comments/',
        method: 'post',
        headers : {"Authorization" : "Token bc4ac83cfbaae30c5ae1e99f3c8a451aa37d087a"},
        data: JSON.stringify({text: "Test", photography: uploads/photo/FullSizeRender.jpg,
        comments_author: 1}),
        contentType:"application/json",
        dataType : "json",
        success:function(response, status) {console.log(response);},
        error: function(response, status) {console.log(response);}
    });
}



$(document).ready(function() {

});