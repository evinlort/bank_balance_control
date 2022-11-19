$("#sum").on("keyup", (e) => {
    var sum = $("#sum")
    var first_payment = $("#preview_first_payment")
    var first_payment_label = $("#first_payment_label")

    if (isNaN(e.target.value)) {
        sum.val(sum.val().slice(0, -1))
    }
    else if (sum.val() === "00") {
        sum.val(sum.val().slice(0, -1))
    }
    else {
        if (sum.val().search(/\./) > 0 && sum.val().split(".")[1].length > 2) sum.val(sum.val().slice(0, -1))
    }

    if (sum.val().length > 1 && sum.val()[0] === "0") {
        sum.val(sum.val().slice(1))
    }

    if (sum.val() == "") {
        first_payment.text("")
        first_payment_label.addClass("d-none")
    }
    else {
        $.get("api/calculate/sum/" + sum.val() + "/payments/" + count.val() + "/first_payment", (data, textStatus, jqXHR) => {
            first_payment_label.removeClass("d-none")
            first_payment.text(data.first_payment)
        }, "json")
    }
})

$("#sum").focus()