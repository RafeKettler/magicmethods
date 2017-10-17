docs: index.html magicmethods.pdf clean

html: index.html

pdf: magicmethods.pdf 

index.html: table.markdown magicmethods.markdown appendix.markdown
	python magicmarkdown.py

magicmethods.pdf: magicmethods.tex
	pdflatex magicmethods.tex

clean:
	rm -f markedup.html magicmethods.log magicmethods.dvi magicmethods.aux
