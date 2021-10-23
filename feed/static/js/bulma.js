document.addEventListener('DOMContentLoaded', () => {
    var textarea = document.querySelector('#id_content');
    textarea.classList.add("textarea");
    var dropdown = document.querySelector('.dropdown');
    dropdown.addEventListener('click', function(event) {
    event.stopPropagation();
    dropdown.classList.toggle('is-active');
    dropdown.classList.toggle('border-option');
    });
    document.addEventListener('click',function(event){
        if(dropdown.classList.contains("is-active")){
            event.stopPropagation();
            dropdown.classList.toggle('is-active');
            dropdown.classList.toggle('border-option');
        }
    });
});
