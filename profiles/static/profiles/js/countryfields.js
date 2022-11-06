let countrySelected = document.querySelector('#id_default_country');
let countrySelectedVal = countrySelected.value;
!countrySelectedVal ? countrySelected.style.color = "#aab7c4" : ""
countrySelected.onchange = function(){
    countrySelectedVal = this.value;
    !countrySelectedVal ? this.style.color = "#aab7c4" : this.style.color = "#000"
}