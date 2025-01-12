let addButton = document.getElementById("add");
let configDiv = document.getElementById("configurations");
let removeButton = document.getElementById("remove");

removeButton.addEventListener("click", function() {

    if (configDiv.children.length > 3) {
        configDiv.removeChild(configDiv.lastChild);
        configDiv.removeChild(configDiv.lastChild);
        configDiv.removeChild(configDiv.lastChild);
    }
});

addButton.addEventListener("click", function() {
    let newExtension = document.createElement("input");
    let newFolder = document.createElement("input");
    let br = document.createElement("br");

    configDiv.appendChild(br);

    newExtension.setAttribute("type","text");
    newFolder.setAttribute("type","text");

    newExtension.id = "ext"
    newFolder.id = "folder"

    newFolder.style = "margin-left: 4px;";

    

    configDiv.appendChild(newExtension);
    configDiv.appendChild(newFolder);
});