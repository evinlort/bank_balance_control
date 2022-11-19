$("#datepicker").datepicker({
    changeMonth: true,
    changeYear: true,
    minDate: -20,
    maxDate: "+0D",
    altField: "#date",
    altFormat: "yy-mm-dd",
    dateFormat: "dd/mm/yy"
}).datepicker('setDate', '+0d')

$("#means_of_payment").on("change", (e) => {
    var payments_div = $("#payments-div")
    var count = $("#payments_count")
    var first_payment = $("#preview_first_payment")
    var first_payment_label = $("#first_payment_label")
    var sum = $("#sum")
    count.val(1)

    var option = $(e.target).find("option:selected")
    if ($(option).data("paymentsEnabled")) {
            enable_children_elements(payments_div)
        }
        else {
            disable_children_elements(payments_div)
        }
    if (option.val() == "") {
        count.val("")
        first_payment.text("")
    }
    if (sum.val() > 0) {
        first_payment_label.removeClass("d-none")
        $.get("api/calculate/sum/" + sum.val() + "/payments/" + count.val() + "/first_payment", (data, textStatus, jqXHR) => {
            first_payment.text(data.first_payment)
        }, "json")
    }
    else {
        first_payment_label.addClass("d-none")
        first_payment.text("")
    }
})

$("#means_of_payment, #payments_count").on("blur", (e) => {
    var count = $("#payments_count")

    if(isNaN(count.val())) {
        count.val(1)
        count.focus()
    }
})

$("#confirm_payment").on("click", (e) => {
    var purchase_data = {
        sum: $("#sum").val(),
        category: $("#category_id").val(),
        means_of_payment: $("#means_of_payment>option:selected").val(),
        payments_count: $("#payments_count").val(),
        purchase_date: $("#date").val(),
        comment: $("#comment").val()
    }
    if (is_not_empty(purchase_data)) {
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
