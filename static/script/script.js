$(function(){
    //resize table
    var mainWidth = $('.demo-content').width();
    $('table').width(mainWidth);
    $('#textField').width(mainWidth);
    $('#btn_download').css({'min-width': mainWidth});

    $('#search').css({'text-align': 'center'});
    $('.mdl-textfield__label').css({'text-align': 'center'});
    $('.mdl-checkbox').width(0);
    

    //register changes on clicks
    $('#checkboxTracks').click(function(){
        $('#s1').val( this.checked );
        $('#sliderTracks').attr({ disabled: !this.checked });
    });

    $('#checkboxAlbum').click(function(){
        $('#s2').val( this.checked );
        $('#sliderAlbum').attr({ disabled: !this.checked });
    });

    $('#sliderTracks').mouseup(function(){
        $('#s3').val( this.value );
    });

    $('#sliderAlbum').mouseup(function(){
        $('#s4').val( this.value );
    });

    //resize table if window was resized
    $(window).resize(function(){
        mainWidth = $('.demo-content').width();
        $('table').width(mainWidth);
        $('#btn_download').css({'min-width': mainWidth});
    });
});