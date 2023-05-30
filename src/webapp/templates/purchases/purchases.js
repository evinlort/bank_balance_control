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

$("#show_for_user").on("change", (e) => {
    var user_id = isNaN(e.target.value)?0:e.target.value
    var year = $("#selected_month_year").text().split(" ")[1]
    var month = $("#month_number").text()

    var url = "purchases/user/"+user_id+"/month/"+month+"/year/"+year

    // TODO: Get data and reload purchases div or reload the page with the UPL
//    if(user_id != 0) {
//        $("[id^=parent-collapse-purchase-").each((index, element) => {
//            if($(element).find(".member_id")[0].innerText != user_id)
//                $(element).hide()
//        })
//    }
})
