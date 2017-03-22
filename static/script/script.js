$(function(){
    //resize table
    $('table').width($('.demo-content').width());

    //resize table if window was resized
    $(window).resize(function(){
        $('table').width($('.demo-content').width());
    });
});