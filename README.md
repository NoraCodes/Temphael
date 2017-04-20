# Geneva Bot

Scrape Tumblr blogs for a corpus, convert it into a Markov probablility matrix,
and generate text posts in the style of the original blog.

This process consists of two scripts, `tscrape.py` and `genevabot.py`. The
first scrapes a Tumblr blog for text and tags (because lots of great content is
included in Tumblr tags!) and creates a PyMarkovChain probability database from
that data. The second simply reconsititues the probability database into memory
and generates some sentances from it.

Here is a sample usage:

```
12:22:03: leo [~/Projects/genevabot]
$ ./tscrape.py 
usage: tscrape.py [-h] [--tag TAG] [--debug DEBUG] URL START_PAGE END_PAGE
tscrape.py: error: the following arguments are required: URL, START_PAGE, END_PAGE

12:22:04: leo [~/Projects/genevabot]
$ ./tscrape.py toasted-pearls --tag "toasty posties" 1 5
Scraping page 1
Scraping page 2
Scraping page 3
Scraping page 4
Scraping page 5
Generating database...
Dumping database to toasted-pearls.toasty%20posties.markov

12:22:23: leo [~/Projects/genevabot]
$ ./
genevabot.py  .git/         tscrape.py    .vscode/      

12:22:23: leo [~/Projects/genevabot]
$ ./genevabot.py 
USAGE: genevabot.py CORPUS NUMBER                            

12:22:37: leo [~/Projects/genevabot]
$ ./genevabot.py toasted-pearls.toasty%20posties.markov 3
It’s cool
No offense but like how does anyone else remember that episode where we learned that Wander was a unicorn
I love ✩ when people joke about infidelity ✩
```