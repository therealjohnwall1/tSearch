# tSearch 
Light weight search engine that includes scrapers, indexer, and ranker.
- Crawler: [Scrapy](https://github.com/scrapy/scrapy)
- indexer and ranker [Whoosh](https://github.com/mchaput/whoosh)

## Startup

#### run setup.sh
<pre>
chmod +x /setup.sh
./setup.sh
</pre>


#### build targets
<pre>
  python3 cmds/refreshlinks.py
</pre>
> **When scraping from urls, my rotating proxies are disabled by default, you can uncomment proxies in settings**
> **turn it on if you don't want to get ip banned, will get rotating api up soon
#### scrape from urls
<pre>
  python3 build.py
</pre>

#### search queries
<pre>
  python3 queryParser.py
</pre>





