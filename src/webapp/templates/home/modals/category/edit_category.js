$("#edit_existing_category").on('shown.bs.modal', () => {
    $(this).find('#edit_category_name').focus();
})

$("#edit_existing_category").on('hidden.bs.modal', () => {
    var subcat_name = $("#subcat_name")
    subcat_name.val("")
    subcat_name.addClass("d-none")
})

$("#show_add_subcat").on("click", (e) => {
    var subcat_name = $("#subcat_name")
    var edit_category_button = $("#edit_category_button")
    subcat_name.val("")

    if (! subcat_name.is(":visible")) {
        subcat_name.removeClass("d-none")
        subcat_name.focus()
        edit_category_button.text("Add new sub category")
    }
    else {
        subcat_name.addClass("d-none")
        subcat_name.blur()
        edit_category_button.text("Edit category")
    }
})