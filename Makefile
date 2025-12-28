PELICAN?=pelican
PELICANOPTS=-D

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

serve:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

# https://docs.getpelican.com/en/latest/tips.html#user-pages
publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
	ghp-import $(OUTPUTDIR) -b gh-pages
	git fetch origin
	@if [ -z "$$(git branch --list gh-pages)" ]; then git checkout -b gh-pages origin/gh-pages; else git checkout gh-pages; fi
	git rebase origin/gh-pages
	git push origin gh-pages:gh-pages

.PHONY: html clean serve publish
