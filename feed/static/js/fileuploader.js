class FileUploader{

  constructor(editor){
    this.editor = editor;
    this.editor.getModule('toolbar').addHandler('image', () => {
      this.selectLocalImage();
    });
  }
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

  selectLocalImage() {
    const input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.click();

    // Listen upload local image and save to server
    input.onchange = () => {
      const file = input.files[0];

      // file type is only image.
      if (/^image\//.test(file.type)) {
        this.saveToServer(file);
      } else {
        console.warn('You could only upload images.');
      }
    };
  }

  /**
   * Step2. save to server
   *
   * @param {File} file
   */
  saveToServer(file) {
    const fd = new FormData();
    fd.append('image', file);
    const csrfToken = this.getCookie('csrftoken');
    fd.append('csrfmiddlewaretoken', csrfToken);

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/uploadfile/', true);

    xhr.onload = () => {
      if (xhr.status === 200) {
        // this is callback data: url
        const json = JSON.parse(xhr.responseText);
        this.insertToEditor(json.location);
      }
    };
    xhr.send(fd);
  }

  /**
   * Step3. insert image url to rich editor.
   *
   * @param {string} url
   */
  insertToEditor(url) {
    // push image url to rich editor.
    const range = this.editor.getSelection();
    this.editor.insertEmbed(range.index, 'image', `${url}`);
  }
}
