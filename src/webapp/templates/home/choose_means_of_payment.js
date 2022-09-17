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

