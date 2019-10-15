var textLayers = ['student_name', 'start_date_', 'end_date', 'status', 'course_name_in_certificate'];
	var values =  [['Subhasis Mondol', 'Eimon Farhad', 'Bapan Bala ', 'Ramiz Raza', 'Palash Nayak', 'Palash Nayak', 'Oishee Sikdar', 'Akanksha Saha', 'Mohak Mazumder', 'Nishantika Sardar', 'Subhajeet Saha', 'Subhajeet Saha', 'Kankan Das', 'Biki Dutta ', 'Debastuti Guha ', 'Arindam Kundu ', 'Moumita Basak'], ['07 June 2018', '07 June 2018', '04 July 2018', '10 July 2018', '13 July 2018', '13 July 2018', '08 May 2018', '08 May 2018', '22 May 2018', '22 May 2018', '02 December 2018', '22 July 2018', '25 July 2018', '25 July 2018', '25 July 2018', '16 August 2018', '29 June 2018'], ['07 December 2018', '07 December 2018', '07 December 2018', '07 December 2018', '07 December 2018', '07 December 2018', '16 November 2018', '16 November 2018', '16 November 2018', '16 November 2018', '27 April 2018', '16 November 2018', '16 November 2018', '16 November 2018', '07 December 2018', '21 December 2018', '21 December 2018'], ['complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete'], ['Android Application Development', 'Android Application Development', 'Android Application Development', 'Android Application Development', 'Android Application Development', 'Advanced PHP Development', 'Website Designing', 'Website Designing', 'Website Designing', 'Website Designing', 'Professional C Programming', 'Website Designing', 'Website Designing', 'Website Designing', 'Android Application Development', 'Android Application Development', 'Android Application Development']];
	var pathPsd=prompt("Enter the path of psd","C:\\>>>").replace("\\","\\\\");
	var pathJpg = prompt("Enter the path to save JPG","C:\\\>>>").replace("\\","\\\\")
	var fixedPath = pathJpg
	var psdFile = new File(pathPsd);  
	var saveName = "";
	var layerName = "";
	var val = "";
	if(psdFile.exists){

	    app.open(psdFile);
	// prompt([prompt message],[title])

		function setLayerName(layerData){
			for(i = 0 ; i<layerData.length ; i++){
				
			}
		}


	    function textLayrr (layers,changes) {

	    	var names = changes[0]
	    	var course = changes[1]
	    	var start_date = changes[2]
	    	var end_date = changes[3]

	      for (i = 0 ; i< names.length ; i++){

	      	val = []

	      	val.push(names[i])
	      	val.push(course[i])
	      	val.push(start_date[i])
	      	val.push(end_date[i])

	      	for (var j = 0; j < layers.length; j++) {
		      		app.activeDocument.layer = activeDocument.artLayers.getByName(layers[j]);
	                if(app.activeDocument.layer.visible == true){
	                    app.activeDocument.layer.textItem.contents= val[j];
				}
	      	}

	      	var jpgFile = new File(pathJpg+"\\"+val[0]+".jpg");
			jpgSaveOptions = new JPEGSaveOptions();
			jpgSaveOptions.formatOptions = FormatOptions.OPTIMIZEDBASELINE;
			jpgSaveOptions.embedColorProfile = true;
			jpgSaveOptions.matte = MatteType.NONE;
			jpgSaveOptions.quality = 12;

			activeDocument.saveAs(jpgFile, jpgSaveOptions, true, Extension.LOWERCASE);

			
		}
		

		}

	textLayrr(textLayers,values)
	    
	app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);  // SAVECHANGES to save file
	}
	else{
	    alert("Give full path");
	}