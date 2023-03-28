function toggleVisibility() {
    var getPassword = document.getElementById('pswrd');
    if(getPassword.type === 'password') {
        getPassword.type = 'text';
    } else {
        getPassword.type = 'password';
    }
}