$("#day_of_birth_parsed").datepicker({
    changeMonth: true,
    changeYear: true,
    minDate: "-120Y",
    maxDate: "+0D",
    altField: "#day_of_birth",
    altFormat: "yy-mm-dd",
    dateFormat: "dd/mm/yy",
    yearRange: "c-120:c+0"
}).datepicker('setDate', '+0d')

$("#email").on("blur", (e) => {
    var email = $(e.target)
    if (!validate_email(email.val())) {
        toast_warning("Please correct the email", "Not valid email.", () => select_input(email))
        return false
    }
    var username = $("#username")
    if (!username.val()) {
        let email_address = email.val()
        username.val(email_address.slice(0, email_address.indexOf("@")))
    }
})

$("#password_confirm").on("blur", (e) => {
    var password_confirm = $(e.target)
    var password = $("#password")

})
