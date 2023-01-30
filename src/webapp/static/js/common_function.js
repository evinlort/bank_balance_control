log = (to_log) => console.log(to_log);

capitalize_first_letter = (string) => string.charAt(0).toUpperCase() + string.slice(1)

var toastLiveExample = document.getElementById('liveToast')
var _toast = new bootstrap.Toast(toastLiveExample)

toast = (message, style, title, callback) => {
    if (typeof(title) === "function" && !callback) {
        callback = title
        title = null
    }
    title = title ? title : style
    $("#toast_message").text(message)
    $("#toast_title").text(capitalize_first_letter(title))
    $("#liveToast").addClass("bg-" + style)
    _toast.show()
    toastLiveExample.addEventListener('hide.bs.toast', () => $("#liveToast").removeClass("bg-" + style))

    if (typeof(callback) === "function") {
        toastLiveExample.addEventListener('hidden.bs.toast', () => callback(), {"once": true})
    }
}

toast_success = (message, title, callback) => toast(message, "success", title, callback)
toast_warning = (message, title, callback) => toast(message, "warning", title, callback)
toast_danger = (message, title, callback) => toast(message, "danger", title, callback)

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

validate_email = mail => {
    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,})+$/.test(mail)) {
        return true
    }
    return false
}

select_input = element => {
    element.select()
}

$.put = (url, data, callback, type) => {
    if ( $.isFunction(data) ){
        type = type || callback,
        callback = data,
        data = {}
    }

    return $.ajax({
        url: url,
        type: 'PUT',
        success: callback,
        data: data,
        contentType: type
    });
}

$.delete = (url, data, callback, type) => {
    if ( $.isFunction(data) ){
        type = type || callback,
        callback = data,
        data = {}
    }

    return $.ajax({
        url: url,
        type: 'DELETE',
        success: callback,
        data: data,
        contentType: type
    })
}

$.patch = (url, data, callback, type) => {
    if ( $.isFunction(data) ){
        type = type || callback,
        callback = data,
        data = {}
    }

    return $.ajax({
        url: url,
        type: 'PATCH',
        success: callback,
        data: data,
        contentType: type
    })
}