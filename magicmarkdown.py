# magicmarkdown.py
# utility script for changing markdown from magic methods guide into HTML

import markdown

mkd = open('magicmethods.mkd', 'r')
text = mkd.read()
mkd.close()
mkd2 = open('appendix.mkd', 'r')
text2 = mkd2.read()
mkd2.close()
html = markdown.markdown(text, 
                         ['def_list', 'codehilite'])
appendix = markdown.markdown(text2, ['tables'])
out = open('markedup.html', 'w')
out.write(html)
out.write(appendix)
out.close()