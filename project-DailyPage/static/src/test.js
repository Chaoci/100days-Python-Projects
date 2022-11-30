$(document).ready(function(){
    $(".heading").click(function(){
        $(".news_container").slideToggle("slow");
        $(".news_container").removeClass('hidden');
        $(".news_container").toggleClass('grid grid-cols-3');
    });
  });