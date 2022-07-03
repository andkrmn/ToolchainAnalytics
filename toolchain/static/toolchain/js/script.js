// function loadTable(e) {
//   document.getElementById("tester").innerHTML = e;
// }

var loadtable = function (link) {
    clicked_table = link.innerHTML;
    document.getElementById("tablename").innerHTML = clicked_table;
    clicked_table_clean = clicked_table.replace(/\s+/g, '');
    for (const table of document.getElementsByClassName("table")) {
        table.style.display = "none"
    }
    document.getElementById(clicked_table_clean).style.display = "block"
    document.getElementById("buttoncontainer").style.display = "block"
    link = "/preprocessing/" + clicked_table_clean
    document.getElementById("B1").setAttribute("formaction", link)
};

function updateTextInput(val) {
          document.getElementById('value').value=val;
          document.getElementById("value2").value=100-val;
        }



