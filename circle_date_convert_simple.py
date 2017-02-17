from dateutil import parser

dates = [
"Sun Jan 03 2016 01:39:39 GMT+0000 (UTC)",
"Sat Jan 09 2016 18:59:47 GMT+0000 (UTC)",
]

for date in dates:
    date_obj = parser.parse(date)
    print str(date_obj.date()) + ' ' + str(date_obj.time())
