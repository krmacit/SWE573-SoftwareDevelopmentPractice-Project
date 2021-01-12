document.body.addEventListener( 'click', function (event) {
    if( event.target.className === 'form-check-input dataset' ) {
        const form = event.target.form;
        const data = new FormData(form);

        const request = new XMLHttpRequest();
        request.open(form.method, form.action, true);
        request.send(data);
    }
});