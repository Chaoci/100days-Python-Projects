$(document).ready(function(){
    $(".news_select").click(function(){
        $(".news_container").slideToggle("slow");
        $(".news_container").removeClass('hidden');
    // if press the selection the other selections will be hidden 
        if($(".nba_container").css('display') == "block"){
            $(".nba_container").slideToggle();
        }else if ($(".movie_container").css('display') == "block"){
            $(".movie_container").slideToggle();
        };
    });

    $(".nba_select").click(function(){
        $(".nba_container").slideToggle("slow");
        $(".nba_container").removeClass("hidden");
    // if press the selection the other selections will be hidden 
        if ($(".news_container").css('display')=='block'){
            $(".news_container").slideToggle();
        }else if ($(".movie_container").css('display') == "block"){
            $(".movie_container").slideToggle();
        };
    });

    $(".movie_select").click(function(){
        $(".movie_container").slideToggle("slow");
        $(".movie_container").removeClass("hidden");
        if ($(".news_container").css('display')=='block'){
            $(".news_container").slideToggle();
        }else if ($(".nba_container").css('display') == "block"){
            $(".nba_container").slideToggle();
        };
    });
    clockUpdate();
    setInterval(clockUpdate, 1000);
});

function clockUpdate() {
    var date = new Date();
    function addZero(x) {
      if (x < 10) {
        return x = '0' + x;
      } else {
        return x;
      }
    }
  
    function twelveHour(x) {
      if (x > 12) {
        return x = x - 12;
      } else if (x == 0) {
        return x = 12;
      } else {
        return x;
      }
    }
  
    var h = addZero(twelveHour(date.getHours()));
    var m = addZero(date.getMinutes());
    var s = addZero(date.getSeconds());
  
    $('.digital-clock').text(h + ':' + m + ':' + s)
  };