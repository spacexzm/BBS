var apiUserLoginin = function (form, callback) {
    var path = '/login'
    ajax('POST', path, form, callback)
}

var bindEventUserLoginIn = function () {
    var login_button = e('#id-button-loginin')
    login_button.addEventListener('click', function (event) {
        var input_username = e('#id-input-username')
        var username = input_username.value
        var input_password = e('#id-input-password')
        var password = input_password.value
        var form = {
            username: username,
            password: password,
        }
        apiUserLoginin(form, function (action) {
            if (action.login) {
                window.location.href = action.path
            } else {
                var error_p = e('#id-error-message')
                error_p.innerHTML = action.error
            }
        })
    })
}

var bindEvents = function () {
    bindEventUserLoginIn()
}

var __main = function () {
    bindEvents()
}

__main()