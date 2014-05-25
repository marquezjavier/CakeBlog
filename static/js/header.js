 $(document).ready(function(){
	 
	 var allowBlink = true;
	 
	 $('#blinker').html('_');
	 $('#blinker').fadeOut(1000).fadeIn(1000).fadeOut(1000).fadeOut(1000).fadeIn(1000).fadeOut(1000).fadeOut(1000).fadeIn(1000).fadeOut(1000).fadeIn(1000);
	 
	 $('#blinker').click(function() {
		 allowBlink = !allowBlink;
	 });
	 
 });