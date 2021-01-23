class PostEditor{

    constructor(textarea_element_id, toolbar_element_id){
        this.editor = new Quill(textarea_element_id, {
            modules: { 
                toolbar: [
                    ['bold', 'italic'],
                    ['link', 'blockquote', 'code-block', 'image'],
                    [{ list: 'ordered' }, { list: 'bullet' }]
                  ]
             },
            placeholder: 'Type here',
            theme: 'snow'
        });
        this.textarea_element_id = textarea_element_id;
        this.toolbar_element_id = toolbar_element_id;
        new FileUploader(this.editor);
        this.onLoadMakeVisible();
        this.onTitleInputScroll();
        this.moveTexteditorToQuill();
        
    };

    onLoadMakeVisible(){
        var postdiv = document.getElementById("postform-wrapper");
        postdiv.style.display ="block";
    }
    onTitleInputScroll() {
        const tx = document.getElementById('id_title');
        tx.addEventListener("input", function(){
            this.style.height = (this.scrollHeight) + 'px';
        }, false);
    }
    moveTexteditorToQuill(){
        var quill = this.editor;
        var titleEditor = document.getElementById("title-div");
        titleEditor.addEventListener("keydown",function(e){
            var code = (e.keyCode ? e.keyCode : e.which);
            if(code == 13) { //Enter keycode
                e.stopPropagation();
                e.preventDefault();
                quill.focus();
            }
        });
    }
};
document.addEventListener("DOMContentLoaded", () => {
    invokeAction = new PostEditor("#editor","#toolbar");
    form = document.querySelector('form');
    var quill = invokeAction.editor;
    var inputContentField = document.getElementById("id_content");
    var inputTitleField = document.getElementById("id_title");
    var titleField = document.getElementById("title-div");
    if(inputContentField.value!= "" && inputTitleField.value!=""){
        quill.root.innerHTML = inputContentField.value;
        titleField.innerHTML = inputTitleField.value;
        titleField.removeAttribute("contenteditable");
        quill.focus();
    }
    form.onsubmit = function() {
        inputContentField.value = quill.root.innerHTML;
        inputTitleField.value = titleField.innerHTML;
    }
});

