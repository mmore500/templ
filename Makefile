out:
		mkdir $@
		mkdir $@/blog
		mkdir $@/class
		mkdir $@/paper
		mkdir $@/talk
		mkdir $@/meet

out/%.pdf: out
	pandoc "$*".md -o "$@"

out/%.html: out
	pandoc "$*".md -o "$@"

out/%.doc: out
	pandoc "$*".md -o "$@"

clean:
		rm -rf out
