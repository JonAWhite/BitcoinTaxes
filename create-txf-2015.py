#!/usr/bin/python

# Creates a TXF file for LibraTax Form to populate Form 8949.
# https://turbotax.intuit.com/txf/TXF042.jsp
# Look for codes 712, 714.

# Export LibraTax for the Appropriate Calendar Year
# Remove the first three lines and last four lines.
# Essentially, you're looking for something like the following over and over:
# 0.4227 BTC,9/3/2015,1/3/2016,182.15,97.53,84.62,Short

# python create-txf-2015.py Libra-Tax_report-2016.csv > 2016_form_8949.txf

# Import the .txf file into TurboTax via 
# "File > Import > From TXF Files".
# You should see this:
# These Documents Are Now Ready for Import:
# - 1099-B (number of transactions)

# If you don't like what you see, you can remove the imported data via
# "File > Remove Imported Data".

import sys
import csv
import datetime

box_dict = {'Short': 712, 'Long': 714}

today = datetime.date.today()
today_formatted = today.strftime('%m/%d/%Y')

print 'V042'
print 'ALibraTax'
print 'D ' + today_formatted 
print '^'

with open(sys.argv[1], 'r') as csvfile:
    for row in csv.reader(csvfile): 
        amount = row[0]
        print 'Amount: ' + amount
        symbol = row[1]
        print 'Symbol: ' + symbol 
        acquired = row[2]
        print 'Acquired: ' + acquired 
        disposed = row[3]
        proceeds = row[4]
        base = row[5]
        gain = row[6]
        term = row[7]
        taxref = box_dict[term]
        descr = amount + ' ' + symbol 
        print 'TD'
        print 'N' + str(taxref)
        print 'C1'
        print 'L1'
        print 'P' + descr
        print 'D' + acquired
        print 'D' + disposed
        print '$' + base
        print '$' + proceeds
        print '^'
