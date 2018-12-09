def datesplit( date1, date2):
    t_date1 = ret_formated(date1)  # all values in int
    t_date2 = ret_formated(date2)
    #below program will check for leap year , if yes, set feb as 29.
    if chk_leap_year(t_date2[0]) != 0:
        month_dict = { '31' : ('1', '3', '5', '7', '8', '10', '12'), '30' : ('4', '6', '9', '11'), '28':('2') }
    else:
        month_dict = { '31' : ('1', '3', '5', '7', '8', '10', '12'), '30' : ('4', '6', '9', '11'), '29':('2') }
    s_month = t_date1[1]
    s_year = t_date1[0]
    t_month = t_date2[1]
    t_year = t_date2[0]
    datelist = [[date1], ]  # format would be dd/mm/yyyy
    # checking month difference
    tot_months = (((t_year - s_year)*12) + (t_month - s_month))
    while tot_months != 0:
        for key, value in month_dict.items(): # this loop will pull month end date.
            if str(s_month) in value:
                temp_day = int(key)
                #print(datelist)
                #type(datelist[-1])
                datelist[-1].append(str(temp_day - 1)+"/"+str(s_month)+"/"+str(s_year))
                datelist.append([str(temp_day)+"/"+str(s_month)+"/"+str(s_year)])
        s_month = s_month + 1
        if s_month == 13:    # resetting counter to Januaray
            s_month = 1
            s_year = s_year + 1
        tot_months= tot_months - 1

    datelist[-1].append(str(t_date2[-1])+"/"+str(t_month)+"/"+str(t_year))
    return(datelist)


# function to convert a string dd/mm/yyyy to a list [yyyy, mm, dd]
def ret_formated( date1 ):
    dyear = date1[-4:]
    dmnt = int(date1[3:5])
    dday = int(date1[:2])
    if len(dyear) != 4 or dmnt > 12:
        raise Exception("wrong format, this function expects format dd/mm/yyyy")
    else:
        return([int(dyear), dmnt, dday])

#function to checkfor a leapyear
def chk_leap_year(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        return(0)
    else:
        return(1)
