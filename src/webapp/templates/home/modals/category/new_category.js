
$("#modal_add_new_category").on("shown.bs.modal", () => {
    $("#add_category_name").val("")
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
    var new_cat = $("#add_category_name")

    if (new_cat.val() == "") {
        new_cat.focus()
        return false
    }

    var data = {"category_name": new_cat.val()}
    var set_cat_id = () => {
        var cat_name_new = $("#add_category_name")
        $("#category_id").val(
            $("#categories-datalist>option").toArray().map(
                e=>$(e)
            ).filter(
                e=>e.val()==cat_name_new.val()
            )[0].data("categoryId")
        )
    }
    $.post("/api/category", data, response => {
        log(typeof(response.new_id))
        if (response.new_id > 0) {
            fill_categories(set_cat_id)
            $("#category_name").val(new_cat.val())
            add_cat_modal.hide()
        }
        else if(response.new_id == -1) {
            $("#add_category_name").focus()
            toast_warning("This category name is already exists!", "Name duplication")
        }
        else {
            toast_danger("Please, provide category name!", "No category")
        }
    })
})