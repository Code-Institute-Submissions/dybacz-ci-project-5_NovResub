let image = document.querySelector('#new_image')
let filename = document.querySelector('#filename')

image.onchange = function () {
    let file = this.files[0];
    filename.innerHTML = `Image will be set to ${file.name}`;
};