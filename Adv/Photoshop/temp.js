
alert(values[0][2]);
// var pathPsd=prompt("Enter the path of psd","C:\\>>>");
var pathPsd="D:\\MyWorks\\Python\\Adv\\Photoshop\\sample2.psd";
var pathJpg = "D:\\MyWorks\\Python\\Adv\\Photoshop\\";
// var pathJpg = prompt("Enter the path to save JPG","C:\\>>>").replace("\\" , "\\\\");
alert("You said: "+pathPsd);
var psdFile = new File(pathPsd.replace("\\","\\\\"));  

if(psdFile.exists){

    app.open(psdFile);
// prompt([prompt message],[title])
    function textLayrr (layers,values) {
        for (var i = 0, len = layers.length ; i< len; i++) {
            if (layers[i].kind == "LayerKind.TEXT") {
            for ( var j = 0 , leng = values[i].length ; j< leng ; j++){
                
                var nameLayer = textLayers[i];
                var newTexts = values[i][j];
                alert(nameLayer ," " , newTexts);
                app.activeDocument.layer = activeDocument.artLayers.getByName(nameLayer);

                if(app.activeDocument.layer.visible == true){
                    app.activeDocument.layer.textItem.contents= newTexts;
                    var saveName = newTexts + ".jpg";
                    var jpgOptn = new JPEGSaveOptions()
                    jpgOptn.quality = 12  // Max quality number
                    pathJpg+= saveName
                    app.activeDocument.saveAs(new File(pathJpg), jpgOptn,true);
                }
                }
            }
        }
    }
    textLayrr(app.activeDocument.artLayers,values);
    // alert(textLayers)
    // var jpgOptn = new JPEGSaveOptions()
    // jpgOptn.quality = 12  // Max quality number
    
    
    // pathJpg+= saveName
    // app.activeDocument.saveAs(new File(pathJpg), jpgOptn,true);
    // alert(pathJpg)
    // app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);  // SAVECHANGES to save file
}
else{
    alert("Give full path");
}
