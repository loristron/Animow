	$(document).ready(function() {
		$('#modal-btn').click(function () {
			$('#modal1')
			 .modal('show')
			;
			})

		$('#modal-btn2').click(function () {
			$('#modal2')
			 .modal('show')
			;

		})

		$('#bar-modal-btn').click(function () {
			$('.ui.basic.modal')
			 .modal('show')
			;

		})

		$('.message .close')
  		.on('click', function() {
   		 $(this)
      		.closest('.message')
     			 .transition('fade')
    		;
 	})
})