$(".save_edited_category").on("click", e => {
    var start_point = $(e.target).parent().parent()
    var inputs_array = $(e.target).parent().parent().find("div").find("input")
    var category_id = $(inputs_array[0]).val()
    var category_name = $(inputs_array[1]).val()
    var category_balance = $(inputs_array[2]).val()

    if ($(inputs_array[1]).val().replace(/\s/g, "") === "") {
        reload_cat_name(start_point, $(inputs_array[1]))
        return false
    }

    $.patch(
        "/api/category/" + category_id,
        JSON.stringify({"category_name": category_name, "category_balance": category_balance}),
        response => {
            if (response.updated_id !== 0) {
                toast_success("Category updated")
            }
            else {
                toast_danger("Please, provide category name!", "No category")
            }
        }, "application/json"
    )
})

reload_cat_name = (start_point, cat_name_element) => {
    var category_id = $(start_point.find("input")[0]).val()
    $.get("/api/category/" + category_id, data => {
        cat_name_element.val(data.category.name)
    })
}