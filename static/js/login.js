const apiUserLoginin = function (form, callback) {
    let path = '/login'
    ajax('POST', path, form, callback)
}


const apiUserSignin = function (form, callback) {
    let path = '/register'
    ajax('POST', path, form, callback)
}


const register_template = `
    <form class="form-register">
        <h2 class="form-login-heading">Please sign in</h2>
        <div class="username-form">
            <label for="inputUsername" class="sr-only">Username</label>
            <input type="text" id="id-input-username" class="form-control" placeholder="Username" pattern="[A-z0-9]{3,}" required autofocus>
        </div>

        <div class="password-form">
            <label for="inputPassword" class="sr-only">Password</label>
            <input type="password" id="id-input-password" class="form-control" placeholder="Password" pattern="[A-z0-9]{3,}" required>
        </div>
        
        <div class="password-form">
            <label for="inputPassword" class="sr-only">VerifyPassword</label>
            <input type="password" id="id-input-verify-password" class="form-control" placeholder="Verify Password" pattern="[A-z0-9]{3,}" required>
        </div>

        <div class="mesage-show">
            <p id="id-error-message" class="alert-danger"></p>
        </div>
        <button id="id-button-register" class="btn btn-lg btn-primary btn-block btn-register">Sign in</button>
    </form>
    <div class="toggle">
        <button id="id-button-toggle" class="btn btn-lg btn-primary btn-block to-login">切换登录</button>
    </div>
`


const login_template = `
        <form class="form-login">
            <h2 class="form-login-heading">Please login in</h2>
            <div class="username-form">
                <label for="inputUsername" class="sr-only">Username</label>
                <input type="text" id="id-input-username" class="form-control" placeholder="Username" pattern="[A-z0-9]{3,}" required autofocus>
            </div>

            <div class="password-form">
                <label for="inputPassword" class="sr-only">Password</label>
                <input type="password" id="id-input-password" class="form-control" placeholder="Password" pattern="[A-z0-9]{3,}" required>
            </div>

            <div class="mesage-show">
                <p id="id-error-message" class="alert-danger"></p>
            </div>
            <button id="id-button-login" class="btn btn-lg btn-primary btn-block btn-login">Login in</button>
        </form>
        <div class="toggle">
            <button id="id-button-toggle" class="btn btn-lg btn-primary btn-block to-register">切换注册</button>
        </div>
`


const loginAction = function () {
    let input_username = e('#id-input-username')
    let username = input_username.value
    let input_password = e('#id-input-password')
    let password = input_password.value
    let error_p = e('#id-error-message')
    let form = {
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


const registerAction = function () {
    let input_username = e('#id-input-username')
    let username = input_username.value
    let input_password = e('#id-input-password')
    let password = input_password.value
    let input_verify_password = e('#id-input-verify-password')
    let verify_password = input_verify_password.value
    if (password == verify_password) {
        let form = {
            username: username,
            password: password,
        }
        apiUserSignin(form, function (action) {
            if (action.register) {
                let error_p = e('#id-error-message')
                error_p.setAttribute('class', 'alert-success')
                error_p.innerHTML = action.message
            } else {
                let error_p = e('#id-error-message')
                error_p.setAttribute('class', 'alert-danger')
                error_p.innerHTML = action.error
            }
        })
    } else {
        let error_p = e('#id-error-message')
        error_p.innerHTML = '两次密码不一致！'
    }
}


const submitLoginAction = function () {
    let formLogin = e('.form-login')
    formLogin.onsubmit = function (event) {
        event.preventDefault()
        loginAction()
    }
}


const submitRegisterAction = function () {
    let formLogin = e('.form-register')
    formLogin.onsubmit = function (event) {
        event.preventDefault()
        registerAction()
    }
}


const bindEventContainer = function () {
    let container = e('.container')
    container.addEventListener('click', function (event) {
        let self = event.target
        if (self.classList.contains('to-register')) {
            toggleLoginRegister(register_template)
            submitRegisterAction()
        } else if (self.classList.contains('to-login')) {
            toggleLoginRegister(login_template)
            submitLoginAction()
        }
    })
}



const toggleLoginRegister = function (template) {
    let container = e('.container')
    container.innerHTML = template
}

const bindEvents = function () {
    bindEventContainer()
    submitLoginAction()
    submitRegisterAction()
}

const __main = function () {
    bindEvents()
}

__main()