
$(function(){


	var images=[];
	var amount=0;
	var index=0;

	var dropbox = $('#dropbox'),
		message = $('.message', dropbox);
	
	dropbox.filedrop({
		// The name of the $_FILES entry:
		paramname:'pic',
		
		maxfiles: 5,
    	maxfilesize: 2,
		url: 'post_file.php',
		
		uploadFinished:function(i,file,response){
			$.data(file).addClass('done');
			// response is the JSON object that post_file.php returns
		},
		
    	error: function(err, file) {
			switch(err) {
				case 'BrowserNotSupported':
					showMessage('Your browser does not support HTML5 file uploads!');
					break;
				case 'TooManyFiles':
					alert('Too many files! Please select 5 at most! (configurable)');
					break;
				case 'FileTooLarge':
					alert(file.name+' is too large! Please upload files up to 2mb (configurable).');
					break;
				default:
					break;
			}
		},



		// Called before each upload is started
		beforeEach: function(file){
			if(!file.type.match(/^image\//)){
				alert('Only images are allowed!');
				
				// Returning false will cause the

				return false;
			}
		},
		
		uploadStarted:function(i, file, len){
			// amount=i+1;
			// console.log(images.length);

			if(images.length<6){
				images.push(file);
				createImage(file);
			}else{
				alert("The max is 6!")
			}
		},
		
		progressUpdated: function(i, file, progress) {
			$.data(file).find('.progress').width(progress);
		}
    	

	});
	
	var template = '<div class="preview">'+
						'<span class="imageHolder">'+
							'<img />'+
							'<span class="uploaded"></span>'+
						'</span>'+
						'<div>'+
						'</div>'+
					'</div>'; 
	
	
	function createImage(file){

		var preview = $(template), 
			image = $('img', preview);
			
		var reader = new FileReader();
		
		image.width = 100;
		image.height = 100;
		
		reader.onload = function(e){
			
			image.attr('src',e.target.result);
		};

		reader.readAsDataURL(file);
		message.hide();
		dropbox.append(preview);
		
	}

	$(".buttonpost").click(function() {

		var data = new FormData();
		data.append("userid", "Groucho");
		data.append("notecls", "hahahaha");
		data.append("puttime", "123123");
		data.append("clstime", "888jjj");
		data.append("picnum", 3);
		$.each(images, function( index, value ) {
			 data.append( "notepic"+index ,value );
		});
		$.ajax({
			type: "POST",
			url:'http://notemoment.tech/postnotes/', 
			data:data,
			processData: false,  // tell jQuery not to process the data
  			contentType: false,   // tell jQuery not to set contentType 
  			crossDomain: false,
    	});
		console.log(data);
		});

});



	$(".clear").click(function() {
		// $(".preview").remove();
		// images=[];
		alert($( "#selector option:selected" ).text());

		});




