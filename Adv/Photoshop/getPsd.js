
var textLayers = [];

var pathPsd=prompt("Enter the path","C:\\>>>");

alert("You said: "+pathPsd);
var psdFile = new File(pathPsd.replace("\\","\\\\"));  

if(psdFile.exists){

    app.open(psdFile);
// prompt([prompt message],[title])
    function textLayrr (layers) {
        for (var i = 0, len = layers.length; i < len; i++) {
            if (layers[i].kind == "LayerKind.TEXT") {
                var nameLayer = layers[i].name;

                textLayers.push(layers[i].name);

                app.activeDocument.layer = activeDocument.artLayers.getByName(nameLayer);

                if(app.activeDocument.layer.visible == true){
                    app.activeDocument.layer.textItem.contents= "World " + i.toString();
                }
            }
        }
    }
    textLayrr(app.activeDocument.artLayers);
    alert(textLayers)
    var jpgOptn = new JPEGSaveOptions()
    jpgOptn.quality = 12  // Max quality number
    var saveName = psdFile.name.split(".")[0] + ".jpg";
    var pathJpg = prompt("Enter the path to save JPG","C:\\>>>").replace("\\" , "\\\\");
    pathJpg+= saveName
    app.activeDocument.saveAs(new File(pathJpg), jpgOptn,true);
    alert(pathJpg)
    // app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);  // SAVECHANGES to save file
}
else{
    alert("Give full path");
}









