all: thesis.pdf

clean:
	rm -fr *.aux *.bbl *.blg *.dep *.fdb_latexmk *.fls *.lof *.log *.lot *.pdf *.toc

deploy: dist/.git/config all
	ln -f thesis.pdf dist
	cd dist && \
	git add -A && \
	git commit --amend -q -m Autogenerated && \
	git push -f origin master:gh-pages

dist/.git/config:
	mkdir -p $(@D)
	url=`git remote -v | grep origin | awk '{ printf "%s", $$2; exit }'` && \
	cd $(@D)/.. && \
	git init && \
	git config user.name Bot && \
	git config user.email "<>" && \
	git commit -m _ --allow-empty && \
	git remote add origin "$$url"

.PHONY: all clean deploy

.SUFFIXES: .pdf .tex

.tex.pdf:
	latexmk -f -g -pdf -interaction=nonstopmode -M -MP -MF $*.dep -outdir=$(@D) $<

-include thesis.dep