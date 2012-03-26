docs: magicmethods.html magicmethods.pdf clean

html: magicmethods.html

pdf: magicmethods.pdf 

magicmethods.html: table.markdown magicmethods.markdown appendix.markdown
	python magicmarkdown.py

magicmethods.pdf: magicmethods.tex
	pdflatex magicmethods.tex

clean:
	rm -f markedup.html magicmethods.log magicmethods.dvi magicmethods.aux
