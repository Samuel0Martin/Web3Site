var countries = {
  "can":{
    "name":"Canada",
    "population":"36,000,000"    
  },
  "nz":{
    "name":"New Zealand",
    "population":"4,000,000"
  },
  "usa":{
    "name":"United States of America",
    "population":"325,000,000"
  }
}

$("select").on("change", function(){    
  var val = $(this).val();  
  var country = countries[val];
  $("#name").html(country.name);
  $("#population").html(country.population);
});