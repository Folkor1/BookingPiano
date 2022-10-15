$(document).ready(function() {

    let lesson = document.getElementById("lesson-confirmation");
    let lessonType = document.getElementById("lesson-type-confirmation");
    let selectDate = document.getElementById("date-confirmation");
    let selectTime = document.getElementById("time-confirmation");
    let pianoOrTheory = document.getElementById("piano-or-theory");
    let onlineorOffline = document.getElementById("online-or-offline");
    let editDateDate = document.getElementById("edit-date-date");
    let editDateTime = document.getElementById("edit-time");
    let booking = [];
    let date = [];
    let time = [];


    // Change lesson type options when clicked
    $("#piano-btn").on("click", function() {
        $("#piano-theory").addClass("d-none");
        $("#book-for").removeClass("d-none");
        $("#select-lesson-type").removeClass("d-none");
        $("#oo-buttons").removeClass("d-none");
        booking.push('Piano');
        pianoOrTheory.innerText = booking[0];
    });

    $("#theory-btn").on("click", function() {
        $("#piano-theory").addClass("d-none");
        $("#book-for").removeClass("d-none");
        $("#select-lesson-type").removeClass("d-none");
        $("#oo-buttons").removeClass("d-none");
        $("#theory").removeClass("d-none");
        booking.push('Theory');
        pianoOrTheory.innerText = booking[0];
    });
    
    // Change online/offline options when clicked
    $("#online-btn").on("click", function() {
        $("#select-lesson-type").addClass("d-none");
        $("#oo-buttons").addClass("d-none");
        $("#select-date").removeClass("d-none");
        $("#calendar").removeClass("d-none");
        $('#online').removeClass("d-none");
        booking.push('Online');
        onlineorOffline.innerText = booking[1];
    });

    $("#offline-btn").on("click", function() {
        $("#select-lesson-type").addClass("d-none");
        $("#oo-buttons").addClass("d-none");
        $("#select-date").removeClass("d-none");
        $("#calendar").removeClass("d-none");
        $('#offline').removeClass("d-none");
        booking.push('Offline');
        onlineorOffline.innerText = booking[1];
    });

    // Back to lesson selection
    $("#back-lesson").on("click", function() {
        $("#select-lesson-type").addClass("d-none");
        $("#piano-theory").removeClass("d-none");
        $("#book-for").addClass("d-none");
        $("#oo-buttons").addClass("d-none");
        $("#piano").addClass("d-none");
        $("#theory").addClass("d-none");
        booking.splice(booking.indexOf('Piano', 'Theory'),1);
        onlineorOffline.innerText = "";
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
        onlineorOffline.innerText = "";
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
        time.splice(0);
        var selectedTime = $("#time-picker option:selected").text();
        console.log(time)
        time.push(selectedTime);
      });

      // Get time from time picker
      function getTime() {
      selectTime.innerText = time[0];
      document.getElementById('time_inp').value = time[0];
      };

      // Get selections lesson types from booking menus
      function getLesson() {
        lesson.innerText = booking[0];
        document.getElementById('lesson_inp').value = booking[0];
      };

      function getLessonType() {
        lessonType.innerText = booking[1];
        document.getElementById('lesson_type_inp').value = booking[1];
      };

      // Get date from the calendar
      $('#date').datepicker().on('changeDate', function (selectedDate) {
        date.splice(0);
        selectedDate = selectedDate.date.toLocaleDateString('en-CA');
        date.push(selectedDate);
      });

      function getDate() {
        selectDate.innerText = date[0];
        document.getElementById('date_inp').value = date[0];
      };

      // Booking confirmation message
      $('#book-confirm').on("click", function() {
        $('#confirm-message').removeClass('d-none');
        $('#calendar').addClass('d-none');
        $('#select-date').addClass('d-none');
        $('#book-for').addClass('d-none');
        getLesson();
        getLessonType();
        getDate();
        getTime();
      });

      // Confirmation message - back button
      $('#back-to-selection').on("click", function() {
        $('#confirm-message').addClass('d-none');
        $('#calendar').removeClass('d-none');
        $('#select-date').removeClass('d-none');
        $('#book-for').removeClass('d-none');
      });

      // Edit date confirmation message
      $('#edit-book-confirm').on("click", function() {
        $('#edit-date-time').addClass('d-none');
        $('#edit-date-form').removeClass('d-none');
        getDateDate();
        getDateTime();
      });

      // Edit date - back button
      $('#edit-date-back-to-selection').on("click", function() {
        $('#edit-date-form').addClass('d-none');
        $('#edit-date-time').removeClass('d-none');
      });

      // Get date from date picker on edit
      function getDateDate() {
        editDateDate.innerText = date[0];
        document.getElementById('edit_date_inp').value = date[0];
      };

      // Get time from time picker on edit
      function getDateTime() {
        editDateTime.innerText = time[0];
        document.getElementById('edit_time_inp').value = time[0];
        };

});
