function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       //document.getElementById("demo").innerHTML = this.responseText;
      window.location.href = "http://127.0.0.1:1134/Aerie/createAccount";
    }
  };
  xhttp.open("GET", "http://127.0.0.1:1134/Aerie/createAccount", true);
  xhttp.send();
}