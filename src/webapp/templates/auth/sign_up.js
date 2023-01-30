$("#day_of_birth_parsed").datepicker({
    changeMonth: true,
    changeYear: true,
    minDate: "-120Y",
    maxDate: "+0D",
    altField: "#day_of_birth",
    altFormat: "yy-mm-dd",
    dateFormat: "dd/mm/yy",
    yearRange: "c-120:c+0"
}).datepicker('setDate', '+0d')