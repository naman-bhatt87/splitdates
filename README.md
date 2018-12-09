# splitdates
input dates need to be in string format, output will be a list having pairs of dates (monthly) till target date.
example-
In [1]:from splitdateinmonths import *
In [2]: datesplit("10/11/2018", "20/12/2019")
Out[2]:
[['10/11/2018', '29/11/2018'],
 ['30/11/2018', '30/12/2018'],
 ['31/12/2018', '30/1/2019'],
 ['31/1/2019', '27/2/2019'],
 ['28/2/2019', '30/3/2019'],
 ['31/3/2019', '29/4/2019'],
 ['30/4/2019', '30/5/2019'],
 ['31/5/2019', '29/6/2019'],
 ['30/6/2019', '30/7/2019'],
 ['31/7/2019', '30/8/2019'],
 ['31/8/2019', '29/9/2019'],
 ['30/9/2019', '30/10/2019'],
 ['31/10/2019', '29/11/2019'],
 ['30/11/2019', '20/12/2019']]
