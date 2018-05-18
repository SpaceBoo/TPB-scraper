# TPB-scraper
A python scraper for The Pirate Bay

Interactive:

Also takes single-line commands for easier scripting:
```bash
TPB_scraper -s Some Search --print --magnets --results 1 2 3 4 5 >> somefile.txt
```
Prints the details and magnet links of the first five search results to somefile.txt
I plan on using this to make a series of automation scripts in the future.

# Future Development
Make a cron script to Download information on the top 100 torrents every 12 hours.
  -generate results from multiple pages
  -add more freedom to customize URL beyond search-terms, including 'top' pages
Add more fields including; user, date, and filesize.
Make a algorythmn to suggest the best downloads based on filesize, ratio, and seeders
Add error support and error codes


