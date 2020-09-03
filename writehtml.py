
# Developed by Koushik - Aug 2020
# Purpose: Create HTML files via Pyhton scripts

# See reference: https://stackoverflow.com/questions/16523939/how-to-write-and-save-html-file-in-python

# If File doesn't exist, it will create automatically
filename = 'C:\\PERSONAL\\' + 'testTables.html'

# Option 1 - create simple HTML file
# Html_file= open(filename,"w")
# html_str = """
# <table border=1>
#      <tr>
#        <th>Number</th>
#        <th>Square</th>
#      </tr>
#      <indent>
#      <% for i in range(10): %>
#        <tr>
#          <td><%= i %></td>
#          <td><%= i**2 %></td>
#        </tr>
#      </indent>
# </table>
# """
# Html_file.write(html_str)
# Html_file.close()


# Option 2

colour = ["red", "red", "green", "yellow"]

with open(filename, 'w') as myFile: # Will override existing content if file exists
    myFile.write('<html>')
    myFile.write('<body>')
    myFile.write('<table>')

    s = '1234567890'
    for i in range(0, len(s), 60):
        myFile.write('<tr><td>%04d</td></tr>' % (i+1))

    for j, k in enumerate(s[i:i+60]):
        myFile.write('<td><font style="background-color:%s;">%s<font></td>' % (colour[j %len(colour)], k))
    	
    #myFile.write('</tr>')
    myFile.write('</table>')
    myFile.write('</body>')
    myFile.write('</html>')

