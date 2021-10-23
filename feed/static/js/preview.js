document.addEventListener("DOMContentLoaded", () => {
    var imageUpload = document.getElementById("id_header_image");
    var uploadImageDiv=document.getElementById("uploadImageDiv");
    var removePreview=document.getElementById("removeButton");
    var descriptionDiv=document.getElementById("description-div");
    var inputDescription = document.getElementById("id_description");
    imageUpload.onchange = function(e){
        document.getElementById('output').src = window.URL.createObjectURL(this.files[0]);
        uploadImageDiv.style.display="none";
    }
    uploadImageDiv.onclick = function(){
        imageUpload.click();
    }
    removePreview.onclick = function(){
        document.getElementById('output').src ="";
        uploadImageDiv.style.display="block";
        imageUpload.value="";
    }
    form = document.querySelector('form');
    form.onsubmit = function() {
        inputDescription.value = descriptionDiv.innerHTML;
    }
});
