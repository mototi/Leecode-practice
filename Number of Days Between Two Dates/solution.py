month_mapper = {
    '1' : 31,
    '2' : 28,
    '3' : 31,
    '4' : 30,
    '5' : 31,
    '6' : 30,
    '7' : 31,
    '8' : 31,
    '9' : 30,
    '10' : 31,
    '11' : 30,
    '12' : 31
}


def swap_dates(year1 , month1 , day1 , year2, month2, day2):
        temp_year = year1
        year1 = year2
        year2 = temp_year
        
        temp_month = month1
        month1 = month2
        month2 = temp_month
        
        temp_day = day1
        day1 = day2
        day2 = temp_day
        
        return (year1, month1, day1, year2, month2, day2)
    

def days_counter_within_same_year(day1 , day2, month1, month2, year1, year2):
    if year1 % 4 == 0:
        month_mapper['2'] = 29
        
    month1_days_count = month_mapper[str(month1)]
    
    days_to_end_month1 = month1_days_count - day1
    days_to_start_month2 = day2
    
    days = days_to_end_month1 + days_to_start_month2
    
    for i in range(month1+1, 12, 1):
        days += month_mapper[str(i)]
    
    if year2 % 4 == 0:
        month_mapper['2'] = 29
    
    for i in range(month2-1, 0, -1):
        days += month_mapper[str(i)]
    
    return day2


def daysBetweenDates(date1, date2):
    """
    :type date1: str
    :type date2: str
    :rtype: int
    """
    
    date1 = date1.split("-")
    date2 = date2.split("-")
    
    year1 = int(date1[0])
    month1 = int(date1[1])
    day1 = int(date1[2])
    
    year2 = int(date2[0])
    month2 = int(date2[1])
    day2 = int(date2[2])
    
    if year1 > year2 or (year1 == year2 and month1 > month2) or (year1 == year2 and month1 == month2 and day1 > day2): 
        dates = swap_dates(year1, month1, day1, year2, month2, day2)
        year1 = dates[0]
        month1 = dates[1]
        day1 = dates[2]
        
        year2 = dates[3]
        month2 = dates[4]
        day2 = dates[5]
    
    
    if year1 == year2 and month1 == month2:
        return day2 - day1
    
    
    days = days_counter_within_same_year(day1 , day2, month1, month2, year1, year2)  
     
    if year1 != year2:
        while year1 < year2-1:
            year1 += 1
            if year1 % 4 == 0:
                days += 366
            else:
                days += 365
    
    return days
        
        
    
            
print(daysBetweenDates("2019-06-30","2019-06-29"))