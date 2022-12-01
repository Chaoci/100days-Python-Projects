$(document).ready(function(){
    $(".heading").click(function(){
        $(".news_container").slideToggle("slow");
        $(".news_container").removeClass('hidden');
        $(".news_container").toggleClass('grid grid-cols-3');
    });
    $(".nba_title").click(function(){
        $(".nba_container").slideToggle("slow");
        $(".nba_container").removeClass("hidden");
    })
  });