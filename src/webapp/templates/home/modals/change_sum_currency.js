$('#change-sum-currency').on('shown.bs.modal', function () {
    $.get("/api/currencies", (data, textStatus, jqXHR) => {
        var datalist = $("#currencies-datalist")
        for (item of data) {
           var option = "<option value='" + item.code + "' data-currency-id='" + item.id + "'></option>"
           datalist.append(option)
        }
    }, "json")
});

$("#currency_name").on("input", (e) => {
    var curr_id_input = $("#currency_id")
    var selectedValue = $(e.target ).val()
    var options = $('#currencies-datalist>option')
    curr_id_input.val("")

    options.each((option) => {
        value = options[option]
        if ($(value).val() == selectedValue) {
            var currency_id = $(value).data("currencyId")
            curr_id_input.val(currency_id)
            return true
        }
    })
})

$("#change-sum-currency-button").on("click", () => {
    var selected_currency_id = $("#currency_id").val()
    $.get("/api/currency/" + selected_currency_id + "/sign", data => {
        log(data)
    }, "json")
})