function index(){
  $.ajax({
    url:'/notes',
    method:'GET',
    success: function(data){
      //data back from the controller
      $('#notes').html(data);
    }
  });
}
$(document).ready(function(){
  console.log('hello world');
  index();
  $.ajax({
    url:'/notes/new',
    method:'GET',
    success: function(data){
      //data back from the controller
      $('#new').html(data);
    }
  })
  $(document).on('submit', 'form', function(e){
    e.preventDefault();
    $.ajax({
      url:$(this).attr('action'),
      method:$(this).attr('method'),
      data:$(this).serialize(), // turn the data into a string that many backends can read (including PHP, python)
      success: function(data){
        //data back from the controller
        $('#notes').html(data);
      }
    }
    );

    return false;
  })
});
