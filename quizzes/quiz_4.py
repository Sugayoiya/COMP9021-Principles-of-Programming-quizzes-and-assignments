# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.


# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
from collections import defaultdict


agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()

countries = []
if list(years)[0] < list(years)[1]:
    year_1, year_2 = list(years)[0], list(years)[1]
else:
    year_2, year_1 = list(years)[0], list(years)[1]
agri_indicator = 'AG.LND.AGRI.K2'
fore_indicator = 'AG.LND.FRST.K2'
position_1 = 0
position_2 = 0
data_agri = defaultdict( list )
data_fore = defaultdict( list )
data = defaultdict( list )
country_agri, country_fore, country = set([]), set([]), set([])
with open ( agricultural_land_filename, 'r', encoding='utf-8') as agri_file:
    lines = csv.reader(agri_file)
    for line in lines:
#         print(line)
#         print(len(line))
        if len(line) >3:
#             print(line)
            if str(year_1) in line and str(year_2) in line:
                # needed year position
                position_1 = line.index(str(year_1))
                position_2 = line.index(str(year_2))
            else:
                if line[position_1] != '' and line[position_2] !='':
                    data_agri[line[0]].append(float(line[position_2])-float(line[position_1]))
                    country_agri.add(line[0])
#     print(data_agri)
#     print(len(country_agri))
    
with open ( forest_filename, 'r', encoding='utf-8') as fore_file:
    lines = csv.reader(fore_file)
    for line in lines:
#         print(line)
#         print(len(line))
        if len(line) >3:
#             print(line)
            if str(year_1) in line and str(year_2) in line:
                # needed year position
                position_1 = line.index(str(year_1))
                position_2 = line.index(str(year_2))
            else:
                if line[position_1] != '' and line[position_2] !='':
                    data_fore[line[0]].append(float(line[position_2])-float(line[position_1]))
                    country_fore.add(line[0])
#     print(len(data_fore))
#     print(len(country_fore))

country = country_agri&country_fore
# print(len(country))

data = [ ( data_agri[k][0] / data_fore[k][0], k ) for k in country if data_fore[k][0]>0  ]
for ( ratio, country_out ) in sorted(data, reverse = True )[:top_n]:
    ratio = format(ratio,'.2f')
    countries.append( f'{country_out}  ({ratio})' )

print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))
    
