function loadDoc() {
  var xhttp = new XMLHttpRequest(),
  		method = "POST",
  		url="http://127.0.0.1:8100/Aerie/api/createAccount"
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "ajax_info.txt", true);
  xhttp.send();
}