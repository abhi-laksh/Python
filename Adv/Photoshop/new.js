var textLayers = ['student_name', 'course', 'start_date', 'end_date'];
	var values =  [['Ram Lakshman', 'Ramesh Suresh', 'Sita Gita', 'Sunny Bunny'], ['Website Designing', 'Php Development', 'Python', 'Machine Learning'], ['21 February 2017', '01 December 2017', '24 November 2017', '01 June 2018'], ['24 November 2017', '01 February 2018', '22 April 2018', '05 September 2018']];
	var pathPsd="D:\\MyWorks\\Python\\Adv\\Photoshop\\sample2.psd";
	var pathJpg = "D:\\MyWorks\\Python\\Adv\\Photoshop\\";

	var psdFile = new File(pathPsd.replace("\\","\\\\"));  
	var saveName = "";
	if(psdFile.exists){

	    app.open(psdFile);
	// prompt([prompt message],[title])
	    function textLayrr (layers,changes) {

	      for (i = 0 ; i< textLayers.length ; i++){
	      	
			for (j=0 ; j< values.length ; j++){

				layerName = textLayers[j];
				val = values[j][i];

				app.activeDocument.layer = activeDocument.artLayers.getByName(layerName);
	                if(app.activeDocument.layer.visible == true){
	                    app.activeDocument.layer.textItem.contents= val;
	                    
	                }
			}
			saveName = changes[0][i] + ".jpg";
	        var jpgOptn = new JPEGSaveOptions();
	        jpgOptn.quality = 12 ; // Max quality number
	        pathJpg+= saveName;
	        saveName = ""
	        // Not Working :(
	        if (saveName === ""){
	        	app.activeDocument.saveAs(new File(pathJpg), jpgOptn,true);
	        }

		}
	}

	textLayrr(textLayers,values)
	    
	app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);  // SAVECHANGES to save file
	}
	else{
	    alert("Give full path");
	}