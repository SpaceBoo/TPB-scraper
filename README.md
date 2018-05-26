# TPB-scraper
A simple python scraper which uses beautiful soup to parse and return data from The PirateBay. Output can be piped, re-directed, or passed directly to transmission-cli for easy download. TPB-scraper takes a wide range of arguments and can function both interactively for convience and directly; using single line commands for easy automation and scripting.

An example of an interactive session, ideal for headless torrent-boxes without graphical support:
```bash
archie@archlinux ~/code/TPB-scraper master $ ./TPB_scraper
Please enter a search term :  Avengers
Index  Seeders  Leachers Ratio    Title
1        7817    1965    4.0      Avengers Infinity War 2018 NEW PROPER 720p HD-CAM X264 HQ-CPG
2        3021    836     3.6      Avengers Infinity War 2018 720p TS x264 AAC TiTAN
3        3003    643     4.7      Avengers: Age of Ultron (2015) 1080p BrRip x264 - YIFY
4        2121    426     5.0      The Avengers 2012 720p BRrip X264 - 1GB - YIFY
5        814     73      11.2     Avengers.Infinity War.2018.720p.TS.1xBet
issue command 'print' or 'transmission' followed the media you wish to act upon
command  : transmission 2 
uploading  Avengers Infinity War 2018 720p TS x264 AAC TiTAN (index:2)  magnet  to transmission
...done
archie@archlinux ~/code/TPB-scraper master $
```

An example of a scripting/automation data-collection project: 
```bash
TPB_scraper --top --print --range 1 100
```
This command writes the details of the top 100 torrents to a file. Output is tab-delimited with one entry per line, ideal for importing into a database.
```bash
0 12 * * * TPB_scraper --top --print  --range 1 100 > ~/TPBS/Data_Files/$(date '+%Y-%m-%d')
```
As a crontab entry, data is collected daily and written to a file named for the date.

# Future Development
For future development I plan to collect data daily through the use of cron-tab entries and compile this data into a database potentially JSON or SQL. This data will eventually be used for something interesting, idk I haven't thought that far yet.

Additional develoment:
Add more fields including; user, date, and filesize.

Make a algorythmn to suggest the best downloads based on filesize, ratio, and seeders.

Add error support and error codes.


