var add_cat_modal = new bootstrap.Modal(document.getElementById('modal_add_new_category'), {
        keyboard: true
    })

$("#add_new_category").on("click", (e) => {
    add_cat_modal.show()
})