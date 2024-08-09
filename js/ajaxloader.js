//refernce : http://w3lessons.info/demo/ajax-indicator/
//http://w3lessons.info/2014/01/26/showing-busy-loading-indicator-during-an-ajax-request-using-jquery/
function ShowProgress()
{
    var text = 'loading data.. please wait..';

    if(jQuery('body').find('#resultLoading').attr('id') != 'resultLoading'){
     jQuery('body').append('<div id="resultLoading" style="display:none"><div><img src="'+document.location.origin+'/static/images/ajax-loader.gif"><div>'+text+'</div></div><div class="bg"></div></div>');
     // jQuery('body').append('<div id="resultLoading" style="display:none"><div><div>'+text+'</div></div><div class="bg"></div></div>');
     }

    jQuery('#resultLoading').css({
        'width':'100%',
        'height':'100%',
        'position':'fixed',
        'z-index':'10000000',
        'top':'0',
        'left':'0',
        'right':'0',
        'bottom':'0',
        'margin':'auto'
    });

    jQuery('#resultLoading .bg').css({
        'background':'#000000',
        'opacity':'0.7',
        'width':'100%',
        'height':'100%',
        'position':'absolute',
        'top':'0'
    });

    jQuery('#resultLoading>div:first').css({
        'width': '250px',
        'height':'75px',
        'text-align': 'center',
        'position': 'fixed',
        'top':'0',
        'left':'0',
        'right':'0',
        'bottom':'0',
        'margin':'auto',
        'font-size':'16px',
        'z-index':'10',
        'color':'#ffffff'

    });

    jQuery('#resultLoading .bg').height('100%');
       jQuery('#resultLoading').fadeIn(300);
    jQuery('body').css('cursor', 'wait');
}

function StopProgress()
{
    jQuery('#resultLoading .bg').height('100%');
       jQuery('#resultLoading').fadeOut(300);
    jQuery('body').css('cursor', 'default');
}

/*
jQuery(document).ajaxStart(function () {
    ShowProgress();
}).ajaxStop(function () {
    StopProgress();
});
*/


//Sridhar On 2022-Apr-02 12:12 PM
// when form submit while loading please wait loader

$('form').on('submit',function(event) {

    if( $('form').valid())
    {
           ShowProgress();
    }      
              // alert("test")
});