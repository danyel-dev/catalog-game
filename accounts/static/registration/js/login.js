let checkbox = document.getElementById('view_password');
let inputPassword = document.getElementById('id_password')

checkbox.addEventListener("click", function() {
    if (this.checked) {
        inputPassword.type = 'text'
    } else {
        inputPassword.type = 'password'
    }
})
