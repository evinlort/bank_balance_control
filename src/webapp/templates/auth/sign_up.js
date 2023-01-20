$("#day_of_birth_parsed").datepicker({
    changeMonth: true,
    changeYear: true,
    minDate: -31,
    maxDate: "+0D",
    altField: "#day_of_birth",
    altFormat: "yy-mm-dd",
    dateFormat: "dd/mm/yy"
}).datepicker('setDate', '+0d')