# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:20:15 2015

@author: iphyer
"""

#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('3k.sqlite')

print "Opened database successfully";

#start=raw_input("Please input the starting list you want ,like 1")
#end=  raw_input("Please input the ending list you want,like 3")

cu = conn.cursor()

#cu.execute("SELECT Column1 AS Eng,Column2 AS Chn FROM list1 UNION SELECT Column1 AS Eng,Column2 AS Chn FROM list2 ORDER BY RANDOM() LIMIT 1;")

#cu.execute("SELECT Column1 AS Eng,Column2 AS Chn FROM list1 UNION SELECT Column1 AS Eng,Column2 AS Chn FROM list2 ORDER BY Eng RANDOM()")
cu.execute("SELECT Column1 AS Eng,Column2 AS Chn, random() AS r FROM list1 UNION ALL SELECT Column1 AS Eng,Column2 AS Chn, random() AS r FROM list2 UNION ALL SELECT Column1 AS Eng,Column2 AS Chn, random() AS r FROM list21 UNION ALL SELECT Column1 AS Eng,Column2 AS Chn, random() AS r FROM list31 ORDER BY r")

rows = cu.fetchall()
for row in rows:
    print '\n %s %s' % (row[0], row[1])