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

$("#category_name").on("click", (e) => {
    $(e.target).select()
})

$("#category_name").on('input change', (e) => {
    var cat_id_input = $("#category_id")
    var selectedValue = $(e.target).val()
    var balance = $("#category-balance-text")
    var options = $('#categories-datalist>option')

    if (selectedValue == "") {
        balance.addClass("d-none")
        return false
    }

    cat_id_input.val("")
    var category_id = 0

    options.each((option) => {
        let value = options[option]
        if ($(value).val() == selectedValue) {
            category_id = $(value).data("categoryId")
            balance.removeClass("d-none")
            balance.addClass("d-block")
            return
        }
        else {
            balance.addClass("d-none")

        }
    })

    cat_id_input.val(category_id)
})
