cat filo.txt| tr -d "]" | awk -F "[" 'BEGIN{ print "\
<style style='text/css'> \
.hoverTable{ width:100%\; border-collapse:collapse\; } \
.hoverTable td{ padding:7px\; border:#0e7094 1px solid\; } \
.hoverTable tr{ background: white\; } \
.hoverTable tr:hover { background-color: #ffff99\; } \
#myInput {\
  background-position: 10px 10px\;\
  background-repeat: no-repeat\;\
  width: 25%\;\
  color: #0e7094\;\
  font-size: 16px\;\
  padding: 12px 20px 12px 40px\;\
  border: 3px solid #0e7094\;\
  border-radius: 25px\;\
  margin-bottom: 12px\;\}\
#resultsx \{\
  border-radius: 25px\;\
  background: #73AD21\;\
  padding: 20px\;\
  width: 200px\;\
  height: 150px\; \}\
  color: #0e7094\; \}\
 #countx \{\
  border-radius: 25px\;\
  background: yellow\;\
  padding: 20px\;\
  width: 200px\;\
  height: 150px\; \}\
</style>\
<input type=\"text\" id=\"myInput\" onkeyup='myFunction\(\)' placeholder=\"Search Here\">\
<a>&emsp;</a>\
<a style=\"color:#0e7094\;\ font-weight: bold\; font-size: large;\"  id=\"totalRows\"></a>\
<a style=\"color:#0e7094\;\ font-weight: bold\; font-size: large;\"  id=\"rowCount\"></a>\
<a>&emsp;</a>\
<a style=\"color:#0e7094\;\ font-weight: bold\; font-size: large;\"  id=\"results\"></a>\
<a style=\"color:#0e7094\;\ font-weight: bold\; font-size: large;\"  id=\"resultCount\"></a>\
<table id=\"myTable\" class=\"hoverTable\" style='width:100%\;border-color:#0e7094\;border-collapse:collapse' border='2'><tbody>\
<tr>\
<th style='height:8px\;width:3%\;background-color:#0e7094\;color:white' scope='row'>S.No</th>\
<th style='width:18%\;background-color:#0e7094\;color:white' scope='row'>Subdomain</th>\
<th  style='width:7%\;background-color:#0e7094\;color:white' scope='row'>IP Address</th>\
<th  style='width:7%\;background-color:#0e7094\;color:white' scope='row'>Web Server</th>\
<th  style='width:30%\;background-color:#0e7094\;color:white' scope='row'>C-Name</th>\
<th  style='width:30%\;background-color:#0e7094\;color:white' scope='row'>Title</th>\
<th  style='width:10%\;background-color:#0e7094\;color:white' scope='row'>Status Code</th>\
</tr>\
"\
}{\
s1 = "<tr><td style='background-color:#F8FEFF\;color:#0e7094'>"NR"</td>"; \
c1 = "<td><a style=\"text-decoration:none\;color:blue\" href="$1"target=\"_blank\">"$1"</a></td>"; \
c2 = "<td>"$2"</td></tr>";\
c3 = "<td>"$3"</td>";\
c4 = "<td>"$4"</td>";\
c5 = "<td>"$5"</td>";\
c6 = "<td>"$6"</td>";\
print s1 c1 c5 c4 c6 c3 c2}END \
\
\
\
{print "</tr></tbody></table>\
<script>\
 function myFunction\(\) \{\
 const rowCountSet = new Set\(\)\;\
  var input, filter, table, tr, th, td, i\;\
  input = document.getElementById\(\"myInput\"\)\;\
  filter = input.value.toUpperCase\(\)\;\
  table = document.getElementById\(\"myTable\"\)\;\
  var totalResults = 0\;\
  var rows = table.getElementsByTagName\(\"tr\"\)\;\
  for \(i = 0; i < rows.length; i++\) \{\
  	rowCount++\;\
    var cells = rows[i].getElementsByTagName\(\"td\"\)\;\
    var j\;\
    const myArr = [];\
    var rowContainsFilter = false\;\
    for \(j = 0\; j < cells.length\; j++\) \{\
      if \(cells[j]\) \{\
        if \(cells[j].innerHTML.toUpperCase\(\).indexOf\(filter\) > -1\) \{\
          rowCountSet.add\(i)\;\
          rowContainsFilter = true\;\
          totalResults++\;\
          myArr.push\(i\) \;\
          continue\;\
        \}\
      \}\
    \}\
    if \(! rowContainsFilter\) \{\
      rows[i].style.display = \"none\"\;\
          rows[0].style.display = \"\"\;\
    \} else \{\
      rows[i].style.display = \"\"\;\
           rows[0].style.display = \"\"\;\
            \}\}\
                       document.getElementById(\"rowCount\").innerHTML = rowCountSet.size\;\
                       document.getElementById(\"totalRows\").innerHTML = \"Rows: \"\;\
                       document.getElementById(\"resultCount\").innerHTML = totalResults\;\
                       document.getElementById(\"results\").innerHTML = \"Results: \"\;\
            \}\
</script>\
\
\
\
"}'
