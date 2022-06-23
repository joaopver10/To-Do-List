var count = 5;

add_task(); // Call the add_task function
delete_task(); // Call the delete_task function

function add_task() {

  $('.add-new-task').submit(function(){
    var new_task = $('.add-new-task input[name=descricao]').val();
    count = count + 1;

    var print = '<li><span>' + new_task + '</span><button id="' + count + '" class="delete-button">X</button></li>';

    if(new_task !== ''){
      $('.add-new-task input[name=new-task]').val('');
      $(print).appendTo('.task-list ul').hide().fadeIn();
      delete_task();
    }
    return false;
  });
}

function delete_task() {
  $('.delete-button').click(function(){
    var current_element = $(this);
    var id = $(this).attr('id');
    current_element.parent().fadeOut("fast", function() { $(this).remove(); });
  });
}

