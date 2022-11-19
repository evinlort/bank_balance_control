$("#edit_existing_category").on('shown.bs.modal', () => {
    $(this).find('#edit_category_name').focus();
})

$("#edit_category_button").on("click", e => {
    var cat_name_edit = $("#edit_category_name")
    var id = $("#category_id").val()

    if (cat_name_edit.val() == "") {
        cat_name_edit.focus()
        toast_warning("Can't update with empty name! Please fill it")
        return false
    }

    var data = {"category_name": cat_name_edit.val()}
    var set_cat_id = () => {
        var cat_name_edit = $("#edit_category_name")
        $("#category_id").val(
            $("#categories-datalist>option").toArray().map(
                e=>$(e)
            ).filter(
                e=>e.val()==cat_name_edit.val()
            )[0].data("categoryId")
        )
    }
    $.patch("/api/category/" + id, JSON.stringify(data), response => {
        if (response.updated_id !== 0) {
            fill_categories(set_cat_id)
            $("#category_name").val(cat_name_edit.val())
            edit_cat_modal.hide()
        }
        else {
            toast_danger("Please, provide category name!", "No category")
        }
    }, "application/json")
})