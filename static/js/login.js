var apiUserLoginin = function (form, callback) {
    var path = '/login'
    ajax('POST', path, form, callback)
}

var apiUserSignin = function (form, callback) {
    var path = '/register'
    ajax('POST', path, form, callback)
}

var register_template = `
    <div class="form-register">
        <h2 class="form-login-heading">Please sign in</h2>
        <div class="username-form">
            <label for="inputUsername" class="sr-only">Username</label>
            <input type="text" id="id-input-username" class="form-control" placeholder="Username" required="" autofocus="">
        </div>

        <div class="password-form">
            <label for="inputPassword" class="sr-only">Password</label>
            <input type="password" id="id-input-password" class="form-control" placeholder="Password" minlength="3" required="">
        </div>
        
        <div class="password-form">
            <label for="inputPassword" class="sr-only">VerifyPassword</label>
            <input type="password" id="id-input-verify-password" class="form-control" placeholder="Verify Password" required="">
        </div>

        <div class="mesage-show">
            <p id="id-error-message" class="alert-danger"></p>
        </div>
        <button id="id-button-register" class="btn btn-lg btn-primary btn-block btn-register">Sign in</button>
        <button id="id-button-toggle" class="btn btn-lg btn-primary btn-block to-login">切换登录</button>
    </div>
`

var login_template = `
        <div class="form-login">
            <h2 class="form-login-heading">Please login in</h2>
            <div class="username-form">
                <label for="inputUsername" class="sr-only">Username</label>
                <input type="text" id="id-input-username" class="form-control" placeholder="Username" required="" autofocus="">
            </div>

            <div class="password-form">
                <label for="inputPassword" class="sr-only">Password</label>
                <input type="password" id="id-input-password" class="form-control" placeholder="Password" minlength="3" required="">
            </div>

            <div class="mesage-show">
                <p id="id-error-message" class="alert-danger"></p>
            </div>
            <button id="id-button-login" class="btn btn-lg btn-primary btn-block btn-login">Login in</button>
            <button id="id-button-toggle" class="btn btn-lg btn-primary btn-block to-register">切换注册</button>
        </div>
`

var loginAction = function () {
    var input_username = e('#id-input-username')
    var username = input_username.value
    var input_password = e('#id-input-password')
    var password = input_password.value
    var error_p = e('#id-error-message')
    if (username.length < 1) {
        error_p.innerHTML = "用户名不能为空！"
        return false
    } else if (password.length < 1) {
        error_p.innerHTML = "密码不能为空！"
        return false
    }
    var form = {
        username: username,
        password: password,
    }
    apiUserLoginin(form, function (action) {
        if (action.login) {
            window.location.href = action.path
        } else {
            error_p.innerHTML = action.error
        }
    })
}

var registerAction = function () {
    var error_p = e('#id-error-message')
    var input_username = e('#id-input-username')
    var username = input_username.value
    var input_password = e('#id-input-password')
    var password = input_password.value
    var input_verify_password = e('#id-input-verify-password')
    var verify_password = input_verify_password.value
    if (username.length < 4) {
        error_p.innerHTML = "用户名长度需大于4！"
        return false
    } else if (password.length < 4) {
        error_p.innerHTML = "密码长度需大于4！"
        return false
    }
    if (password == verify_password) {
        var form = {
            username: username,
            password: password,
        }
        apiUserSignin(form, function (action) {
            if (action.register) {
                var error_p = e('#id-error-message')
                error_p.setAttribute('class', 'alert-success')
                error_p.innerHTML = action.message
            } else {
                var error_p = e('#id-error-message')
                error_p.setAttribute('class', 'alert-danger')
                error_p.innerHTML = action.error
            }
        })
    } else {
        var error_p = e('#id-error-message')
        error_p.innerHTML = '两次密码不一致！'
    }
}

var bindEventUser = function () {
    var container = e('.container')
    container.addEventListener('click', function (event) {
        var self = event.target
        if (self.classList.contains('btn-register')) {
            registerAction()
        } else if (self.classList.contains('btn-login')) {
            loginAction()
        } else if (self.classList.contains('to-register')) {
            toggleLoginRegister(register_template)
        } else if (self.classList.contains('to-login')) {
            toggleLoginRegister(login_template)
        }

    })
}


var toggleLoginRegister = function (template) {
    var container = e('.container')
    container.innerHTML = template
}

var bindEvents = function () {
    bindEventUser()
}

var __main = function () {
    bindEvents()
}

__main()