$("#datepicker").datepicker({
    changeMonth: true,
    changeYear: true,
    minDate: -31,
    maxDate: "+0D",
    altField: "#date",
    altFormat: "yy-mm-dd",
    dateFormat: "dd/mm/yy"
}).datepicker('setDate', '+0d')