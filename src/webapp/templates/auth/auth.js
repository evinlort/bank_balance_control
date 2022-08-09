
(() => {
    log("Cleaning")
    $("#username").val("")
    $("#password").val("")
})()

$("#login_button").on("click submit", () => {
    var username = $("#username")
    var password = $("#password")
    if (is_empty(username.val()) || is_empty(password.val())) {
        log("Empty")
        username.val("")
        password.val("")
        return false
    }
    try_to_login(username.val(), password.val())
})

is_empty = (value) => value == ""
is_not_empty = (value) => !is_empty(value)
try_to_login = (user, pass) => {
    $.post("/auth/login", {username: user, password: pass}, (data, textStatus, jqXHR) => {
        log(data)
        if(!data) {
            location.reload()
        }
        location.href = "{{ url_for('main.home_page') }}"
    })
}