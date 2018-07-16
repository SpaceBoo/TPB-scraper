#!/usr/bin/env python3

"""
pirate-bot
https://github.com/SpaceBoo/TPB-scraper
piratebot --help
"""

import json
import argparse
import util
import sys
import requests
from bs4 import BeautifulSoup
from cats import categories

def parse_arguments(args_in):
    parser = argparse.ArgumentParser()
    parser.add_argument('--search', '-s', metavar='[KEYWORD]',
                    help='search for a keyword')
    parser.add_argument('--top', '-T', action='store_true',
                    help='Get the top 100 daily torrents from TPB')
    parser.add_argument('--category', '-c', metavar='[CAT]',
                    help='look up the top torrents from a specific category')
    parser.add_argument('--cats', '-l', action='store_true',
                    help='gives the available categories')
    parser.add_argument('-t', '--transmission',
                    action='store_true',
                    help='open magnets with transmission-remote')
    parser.add_argument('--print', '-p', action='store_true',
                    help='print the data in plaintext')
    parser.add_argument('--csv', action='store_true',
                    help='print the data as csv', )
    parser.add_argument('--json', '-j', action='store_true',
                    help='print the data as JSON', )
    parser.add_argument('--results', '-r', nargs='+', type=int,
                    default=[1, 2, 3, 4, 5, 6, 7, 8 ,9, 10],
                    help='select results to colllect data from')
    parser.add_argument('--range', '-R', nargs=2, type=int,
                    help='Specify a range of results to collect data from')
    args = parser.parse_args(args_in)
    return args

#download and parse html
def get_soup(args):
    home_page = "https://thepiratebay.org"
    search = "/search/"
    top = "/top/"
    if args.search:
        webpage = (home_page + search + args.search)
    elif args.category:
        webpage = (home_page + top + str(categories[args.category]))
    elif args.top:
        webpage = (home_page + top + "all")
    else:
        webpage = (home_page + search + input("search term : "))
    print ("fetching webapge: " + webpage)

    page = requests.get(webpage)
    soup = BeautifulSoup(page.content, 'html.parser')
    return (page,soup)

def parse_html(page,soup):
    """ find a way to get rid of these two lines??
    -maybe some kind of dict. comprehension?"""
    result = 1; _id = {}; seeders = {} ;leachers = {}; magnets = {};
    details = {}; users = {}; file_sizes = {}
    if str(page) == "<Response [200]>":
        table = soup.find("table", id="searchResult")
        if not table:
            print ("You search did not return any results")
            return 'None'
        for tr in table.find_all("tr")[1:]:
            _id[result] =  ((tr.find(class_="detName")).get_text().replace("\n", ""))
            details[result] = (tr.find(class_="detDesc")).get_text()
            magnets[result] = tr.find_all('a')[3]["href"]
            seeders[result],leachers[result]= [int(i.text) for i in tr('td')[-2:]]
            result += 1

        dates, users, file_sizes = util.expand_details(details)
        ratios = util.calc_ratios(seeders, leachers)

        data={i: {'_id': _id[i], 'size': file_sizes[i], 'ratio': ratios[i],
        'SE': seeders[i], 'LE': leachers[i], 'uploader': users[i], 'date': dates[i],
        'magnet': magnets[i]} for i in range(1,(result))}
        return (data)

def pirate_main(args,data):
    # range --range/-R
    if args.range:
        results = []
        for i in range(args.range[0], (args.range[-1] + 1)):
            (results.append(i))
    # results --results/-r
    else:
        results = args.results
    # print --print/-p
    if args.print:
        util.print_results(results, data)
    # --transmission/-t
    if args.transmission:
        for i in results:
            util.transmission(i, data)
        #   util.transmission(results,data) #ALT3
    # --json/-j
    elif args.json:
        util.json_output(search_result)
    elif not args.transmission and not args.print and not args.json:
        util.print_results(results, data)
        _input = input("\nissue a command 'print' or 'transmission' \
        \nexamples: 'transmission 1 2 3' - 'print 5 10\n$ ").split()
        if _input[0] == "transmission":
            for i in range(1, len(_input)):
                util.transmission(_input[i], data)

        elif _input[1] == "transmission": # in case the user puts a space at the beginning of the input #ALT3
            for i in range(2, len(_input)):
                util.transmission(_input[i], data)

        elif _input[0] == "print":
            results = []
            for i in range(1, len(_input)):
                (results.append(int(_input[i])))
            util.print_results(results, data)

        elif _input[1] == "print":
            results = []
            for i in range(2, len(_input)):
                (results.append(int(_input[i])))
            util.print_results(results ,data)

### master caller
def main():
    args = parse_arguments(sys.argv[1:])
    if args.cats:
        print (json.dumps(categories, indent=4, sort_keys=True))
        sys.exit(0)
    page,soup = get_soup(args)
    data = parse_html(page,soup)
    pirate_main(args, data)

if __name__ == '__main__':
    main()
