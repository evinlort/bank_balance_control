log = (to_log) => console.log(to_log);

capitalize_first_letter = (string) => string.charAt(0).toUpperCase() + string.slice(1)

var toastLiveExample = document.getElementById('liveToast')
var _toast = new bootstrap.Toast(toastLiveExample)

toast = (message, style, title) => {
    title = title !== undefined ? title : style
    $("#toast_message").text(message)
    $("#toast_title").text(capitalize_first_letter(title))
    $("#liveToast").addClass("bg-" + style)
    _toast.show()
}

toast_success = (message, title) => toast(message, "success", title)
toast_warning = (message, title) => toast(message, "warning", title)
toast_danger = (message, title) => toast(message, "danger", title)

disable_children_elements = (parent_element) => {
        for (const element of parent_element.children()) {
            var elem = $(element)
            elem.prop("disabled", true)
        }
    }

enable_children_elements = (parent_element) => {
    for (const element of parent_element.children()) {
        var elem = $(element)
        elem.prop("disabled", false)
    }
}