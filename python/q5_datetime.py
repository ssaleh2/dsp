# Hint:  use Google to find python function
from datetime import datetime, date

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'
fmt = '%m-%d-%Y' 
start = datetime.strptime(date_start,fmt)
stop = datetime.strptime(date_stop,fmt)
print (stop-start).days

####b)  
date_start = '12312013'  
date_stop = '05282015' 
fmt = '%m%d%Y' 
start = datetime.strptime(date_start,fmt)
stop = datetime.strptime(date_stop,fmt)
print (stop-start).days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 
fmt = '%d-%b-%Y' 
start = datetime.strptime(date_start,fmt)
stop = datetime.strptime(date_stop,fmt)
print (stop-start).days