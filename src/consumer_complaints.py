# -*- coding: utf-8 -*-
"""
Created on Monday Apr 16 2020

@author: Liam Geiger
"""

#import data set in read mode
import csv
from datetime import datetime
from collections import Counter
import os

start = datetime.now()
#use csv_splitter to split file developed by Aziz Alto https://stackoverflow.com/questions/36445193/splitting-one-csv-into-multiple-files-in-python/36445821
#This was used only for dev purposes to make the file easier to handle
#csvfile = open('complaints.csv', 'r', encoding="utf8").readlines()
#filename = 1
#for i in range(len(csvfile)):
#    if i % 50000 == 0:
#        open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+1000])
#        filename += 1
#define variables and lists
#date list to convert to datetime
date = []
#year list for full CSV file datetime
year = []
#full list of years in CSV
yeart = []
#unique list of years in CSV
uniq_year = []
#final list of years for output
final_yeart = []

#list of product types
product = []
#full list of products
productt = []
#unique list of products
uniq_product = []


#list of issues
issue = []
#full list of issues
issuet = []

#list of companies
company = []
#full list of companies
companyt = []
#unique list of companies
uniq_company = []

#create master dictionary
z = {}
#set default columns for csv file in case file does not have header
#default date row
d = 0
#default product column
p = 1
#default company column
c = 7

#path = r"C:\Users\liamg_000\Documents\Insight Program\Projects\LSG_Coding_Challenge\To ze Hub\insight_testsuite\tests\your-own-test_1\input\complaints.csv"
#path = r"C:\Users\liamg_000\Documents\Insight Program\Projects\LSG_Coding_Challenge\To ze Hub\input\complaints.csv"
inpath = r"./input/complaints.csv"
with open(inpath, encoding="utf8") as csvfile:
    csv_reader = iter(csv.reader(csvfile, delimiter = ','))
    #determine if csv file has a header
    sniffer = csv.Sniffer()
    has_header = sniffer.has_header(csvfile.read(2048))
    csvfile.seek(0)
    #if it has a header skip header and start importing lines below
    if has_header:
        try:
            header = next(csv_reader)
            d =header.index('Date received')
            p = header.index('Product')
            c = header.index('Company')
            #quick check to make sure header contains proper strings
        except ValueError:
            print("Date Format Error","The header contains unknown strings. "
                                                     "Confirm the header in the csv file has all three of the following "
                                                     "exactly    Date recieved   Product   Company")
            next(csv_reader)
    #import data csv
    for row in csv_reader:
        #quick check to make sure date column is in correct format.
        try:
            datecheck = datetime.strptime(row[d], "%Y-%m-%d")
        except ValueError:
            print("Date Format Error",
                                 ("Dates are required to be in YYYY-MM-DD format please contact Liam @ ext xxxx if "
                                  "issue persists. The error is with this data ", row[d]),)
        # getting total year list and unique years out of csv
        date = datetime.strptime(row[d], "%Y-%m-%d")
        year = date.year
        yeart.append(year)
        #getting total product list and unique products out of csv
        product = row[p]
        productt.append(product.lower())
        #getting total company list and unique companies out of csv
        company = row[c]
        companyt.append(company)


uniq_product = set(productt)
uniq_product = sorted(uniq_product)
#print(uniq_product)

#sorting unique years numerically
uniq_year = set(yeart)
uniq_year = sorted(uniq_year)
#print(uniq_year)

#create list of unique company names
uniq_company = set(companyt)
#print(uniq_company)


#create super dictionary to help "sort" data similar to excel pivot table

for year, product, company in zip(yeart, productt, companyt):
    if product not in z.keys():
        z[product] = {}
    if year not in z[product].keys():
        z[product][year] = []
    z[product][year].append(company)

final_count = []
final_product = []
final_productt = []
final_year = []
final_company_count = []
final_company_count_maxt = []
total_number_compt = []
final_number_compt = []
final_high_perc = []

#setting up final year list, total number of complaint list, and total number of complaint list
for i in uniq_product:
    for j in uniq_year:
        complaint_count = len(z.get(i, {}).get(j, {}))
        final_count.append(complaint_count)
        final_year.append(uniq_year)
        company_count = list(Counter(z.get(i, {}).get(j, {})).values())
        final_company_count.append(company_count)
        total_number_comp = list(Counter(set(z.get(i, {}).get(j, {}))).values())
        total_number_compt.append(total_number_comp)


# determine the total number of companies for that year and product
for val in range(len(final_company_count)):

    final_company_count_max = max(final_company_count[val], default=0)
    final_company_count_maxt.append(final_company_count_max)
    final_number_comp = sum(total_number_compt[val])
    final_number_compt.append(final_number_comp)



#setting up final product and year list to repeat based on number of unique years
for i in range(len(uniq_product)):
    for j in range(len(uniq_year)):
        final_product = uniq_product[i]
        final_productt.append(final_product)
        final_year = uniq_year[j]
        final_yeart.append(final_year)


#determine the largest percentage of complaints against a single company
for i, j in zip(final_company_count_maxt, final_count):
    try:
        final_high_perc.append((100*i)/j)
    except ZeroDivisionError:
        final_high_perc.append(0)
final_high_perc_round = [round(num) for num in final_high_perc]

#define output list
report_list = [(a, b, c, d, e) for a, b, c, d, e in zip(final_productt, final_yeart, final_count, final_number_compt, final_high_perc_round) if a and b and c and d and e]
#report_list = zip(final_productt, final_yeart, final_count, final_number_compt, final_high_perc_round)

with open('./output/report.csv', 'w', newline= '',encoding="utf8") as report:
    writer = csv.writer(report)
    for row in report_list:
        writer.writerow(row)
    report.seek(0, os.SEEK_END)
    report.seek(report.tell()-2, os.SEEK_SET)
    report.truncate()
finish = datetime.now()

elapsed = finish-start
print('finished in ',elapsed)
