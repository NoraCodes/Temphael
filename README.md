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
13:03:39: leo [~/Projects/genevabot]
$ ./tscrape.py clientsfromhell 1 10 --notags
Scraping page 1
[...]
Scraping page 10
Generating database...
Dumping database to clientsfromhell.posts.markov

13:03:59: leo [~/Projects/genevabot]
$ ./genevabot.py clientsfromhell.posts.markov 10
Perfect for everything from invitations to logos, the 35+ unique fonts – for example, an idea
logo, and brand image for my sister’s cake
It’s a Samsung iPhone
Me: I removed all the details
do it for free, and still
By making it easy to make bold and professional designs,
Thanks for the time to actually review said contract, I was
After this phone call, I received some revisions from said customer that came in to work with us can pay our full fees and is standard across
I sent it over – along with a
What will we do
```