#!/usr/bin/evn python3
# utilities
import subprocess

#split details
def expand_details(details):
    dates = {}; users = {}; file_sizes = {};
    for i in details:
        dates[i] = (details[i].split()[1] + " " + details[i].split()[2])
        users[i] = details[i].split()[8]
        file_sizes[i] = ((details[i].split()[4]) + " " + details[i].split()[5])
        #[4][:2]
    return (dates, users, file_sizes)

#calculate ratio
def calc_ratios(seeders, leachers):
    ratios = {};
    for i in seeders:
        if seeders[i] == 0  or leachers[i] == 0:
            ratios[i] = 0
        else:
            ratios[i] = round((seeders[i]/leachers[i]), 1)
    return (ratios)
#ouput functions
def print_results(results, data):
    print ("    Size       Ratio  Seeders    ID") #(succinct
    for i in results:
        if (i%2) == 0:
            print ("\033[m" + str(i) + "  " + data[i]['size'], data[i]['ratio'], int(data[i]['SE']), data[i]['_id'], "\033[0m", sep=('\t')) #(succinct)
        elif (i%2) != 0:
            print ("\033[36m" + str(i) + "  " + data[i]['size'], data[i]['ratio'], int(data[i]['SE']), data[i]['_id'], "\033[0m", sep=('\t')) #(succinct)
#        if (i%2) == 0:
#            print ("\033[m" + str(i) + "  " + data[i]['_id'], data[i]['size'], data[i]['ratio'], int(data[i]['SE']), "\033[0m", sep=('\t')) #(succinct)
#       elif (i%2) != 0:
#            print ("\033[36m" + str(i) + "  " + data[i]['_id'], data[i]['size'], data[i]['ratio'], int(data[i]['SE']), "\033[0m", sep=('\t')) #(succinct)

def print_magnets(results, data):
    for i in results:
        print (data[1]['_id'])
        print (data[i]['magnet'])

def transmission(results, data):
    for i in results:
        print ("\nuploading" + data[int(i)]['_id']+  " to transmission\n")
        subprocess.call(['transmission-cli', (data[int(i)]['magnet'])])

def json_output(search_result):
    with open('results.json', 'w') as fp:
        json.dump(data, fp, indent=4, sort_keys=True)
    print ("results exported to results.json")
