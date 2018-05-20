# TPB-scraper
A python scraper for The Pirate Bay

Interactive:
```bash
archie@archlinux ~/code/TPB-scraper master $ ./TPB_scraper

search term :  Avengers

Index  Seeders  Leachers Ratio    Title
1        7817    1965    4.0      Avengers Infinity War 2018 NEW PROPER 720p HD-CAM X264 HQ-CPG
2        3021    836     3.6      Avengers Infinity War 2018 720p TS x264 AAC TiTAN
3        3003    643     4.7      Avengers: Age of Ultron (2015) 1080p BrRip x264 - YIFY
4        2121    426     5.0      The Avengers 2012 720p BRrip X264 - 1GB - YIFY
5        814     73      11.2     Avengers.Infinity War.2018.720p.TS.1xBet

input command :  transmission: 1 2

uploading magnet link(s) to transmission

...done

archie@archlinux ~/code/TPB-scraper master $
```

Also takes single-line commands for easier scripting:
```bash
TPB_scraper --search Some Search --print --magnets --results 1 2 3 4 5 >> somefile.txt
```
Prints the details and magnet links of the first five search results to somefile.txt.
I plan on using this fucntionality to make a series of automation scripts in the future.

# Future Development
Make a cron script to Download information on the top 100 torrents every 12 hours.

    -generate results from multiple pages
  
    -add more freedom to customize URL beyond search-terms, including 'top' pages

Add more fields including; user, date, and filesize.

Make a algorythmn to suggest the best downloads based on filesize, ratio, and seeders

Add error support and error codes


