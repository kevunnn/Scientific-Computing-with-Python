def add_time(start, duration, day=''):

    week = {1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}

    #convert to 24-hour format

    firstsplitstart = start.split(':')
    secondsplitstart = firstsplitstart[1].split(' ')
    starthour = int(firstsplitstart[0])
    startmin = int(secondsplitstart[0])
    meridiem = secondsplitstart[1]
    if meridiem == 'PM':
        starthour = starthour * 100 + 1200
    elif meridiem == 'AM':
        starthour = starthour * 100
    #print(starthour)
    #print(startmin)

    splitduration = duration.split(':')
    durationhour = int(splitduration[0])
    durationmin = int(splitduration[1])
    if durationhour > 48:
        newdurationhour = durationhour % 24
        newdurationhour = newdurationhour * 100
        totalhour = starthour + newdurationhour
    else:
        totalhour = starthour + (durationhour * 100)
    #if durationhour >= 24:
    #    converteddurationhour = (durationhour % 24) * 100
    #print(durationhour)
    #print(durationmin)

    totalminute = durationmin + startmin
    if totalminute > 60:
        totalminute = totalminute - 60
        totalhour = totalhour + 100
    
    #print(totalhour)
    #print(totalminute)
    
    total = totalhour + totalminute

    #print(total)
    
    if total > 2359 and total < 4759 and durationhour < 48:
        total = total - 2400
        addeddays = int(durationhour / 24)
        finaladdeddays = '(next day)'
    elif durationhour > 48:
        total = total - 2400
        addeddays = int(durationhour / 24 + 1)
        finaladdeddays = (f'({addeddays} days later)')
    elif total > 4759:
        total = total - 4800
        addeddays = int(durationhour / 24 + 1)
        finaladdeddays = (f'({addeddays} days later)')
    else:
        finaladdeddays = ''
    #print(durationhour)
    #print(addeddays)
    if total >= 1200:
        meridiem = 'PM'
    elif total <1200:
        meridiem = 'AM'

    try:
        if day != '':
            day = day.capitalize()
            numday = [k for k, v in week.items() if v == day]
            newnumday = int(numday[0]) + addeddays
            if newnumday > 7:
                newnumday = newnumday % 7
            day = week.get(newnumday)
    except:
        day = day
 
    if total > 1200 and total < 2400: 
        total = total - 1200

    if len(str(total)) < 3:
        total = total + 1200
    
    #print(total)

    total = str(total)
    if len(total) == 4 and day != '':
        new_time = (f'{total[-4]}{total[-3]}:{total[-2]}{total[-1]} {meridiem}, {day} {finaladdeddays}').replace('  ',' ')
    elif len(total) == 3 and day != '':
        new_time = (f'{total[-3]}:{total[-2]}{total[-1]} {meridiem}, {day} {finaladdeddays}').replace('  ',' ')
    elif len(total) == 4 and day == '':
        new_time = (f'{total[-4]}{total[-3]}:{total[-2]}{total[-1]} {meridiem} {finaladdeddays}').replace('  ',' ')
    elif len(total) == 3 and day == '':
        new_time = (f'{total[-3]}:{total[-2]}{total[-1]} {meridiem} {finaladdeddays}').replace('  ',' ')
    
    new_time = new_time.rstrip()
    
    #return new_time
    print(new_time)

add_time("2:59 AM", "24:00", "saturDay")