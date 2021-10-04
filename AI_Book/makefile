book:
	jb build .

upload: book
	ghp-import -n -p -f ./_build/html

pdf: book
	jb build . --builder pdflatex
	#jb build . --builder pdfhtml

