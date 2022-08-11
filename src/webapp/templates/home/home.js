$("#datepicker").datepicker({
    changeMonth: true,
    changeYear: true,
    minDate: -20,
    maxDate: "+0D",
    altField: "#date",
    altFormat: "yy-mm-dd"
})

$("#category").on('input', function (){
    var selectedValue = $(this).val();
    var options = $('#categories-datalist>option')

    for (const [key, value] of Object.entries(options)) {
        if ($(value).val() == selectedValue) {
            var category_id = $(options[key]).data("categoryId")
            break
        }
    }
    log(category_id)
});
