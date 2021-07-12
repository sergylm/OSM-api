$('#btn').click(function(){
    var btn = $(this);
    if(btn.hasClass('convert')){
        btn.text('Converting').prop('disabled', true)
        $.post('/convert').then(function(){
            btn.prop('disabled', false).text('Download files').removeClass('convert').addClass('download')
        })
    } else{
        btn.text('Downloaded')
        window.location = '/download'
    }
})