var myDropzone = new window.Dropzone('div#update', {url: "/"});

// dropCOntainer.ondraggover = dropCOntainer.ondragenter = function(e){
//     e.preventDefault();
// };

// dropCOntainer.ondrop = function(e){
//     fileInput.files = e.dataTransfer.files;
//     const dt = new DataTransfer();

//     dt.items.add(e.e.dataTransfer.files[0]);
//     dt.items.add(e.e.dataTransfer.files[3]);
//     fileInput.files = dt.files;

//     e.preventDefault();
// }