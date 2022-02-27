subfinder -d whitehatjr.com| httpx -ip -web-server -title -status-code -cname -no-color| tr -d "]" | awk -F "[" 'BEGIN{ print "\
<style style='text/css'> \
.hoverTable{ width:100%\; border-collapse:collapse\; } \
.hoverTable td{ padding:7px\; border:#0e7094 1px solid\; } \
.hoverTable tr{ background: white\; } \
.hoverTable tr:hover { background-color: #ffff99\; } \
</style>\
<table class='hoverTable' style='width:100%\;border-color:#0e7094\;border-collapse:collapse' border='2'><tbody>\
<tr>\
<th style='background-color:#0e7094\;color:white' scope='row'>S.No</th>\
<th style='background-color:#0e7094\;color:white' scope='row'>Subdomain</th>\
<th  style='background-color:#0e7094\;color:white' scope='row'>IP Address</th>\
<th  style='background-color:#0e7094\;color:white' scope='row'>Web Server</th>\
<th  style='background-color:#0e7094\;color:white' scope='row'>C-Name</th>\
<th  style='background-color:#0e7094\;color:white' scope='row'>Title</th>\
<th  style='background-color:#0e7094\;color:white' scope='row'>Status Code</th>\
</tr>\
"\
}{\
s1 = "<tr><td style='background-color:#F8FEFF\;color:#0e7094'>"NR"</td>"; \
c1 = "<td>"$1"</td>"; \
c2 = "<td>"$2"</td></tr>";\
c3 = "<td>"$3"</td>";\
c4 = "<td>"$4"</td>";\
c5 = "<td>"$5"</td>";\
c6 = "<td>"$6"</td>";\

print s1 c1 c5 c4 c6 c3 c2}END \
{printf "</tr></tbody></table>"}'
