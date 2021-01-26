class PostEditor{

    constructor(textarea_element_id, slug){
        this.slug = slug
        this.editor = new Quill(textarea_element_id, {
            modules: { 
                toolbar: [
                    ['bold', 'italic'],
                    ['link', 'blockquote', 'code-block', 'image'],
                    [{ list: 'ordered' }, { list: 'bullet' }]
                  ],
                  clipboard: {
                    matchVisual: false
                }
             },
            placeholder: 'Type here',
            theme: 'snow'
        });
        this.title = "";
        this.content = "";
        this.textarea_element_id = textarea_element_id;
        new FileUploader(this.editor);
        this.onLoadMakeVisible();
        this.onTitleInputScroll();
        this.moveTexteditorToQuill();
        
    };
    getCookie(name) {
        if (!document.cookie) {
          return null;
        }
    
        const xsrfCookies = document.cookie.split(';')
          .map(c => c.trim())
          .filter(c => c.startsWith(name + '='));
    
        if (xsrfCookies.length === 0) {
          return null;
        }
        return decodeURIComponent(xsrfCookies[0].split('=')[1]);
      }
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

    syncpost(){
        var titleField = document.getElementById("title-div");
        const fd = new FormData();
        var titleVal =titleField.innerHTML;
        var contentVal =  this.editor.root.innerHTML;
        if(titleVal==this.title && (contentVal == this.content || this.isQuillEmpty())){
            return ;
        }
        fd.append('title', titleVal);
        fd.append('content', contentVal);
        const csrfToken = this.getCookie('csrftoken');
        fd.append('csrfmiddlewaretoken', csrfToken);  
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/edit/'+this.slug, true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.send(fd);
        this.title = titleField.innerHTML;
        this.content = this.editor.root.innerHTML;
    }
    moveTexteditorToQuill(){
        var quill = this.editor;
        var titleEditor = document.getElementById("title-div");
        titleEditor.addEventListener("keydown",function(e){
            var code = (e.keyCode ? e.keyCode : e.which);
            if(code == 13 || code==9) { //Enter keycode
                e.stopPropagation();
                e.preventDefault();
                quill.focus();
            }
        });
    }
    isQuillEmpty() {
        return this.editor.getText().trim().length === 0 && this.editor.container.firstChild.innerHTML.includes("img") === false;
    }
};

