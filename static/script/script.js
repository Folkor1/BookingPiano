$(document).ready(function() {

    let lesson = document.getElementById("lesson-confirmation");
    let lessonType = document.getElementById("lesson-type-confirmation");
    let selectDate = document.getElementById("date-confirmation");
    let selectTime = document.getElementById("time-confirmation");
    let booking = [];
    let date = [];
    let time = [];

    // Change lesson type options when clicked
    $("#piano-btn").on("click", function() {
        $("#piano-theory").addClass("d-none");
        $("#book-for-1").removeClass("d-none");
        $("#select-lesson-type").removeClass("d-none");
        $("#oo-buttons").removeClass("d-none");
        $("#piano").removeClass("d-none");
        booking.push('Piano');
    });

    $("#theory-btn").on("click", function() {
        $("#piano-theory").addClass("d-none");
        $("#book-for-1").removeClass("d-none");
        $("#select-lesson-type").removeClass("d-none");
        $("#oo-buttons").removeClass("d-none");
        $("#theory").removeClass("d-none");
        booking.push('Theory');
    });
    
    // Change online/offline options when clicked
    $("#online-btn").on("click", function() {
        $("#select-lesson-type").addClass("d-none");
        $("#oo-buttons").addClass("d-none");
        $("#select-date").removeClass("d-none");
        $("#calendar").removeClass("d-none");
        $('#online').removeClass("d-none");
        booking.push('Online');
    });

    $("#offline-btn").on("click", function() {
        $("#select-lesson-type").addClass("d-none");
        $("#oo-buttons").addClass("d-none");
        $("#select-date").removeClass("d-none");
        $("#calendar").removeClass("d-none");
        $('#offline').removeClass("d-none");
        booking.push('Offline');
    });

    // Back to lesson selection
    $("#back-lesson").on("click", function() {
        $("#select-lesson-type").addClass("d-none");
        $("#piano-theory").removeClass("d-none");
        $("#book-for-1").addClass("d-none");
        $("#oo-buttons").addClass("d-none");
        $("#piano").addClass("d-none");
        $("#theory").addClass("d-none");
        booking.splice(booking.indexOf('Piano', 'Theory'),1);
    });

    // Back to lesson type selection
    $("#back-lesson-type").on("click", function() {
        $("#calendar").addClass("d-none");
        $("#select-lesson-type").removeClass("d-none");
        $("#select-date").addClass("d-none");
        $("#oo-buttons").removeClass("d-none");
        $('#online').addClass("d-none");
        $('#offline').addClass("d-none");
        booking.splice(booking.indexOf('Online', 'Offline'),1);
    });

    // Pop-up on hover window
    $(function() {
        var moveLeft = 20;
        var moveDown = 10;
     
        $('a.trigger').hover(function() {
          $('div#pop-up').show();
        }, function() {
          $('div#pop-up').hide();
        });
     
        $('a.trigger').mousemove(function(e) {
          $("div#pop-up").css('top', e.pageY + moveDown).css('left', e.pageX + moveLeft);
        });
      });

      // Display time picker once date is selected
      $('#date').datepicker().on('changeDate', function() {
        $('#time-picker').removeClass('d-none');
      });

      // Display Book button once time is selected
      $('#time-picker').change(function() {
        $('#book-div').removeClass('d-none');
        var selectedTime = $("#time-picker option:selected").text();
        time.push(selectedTime);
      });

      // Get time from time picker
      function getTime() {
      selectTime.innerText = time[0];
      };

      // Get selections lesson types from booking menus
      function getLesson() {
        lesson.innerText = booking[0];
      };

      function getLessonType() {
        lessonType.innerText = booking[1];
      };

      // Get date from the calendar
      $('#date').datepicker().on('changeDate', function (selectedDate) {
        selectedDate = selectedDate.date.toString().slice(0, 10);
        date.push(selectedDate);
      });

      function getDate() {
        selectDate.innerText = date[0];
      };

      // Booking confirmation message
      $('#book-confirm').on("click", function() {
        $('#confirm-message').removeClass('d-none');
        $('#calendar').addClass('d-none');
        $('#select-date').addClass('d-none');
        $('#book-for-1').addClass('d-none');
        $("#piano").addClass("d-none");
        $("#theory").addClass("d-none");
        $("#online").addClass("d-none");
        $("#offline").addClass("d-none");
        getLesson();
        getLessonType();
        getDate();
        getTime();
      });

});
