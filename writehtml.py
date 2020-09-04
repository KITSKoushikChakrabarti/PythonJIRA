
# Developed by Koushik - Aug 2020
# Purpose: Create HTML files via Pyhton scripts

# See reference: https://stackoverflow.com/questions/16523939/how-to-write-and-save-html-file-in-python

# If File doesn't exist, it will create automatically
filename = 'C:\\PERSONAL\\' + 'testTables.html'

# Option 1 - create simple HTML file
Html_file= open(filename,"w")
html_str = """
<head>
<style type="text/css">
p {
  color: #FFFF88;
}
table {
  border-collapse: separate;
  border-spacing: 0;
  color: #888888;
  font: 14px/1.4 "Helvetica Neue", Helvetica, Arial, sans-serif;
}

th {
  background-color: #88FFFF;  
}
th,
td {
  padding: 10px 15px;
  vertical-align: middle;
  }
th:first-child {
  text-align: left;
}
tbody tr:nth-child(even) {
  background: #f0f0f2;
}
td {
  border-bottom: 1px solid #cecfd5;
  border-right: 1px solid #cecfd5;
}
td:first-child {
  border-left: 1px solid #cecfd5;
}
.book-title {
  color: #395870;
  display: block;
}
.item-stock,
.item-qty {
  text-align: center;
}
.item-price {
  text-align: right;
}
.item-multiple {
  display: block;
}
tfoot {
  text-align: right;
}
tfoot tr:last-child {
  background: #f0f0f2;
}
</style>
</head>
<body>
<table style="width:100%" border="1px" bordercolor="0088FF" >
  <caption>Design and Front-End Development Books</caption>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Marks</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
   <tr>
    <td>Rik</td>
    <td>Chakrabarti</td>
    <td>99</td>
  </tr>
   <tr>
    <td>Jack</td>
    <td>Junior</td>
    <td>98</td>
  </tr>
   <tr>
    <td>Cina</td>
    <td>Harris</td>
    <td>99</td>
  </tr>
</table>
</body>
"""
Html_file.write(html_str)
Html_file.close()


# Option 2

# colour = ["red", "red", "green", "yellow"]

# with open(filename, 'w') as myFile: # Will override existing content if file exists
#     myFile.write('<html>')
#     myFile.write('<body>')
#     myFile.write('<table>')

#     s = '1234567890'
#     for i in range(0, len(s), 60):
#         myFile.write('<tr><td>%04d</td></tr>' % (i+1))

#     for j, k in enumerate(s[i:i+60]):
#         myFile.write('<td><font style="background-color:%s;">%s<font></td>' % (colour[j %len(colour)], k))
    	
#     #myFile.write('</tr>')
#     myFile.write('</table>')
#     myFile.write('</body>')
#     myFile.write('</html>')

