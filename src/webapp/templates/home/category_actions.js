$("#add_new_category").on("click", (e) => {
//    var category_name = $("#category_name")
//    if (category_name.val() == "") {
        var new_cat = new bootstrap.Modal(document.getElementById('modal_add_new_category'), {
            keyboard: true
        })
        new_cat.toggle()
//    }
//    else {
//        var edit_cat = new bootstrap.Modal(document.getElementById('edit-category'), {
//            keyboard: true
//        })
//        var edit_cat_input = $("#edit_category_name")
//        edit_cat_input.val(category_name.val())
//        edit_cat.toggle()
//    }
})