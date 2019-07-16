$(document).ready(function() {
    var theme = localStorage.getItem('theme');
    if (theme == 'dark') {
        $('link[href="/static/light.css"]').remove();
    } else if (theme == 'light') {
        $('link[href="/static/dark.css"]').remove();
    } else {
        console.log('localStorage unset')
        $('link[href="/static/light.css"]').remove();
    }

    $('a#toggle').click(function (e){
        console.log('Clicked');
        var dark = $('link[href="/static/dark.css"]');
        var light = $('link[href="/static/light.css"]');
        if (dark.length > 0) {
            console.log('Switch to light');
            localStorage.setItem('theme', 'light');
            dark.attr('href','/static/light.css');
        } else {
            console.log('Switch to light');
            localStorage.setItem('theme', 'dark');
            light.attr('href','/static/dark.css');
        }
       // $('link[href="/static/dark.css"]').attr('href','/static/light.css');
       // $('link[href="/static/light.css"]').attr('href','/static/dark.css');
        e.preventDefault();

    });
    // $('#original').click(function (){
    //    $('link[href="style2.css"]').attr('href','style1.css');
    // });

    $('a.toggle_losses').click(function(e){
       $('img.red').parent().parent().toggle();
        $('a.hide').toggle();
        $('a.show').toggle();
        e.preventDefault();
    });

    $('a.toggle_losses2').click(function(e){
       $('img.red').parent().parent().parent().toggle();
        $('a.hide').toggle();
        $('a.show').toggle();
        e.preventDefault();
    });

    $.getJSON('/static/search.json', function(data){
        $("#searchbox input").keyup(function(){
            $("#search_results").removeClass("active");
            var input = $("#searchbox input").val().toLowerCase();
            console.log(input);

            $("body").click(function(){
                $("#search_results").removeClass("active");
            });

            // Prevent events from getting pass .popup
            $("#search_results, #searchbox").click(function(e){
              e.stopPropagation();
            });

            $("#search_results").text('');
            var heroes = [];
            var players = [];
            if (input.length >= 2) {
                $.each(data['heroes'], function (key, value) {
                    if (key.toLowerCase().indexOf(input) > -1) {
                        heroes.push(key);
                    }
                    if (value.valid.indexOf(input) > -1) {
                        if (heroes.indexOf(key) == -1) {
                         heroes.push(key)
                        }
                    }
                });
                $.each(data['players'], function (key, value) {
                    if (key.toLowerCase().indexOf(input) > -1) {
                       players.push(key);
                    }
                    if (value.valid.indexOf(input) > -1) {
                        if (found.indexOf(key) == -1) {
                            players.push(key)
                        }
                    }
                });

                if (heroes.length > 0 || players.length > 0) {
                    $("#search_results").addClass('active')
                }
                else {
                    $("#search_results").removeClass('active')
                }


                $("#search_results").append('Heroes');
                $("<ul>").addClass("heroes").appendTo("#search_results");
                if (heroes.length > 0) {
                    $.each(heroes, function(key, value) {
                        $("#search_results ul.heroes").append(
                                "<li><a href='/hero/"+ value +"'>"+ value +"</a></li>"
                        )
                    })
                } else {
                    $("#search_results ul.heroes").append(
                            "<li>No results</li>"
                    )
                }

                $("#search_results").append('Players');
                $("<ul>").addClass("players").appendTo("#search_results");
                if (players.length > 0) {

                    $.each(players, function(key, value) {
                        $("#search_results ul.players").append(
                                "<li><a href='/player/"+ value +"'>"+ value +"</a></li>"
                        )
                    })
                } else {
                    $("#search_results ul.players").append(
                            "<li>No results</li>"
                    )
                }






            }
        });
    });
});

$(document).keyup(function(e) {
  if (e.keyCode === 27) {
    $("#search_results").removeClass('active')
  }   // esc
});