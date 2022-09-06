$("#datepicker").datepicker({
    changeMonth: true,
    changeYear: true,
    minDate: -20,
    maxDate: "+0D",
    altField: "#date",
    altFormat: "yy-mm-dd"
})

$("#category_name").on('input', () => {
    var cat_id_input = $("#category_id")
    var selectedValue = $(this).val()
    var balance = $("#category-balance-text")
    var options = $('#categories-datalist>option')

    if (selectedValue == "") {
        balance.addClass("d-none")
        return false
    }

    cat_id_input.val("")

    options.each((option) => {
        value = options[option]
        if ($(value).val() == selectedValue) {
            var category_id = $(value).data("categoryId")
            balance.removeClass("d-none")
            balance.addClass("d-block")
            return false
        }
        else {
            balance.addClass("d-none")

        }
    })

    cat_id_input.val(category_id)
});

$("#means_of_payment").on("change", (e) => {
    var payments_div = $("#payments-div")
    var count = $("#payments_count")
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
    }
})

$(document).on("click", "#payments_add, #payments_subtract", (e) => {
    var count = $("#payments_count")
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
})

$("#sum").on("keyup", (e) => {
    var sum = $("#sum")
    if (isNaN(e.target.value)) {
        sum.val(sum.val().slice(0, -1))
    }
    else {
        if (sum.val().search(/\./) > 0 && sum.val().split(".")[1].length > 2) sum.val(sum.val().slice(0, -1))
    }
})

disable_children_elements($("#payments-div"))
let option = $("#means_of_payment").find("option:selected")
let count = $("#payments_count")
if (option.val() == "") {
    count.val("")
}
