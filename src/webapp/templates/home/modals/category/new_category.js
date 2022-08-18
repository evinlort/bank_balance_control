$("#add-new-category").on("shown.bs.modal", () => {
    $("#add_category_name").focus()
})

$("#add-new-category").on("show.bs.modal", () => {
    var languages = $("#new_cat_languages")
    $.get("/api/languages", data => {
        languages.empty()
        for (item of data) {
            let selected = item.default ? "selected" : ""
            var option = "<option value='" + item.id + "' " + selected + ">" + capitalize_first_letter(item.name) + "</option>"
            languages.append(option)
        }
    })
})