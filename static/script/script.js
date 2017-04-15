$(function(){
    /*---------- Resize elements ----------*/
    var resizeElements = function(){
        //get the current window width
        var mainWidth = $('.demo-content').width();
        $('table').width(mainWidth);
        $('#textField').width(mainWidth);
        $('#btn_download').css({'min-width': mainWidth});
    }

     //resize table if window was resized
    $(window).resize(resizeElements);
    resizeElements();

    //Style modifications
    $('#search').css({'text-align': 'center'});
    $('.mdl-textfield__label').css({'text-align': 'center'});
    $('.mdl-checkbox').width(0);
    
    /*---------- Click Event(s) ----------*/
    //Filter-elements
    $('#checkboxTracks').click(function(){
        $('#sliderTracks').attr({ disabled: !this.checked });
    });

    $('#checkboxAlbum').click(function(){
        $('#sliderAlbum').attr({ disabled: !this.checked });
    });

    //Press enter 
    $(document).keypress(function(e) {
        if(e.which == 13) { //<Enter> pressed
            if( ($('#search').val()).length > 0 ) {
                //Send request
                $.post("/search/", {
                    checkboxAlbum:  $('#checkboxAlbum').is(":checked"),
                    checkboxTracks: $('#checkboxTracks').is(":checked"),
                    sliderTracks:   $('#sliderTracks').val(),
                    sliderAlbum:    $('#sliderAlbum').val(),
                    searchText:     $('#search').val()
                })

                //Server response
                .done(function(data) {
                    //Parse html
                    var response = $.parseHTML(data);

                    //output
                    $("#my-table").html(response);

                    //upgrade/resize elements
                    componentHandler.upgradeDom();
                    resizeElements();

                    //Download button
                    $('#btn_download').click(function(){
                        $("table").find("tr.is-selected").each(function(){
                            console.log(this);
                        });

                        /*
                        $.post("/download/", {
                                name: "IGnoXX"
                        });
                        */
                    });
                });
            }
        }
    });
});