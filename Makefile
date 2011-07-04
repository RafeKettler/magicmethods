docs: magicmethods.html magicmethods.pdf clean

html: magicmethods.html

pdf: magicmethods.pdf 

magicmethods.html: markedup.html
	cat header.html markedup.html footer.html > magicmethods.html

markedup.html: table.markdown magicmethods.markdown table.markdown
	python magicmarkdown.py

magicmethods.pdf: magicmethods.tex
	pdflatex magicmethods.tex

clean:
	rm -f markedup.html magicmethods.log magicmethods.dvi magicmethods.aux
