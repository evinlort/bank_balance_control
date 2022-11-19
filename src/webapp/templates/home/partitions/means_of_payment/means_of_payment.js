fill_means_of_payments = (callback=()=>{}) => {
    $.get("/api/means_of_payments", (data, status, xhr) => {
        var select_elem = $("#means_of_payment")
        for (item of data) {
           var option = "<option value='" + item.id + "' data-payments-enabled='" + item.allow_payments + "'>" + item.display_name + "</option>"
           select_elem.append(option)
        }
        callback()
    }, "json")
}

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

fill_categories(fill_means_of_payments())
