const runCKDITOR = () => {
var labels = document.getElementsByTagName('label');
for (var i = 0; i < labels.length; i++) {
if(labels[i].htmlFor == "id_body"){
labels[i].parentNode.removeChild(labels[i]);
}
}
CKEDITOR.replace('body')};

window.onload = runCKDITOR;

