var textLayers = ['start_day', 'start_super', 'start_month', 'end_day', 'end_super', 'end_month', 'student_name', 'course_name'];
	var values =  [['Subhasis Mondol', 'Eimon Farhad', 'Bapan Bala ', 'Ramiz Raza', 'Palash Nayak', 'Palash Nayak', 'Oishee Sikdar', 'Akanksha Saha', 'Mohak Mazumder', 'Nishantika Sardar', 'Subhajeet Saha', 'Subhajeet Saha', 'Kankan Das', 'Biki Dutta ', 'Debastuti Guha ', 'Arindam Kundu ', 'Moumita Basak'], ['th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'nd', 'nd', 'nd', 'nd', 'th', 'th', 'th', 'th', 'th'], ['07', '07', '04', '10', '13', '13', '08', '08', '22', '22', '02', '22', '25', '25', '25', '16', '29'], ['Jun, 2018', 'Jun, 2018', 'Jul, 2018', 'Jul, 2018', 'Jul, 2018', 'Jul, 2018', 'May, 2018', 'May, 2018', 'May, 2018', 'May, 2018', 'Dec, 2018', 'Jul, 2018', 'Jul, 2018', 'Jul, 2018', 'Jul, 2018', 'Aug, 2018', 'Jun, 2018'], ['th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'st', 'st'], ['07', '07', '07', '07', '07', '07', '16', '16', '16', '16', '27', '16', '16', '16', '07', '21', '21'], ['Dec, 2018', 'Dec, 2018', 'Dec, 2018', 'Dec, 2018', 'Dec, 2018', 'Dec, 2018', 'Nov, 2018', 'Nov, 2018', 'Nov, 2018', 'Nov, 2018', 'Apr, 2018', 'Nov, 2018', 'Nov, 2018', 'Nov, 2018', 'Dec, 2018', 'Dec, 2018', 'Dec, 2018'], ['Android Application Development', 'Android Application Development', 'Android Application Development', 'Android Application Development', 'Android Application Development', 'Advanced PHP Development', 'Website Designing', 'Website Designing', 'Website Designing', 'Website Designing', 'Professional C Programming', 'Website Designing', 'Website Designing', 'Website Designing', 'Android Application Development', 'Android Application Development', 'Android Application Development']];
	var pathPsd=prompt("Enter the path of psd","C:\\>>>").replace("\\","\\\\");
	var pathJpg = prompt("Enter the path to save JPG","C:\\\>>>").replace("\\","\\\\")
	var fixedPath = pathJpg
	var psdFile = new File(pathPsd);  
	var saveName = "";
	var layerName = "";
	var val = "";
	if(psdFile.exists){

	    app.open(psdFile);
	    function textLayrr (layers,changes) {

	    	var names = changes[0]

	    	var start_spr = changes[1]
	    	var start_day = changes[2]
	    	var start_mnth = changes[3]
	    	

			var end_spr = changes[4]
	    	var end_day = changes[5]
	    	var end_mnth = changes[6]

	    	var course = changes[7]

	      for (i = 0 ; i< names.length ; i++){

	      	val = []

	      	val.push(start_day[i])
	      	val.push(start_spr[i])
	      	val.push(start_mnth[i])

	      	val.push(end_day[i])
	      	val.push(end_spr[i])
	      	val.push(end_mnth[i])

	      	val.push(names[i])
	      	val.push(course[i])

	      	for (var j = 0; j < layers.length; j++) {
		      		app.activeDocument.layer = activeDocument.artLayers.getByName(layers[j]);
	                if(app.activeDocument.layer.visible == true){
	                    app.activeDocument.layer.textItem.contents= val[j];
				}
	      	}
	      	var jpgFile = new File(pathJpg+"\\"+val[6]+".jpg");

			jpgSaveOptions = new JPEGSaveOptions();
			// jpgSaveOptions.formatOptions = FormatOptions.OPTIMIZEDBASELINE;
			// jpgSaveOptions.embedColorProfile = true;
			// jpgSaveOptions.matte = MatteType.NONE;
			jpgSaveOptions.quality = 12;

			if (jpgFile.exists){
				var dupFile = new File(pathJpg+"\\" + val[6] + i.toString() +".jpg");
				activeDocument.saveAs(dupFile, jpgSaveOptions, true, Extension.LOWERCASE);
				pathJpg = fixedPath
	      	}
	      	else{
	      		activeDocument.saveAs(jpgFile, jpgSaveOptions, true, Extension.LOWERCASE);
				pathJpg = fixedPath
	      	}
			

			
		}
		

		}

	textLayrr(textLayers,values)
	    
	app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);  // SAVECHANGES to save file
	}
	else{
	    alert("Give full path");
	}