
$("#modal_add_new_category").on("shown.bs.modal", () => {
    $("#add_category_name").focus()
})

$("#modal_add_new_category").on("show.bs.modal", () => {
    var languages = $("#new_cat_languages")
    $.get("/api/languages", data => {
        languages.empty()
        for (item of data) {
            let selected = item.default ? "selected" : ""
            var option = "<option value='" + item.id + "' " + selected + ">" + capitalize_first_letter(item.name) + "</option>"
            languages.append(option)
        }
    })
})

$("#modal_add_new_category_button").on("click", e => {
    var lang_id = $("#new_cat_languages").val()
    var new_cat = $("#add_category_name")

    if (new_cat.val() == "") {
        new_cat.focus()
        return false
    }

    var data = {"category_name": new_cat.val(), "language_id": lang_id}

    $.post("/api/category", data, response => {
        if (response === true) {
            add_cat_modal.hide()
        }
        else {
            toast_danger("Please, provide category name!", "No category")
        }
    })
})