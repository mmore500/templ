pr:
		pandoc -o pr-out.pdf $$(templ pr)

je:
		pandoc -o je-out.pdf $$(templ je)

clean:
		rm -rf *out.pdf
