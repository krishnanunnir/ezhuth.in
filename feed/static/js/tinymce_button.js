function tinymce_js(editor){
    editor.ui.registry.addButton('submit', {
        text: 'Submit Post',
        onAction: function () {
          var x = document.getElementById("publish-button");
          x.click();
        }
      });
}