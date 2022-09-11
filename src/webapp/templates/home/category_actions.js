var add_cat_modal = new bootstrap.Modal(document.getElementById('modal_add_new_category'), {
        keyboard: true
    })
var edit_cat_modal = new bootstrap.Modal(document.getElementById('edit_existing_category'), {
        keyboard: true
    })

$("#add_new_category").on("click", (e) => {
    var category_name = $("#category_name")
    if (category_name.val() != "" && $("#categories-datalist>option").toArray().map(e => $(e).val()).includes(category_name.val())) {
        let edit_category_name = $("#edit_category_name")
        edit_category_name.val(category_name.val())
        edit_cat_modal.show()
    }
    else {
        add_cat_modal.show()
    }
})