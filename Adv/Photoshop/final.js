var textLayers = ['student_name', 'start_date_', 'end_date', 'status', 'course_name_in_certificate'];
	var values =  [['Subhasis Mondol', 'Eimon Farhad', 'Bapan Bala ', 'Ramiz Raza', 'Palash Nayak', 'Palash Nayak', 'Oishee Sikdar', 'Akanksha Saha', 'Mohak Mazumder', 'Nishantika Sardar', 'Subhajeet Saha', 'Subhajeet Saha', 'Kankan Das', 'Biki Dutta ', 'Debastuti Guha ', 'Arindam Kundu ', 'Moumita Basak'], ['07 June 2018', '07 June 2018', '04 July 2018', '10 July 2018', '13 July 2018', '13 July 2018', '08 May 2018', '08 May 2018', '22 May 2018', '22 May 2018', '02 December 2018', '22 July 2018', '25 July 2018', '25 July 2018', '25 July 2018', '16 August 2018', '29 June 2018'], ['07 December 2018', '07 December 2018', '07 December 2018', '07 December 2018', '07 December 2018', '07 December 2018', '16 November 2018', '16 November 2018', '16 November 2018', '16 November 2018', '27 April 2018', '16 November 2018', '16 November 2018', '16 November 2018', '07 December 2018', '21 December 2018', '21 December 2018'], ['complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete', 'complete'], ['Android Application Development', 'Android Application Development', 'Android Application Development', 'Android Application Development', 'Android Application Development', 'Advanced PHP Development', 'Website Designing', 'Website Designing', 'Website Designing', 'Website Designing', 'Professional C Programming', 'Website Designing', 'Website Designing', 'Website Designing', 'Android Application Development', 'Android Application Development', 'Android Application Development']];
	var pathPsd=prompt("Enter the path of psd","C:\\>>>").replace("\\","\\\\");
	var pathJpg = prompt("Enter the path to save JPG","C:\\>>>").replace("\\","\\\\")

	var psdFile = new File(pathPsd);  
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