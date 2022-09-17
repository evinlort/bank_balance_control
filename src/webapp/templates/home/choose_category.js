$("#category_name").on("click", (e) => {
    $(e.target).select()
})

fill_categories = (callback=()=>{}) => {
    $.get("/api/categories", (data, status, xhr) => {
        var datalist = $("#categories-datalist")
        var cat_id = $("#category_id")
        datalist.html("")
        cat_id.val("")
        for (item of data) {
           var option = "<option value='" + capitalize_first_letter(item.name) + "' data-category-id='" + item.id + "'></option>"
           datalist.append(option)
        }
        callback()
    }, "json")
}

fill_categories(fill_means_of_payments())
