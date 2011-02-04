# magicmarkdown.py
# utility script for changing markdown from magic methods guide into HTML

import markdown

table = open('table.mkd').read()
body = open('magicmethods.mkd').read()
appendix = open('appendix.mkd').read()

table_text = markdown.markdown(table)
body_text = markdown.markdown(body, 
                         ['def_list', 'codehilite'])
appendix_text = markdown.markdown(appendix, ['tables'])

with open('markedup.html', 'w') as out:
    out.write(table_text)
    out.write(body_text)
    out.write(appendix_text)
