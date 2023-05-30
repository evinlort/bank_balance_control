$("[id^=parent-collapse-purchase-]").each((index, element) => {
    $(element).on("click", () => {
        disable_other_collapses_except(index+1)
    })
})

disable_other_collapses_except = (index) => {
    $("[id^='collapse-purchase-'][id!='collapse-purchase-" + index + "']").each((index, element) => {
        $(element).collapse("hide")  // Hide all except the clicked collapse
    })
}
