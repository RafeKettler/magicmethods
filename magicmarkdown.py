# magicmarkdown.py
# utility script for changing markdown from magic methods guide into HTML

import markdown

mkd = open('magicmethods.mkd', 'r')
text = mkd.read()
html = markdown.markdown(text, 
                         ['def_list', 'codehilite'])
out = open('markedup.html', 'w')
out.write(html)