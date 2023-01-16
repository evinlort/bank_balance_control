$("#confirm_payment").on("click", (e) => {
    var button = $(e.target)
    var purchase_data = {
        sum: $("#sum").val(),
        category: $("#category_id").val(),
        means_of_payment: $("#means_of_payment>option:selected").val(),
        payments_count: $("#payments_count").val(),
        purchase_date: $("#date").val(),
        comment: $("#comment").val()
    }
    if (is_not_empty(purchase_data)) {
        button.addClass("disabled")

        $.post("api/purchase", purchase_data, response => {
            $("#sum").val("")
            $("#category_name").val("")
            $("#category_id").val("")
            $("#category-balance-text").addClass("d-none")
            $("#means_of_payment").val("")
            $("#first_payment_label").addClass("d-none")
            $("#preview_first_payment").text("")
            $("#payments_count").val("")
            disable_children_elements($("#payments-div"))
            $("#date").val("")
            $("#datepicker").datepicker("setDate", '+0d')
            $("#comment").val("")
            toast_success("Purchase successfully saved", "Payment saved")

            button.removeClass("disabled")
        }, "json")
    }
})

is_not_empty = data => {
    for (key in data) {
        if (data[key] == "") return false
    }
    return true
}

disable_children_elements($("#payments-div"))
let option = $("#means_of_payment").find("option:selected")
let count = $("#payments_count")
if (option.val() == "") {
    count.val("")
}
