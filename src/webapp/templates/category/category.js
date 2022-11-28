$(".save_edited_category").on("click", e => {
    $(e.target).parent().parent().find("div").each((i, elem) => {
        log($(elem).find("input").val())
    })
})