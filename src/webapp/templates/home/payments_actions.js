$(document).on("click", "#payments_add, #payments_subtract", (e) => {
    var count = $("#payments_count")
    var first_payment = $("#preview_first_payment")
    var sum = $("#sum")

    if(isNaN(count.val())) {
        count.val(1)
        return false
    }
    var id_array = $(e.target).prop("id").split("_")
    var action = id_array[id_array.length - 1].toLowerCase()
    if (action == "add") {
        count.val(parseInt(count.val()) + 1)
    }
    else {
        if (parseInt(count.val()) > 1) {
            count.val(parseInt(count.val()) - 1)
        }
    }
    if (sum.val() > 0) {
        $.get("api/calculate/sum/" + sum.val() + "/payments/" + count.val() + "/first_payment", (data, textStatus, jqXHR) => {
            first_payment.text(data.first_payment)
        }, "json")
    }
})