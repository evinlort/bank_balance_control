$(".save_edited_category").on("click", e => {
    var start_point = $(e.target).parent().parent()
    var inputs_array = $(e.target).parent().parent().find("div").find("input")
    var category_name = $(inputs_array[0]).val()
    var category_balance = $(inputs_array[1]).val()

    if ($(inputs_array[0]).val().replace(/\s/g, "") === "") {
        reload_cat_name(start_point, $(inputs_array[0]))
        return false
    }


    log(category_name)
    log(category_balance)
})

reload_cat_name = (start_point, cat_name_element) => {
    var category_id = $(start_point.find("input")[0]).val()
    $.get("/api/category/" + category_id, data => {
        cat_name_element.val(data.category.name)
    })
}