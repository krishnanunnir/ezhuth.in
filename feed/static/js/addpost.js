class PostEditor{

    constructor(textarea_element_id, toolbar_element_id){
        this.editor = new Quill(textarea_element_id, {
            modules: { toolbar: toolbar_element_id },
            theme: 'snow'
        });
        this.textarea_element_id = textarea_element_id;
        this.toolbar_element_id = toolbar_element_id;
        new FileUploader(this.editor);
        this.onLoadMakeVisible();
        this.onTitleInputScroll();
        this.moveTexteditorToQuill();
        this.eventListenerTitleFocus();
        
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
        var titleEditor = document.getElementById("id_title");
        titleEditor.addEventListener("keydown",function(e){
            var code = (e.keyCode ? e.keyCode : e.which);
            if(code == 13) { //Enter keycode
                e.stopPropagation();
                e.preventDefault();
                quill.focus();
            }
        });
    }
    eventListenerTitleFocus(){
        var quill = this.editor;
        var toolbar = document.getElementById("toolbar-wrapper");
        quill.root.addEventListener('focusin', ()=>{
            toolbar.style.visibility = "visible";
        });
        quill.root.addEventListener('focusout', ()=>{
            toolbar.style.visibility = "hidden";
        });
    }
};
document.addEventListener("DOMContentLoaded", () => {
    invokeAction = new PostEditor("#editor","#toolbar");
    form = document.querySelector('form');
    var quill = invokeAction.editor;
    var inputField = document.getElementById("id_content");
    if(inputField.value!= null){
        quill.root.innerHTML = inputField.value;
    }
    form.onsubmit = function() {
        inputField.value = quill.root.innerHTML;
    }
});

