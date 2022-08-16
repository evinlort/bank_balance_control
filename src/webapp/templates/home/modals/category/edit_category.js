$("#edit-category").on('shown.bs.modal', () => {
    $(this).find('#edit_category_name').focus();
})

$("#edit-category").on('hidden.bs.modal', () => {
    var subcat_name = $("#subcat_name")
    subcat_name.val("")
    subcat_name.addClass("d-none")
})

$("#show_add_subcat").on("click", (e) => {
    var subcat_name = $("#subcat_name")
    subcat_name.val("")

    if (! subcat_name.is(":visible")) {
        subcat_name.removeClass("d-none")
        subcat_name.focus()
    }
    else {
        subcat_name.addClass("d-none")
        subcat_name.blur()
    }
})