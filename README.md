**This repository has not been mainatined in some time**


# PirateBot
Piratebot allows users to scrape The Pirate Bay by category, top torrents, or searchterm.  Results can be viewed in the terminal, written to a file, or passed directly to transmission-cli for download. Piratebot is an excellent option for identifying torrents on a vps, torrent-box, or any computer where graphics may not be an option and integrates well into scripts with one line commands for automation and data collection.
 
# Features

# Arguments
  `-h, --help            show this help message and exit
  --search SEARCH, -s SEARCH
                        specify a search-term
  --top, -T             scrape the top 100 torrents of the day
  --transmission, -t    passes selected results to 'transmission-cli' for downloading
  --json, -j            pretty print the details of specified result(s) as json
  --print, -p           print the details of specified result(s) as plain text
  --results RESULTS [RESULTS ...], -r RESULTS [RESULTS ...]
                        specify selected results to act upon
  --range RANGE RANGE, -R RANGE RANGE
                        specify a range of results to act upon`
                        
# Examples

An example of an interactive session, ideal for headless torrent-boxes without graphical support:
```bash
archie@archlinux $ ./TPB_scraper

Please enter a search term :  Avengers

Index                         Title                               File Size       Ratio Seeders  Leachers                  
1   Avengers Infinity War 2018 NEW PROPER 720p HD-CAM X264 HQ-CPG                   4.0 7817     1965           
2   Avengers Infinity War 2018 720p TS x264 AAC TiTAN                               3.  63021                      836     3.6      
3   Avengers: Age of Ultron (2015) 1080p BrRip x264 - YIFY3003      643     4.7     
4   Avengers Infinity War 2018 720p TS x264 AAC TiTAN  2121      426     5.0      
5   Avengers.Infinity War.2018.720p.TS.1xBet
 814        73    11.2      Avengers.Infinity War.2018.720p.TS.1xBet

issue command 'print' or 'transmission' followed the media you wish to act upon

command  : transmission 2 

uploading  Avengers Infinity War 2018 720p TS x264 AAC TiTAN (index:2)  magnet  to transmission
...done
archie@archlinux $
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
For future development I plan to collect data daily through the use of cron-tab entries and compile this data into a databasThis data will eventually be used for something interesting.

Additional develoment:
Add more fields including; user, date, and filesize.

Make a algorythmn to suggest the best downloads based on filesize, ratio, and seeders.

Add error support and error codes.


