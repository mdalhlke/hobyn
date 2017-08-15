$(document).ready(setUp);

function setUp() {
  $('.hobby').click(toggleDescription);
}

function toggleDescription(){
  $(this).find('.hobbyDescription').slideToggle(500);
}
