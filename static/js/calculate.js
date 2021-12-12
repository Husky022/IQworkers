$(document).ready(function () {

      $('#object_type input:checkbox').click(function(){
          if ($(this).is(':checked')) {
              $('#object_type input:checkbox').not(this).prop('checked', false);
          }
      });


      $('#send-calculation').on('click',function(){
          $.ajax({
              data: {
                  'checked': $('input[name="chk-option"]:checked').serialize(),
                  'square': $('#square').val(),
                  'csrfmiddlewaretoken': csrf_token
                    },
              method: 'POST',
              url: '/get_calculation/',
              success: function (response) {
                  console.log(response.result)
                  $('.calc-result').html(response.result);
                  if (!$('.button-reset-calc').length){
                      $('#reset-calc').append($('<button class="button-reset-calc">Сбросить</button>'));
                  }

                }
          });
      });

      $('#reset-calc').on('click',function(){
          $.ajax({
              url: '/reset_calculation/',
              success: function () {
                  $('.calc-result').html('');
                  $('input[name="chk-option"]:checked').prop('checked', false);
                }
          });
      });




  })


