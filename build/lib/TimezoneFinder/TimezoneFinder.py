import pytz
from datetime import datetime
       

zones = ['Africa/Abidjan', 'Africa/Addis_Ababa', 'Europe/London', 'Europe/Stockholm', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Araguaina', 
    'America/Atikokan', 'America/Belize', 'America/Creston', 'America/Miquelon', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Mawson', 
    'Antarctica/McMurdo', 'Antarctica/Vostok', 'Asia/Baku', 'Asia/Brunei', 'Asia/Chita', 'Atlantic/Cape_Verde', 'Pacific/Apia', 'Pacific/Honolulu']


##get a list of all timezones where it's a specific time
def gettimezones24h(time:str):
    
    listOfTimeZones = []

    ##make sure the input is formated correctly
    if len(time) != 5:
        raise Exception("ERROR: time not formated correctly (##:##)")
    num = 0
    minute = ""
    for character in time:
        if num == 2:
            if character != ":":
                raise Exception("ERROR: time not formated correctly (##:##)")
        else:
            if not character.isdigit():
                raise Exception("ERROR: time not formated correctly (##:##)")
        if num > 2:
            minute += character

        num += 1
    
    ##Make sure that the time is the current time
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%M")
    if not minute == currentTime:
        raise Exception("ERROR: Time is not correct, minutes must match current")

    ##check in what timesones the time matches
    for timezone in pytz.common_timezones:
        timezonee = pytz.timezone(timezone)
        currentDateAndTime = datetime.now(timezonee)
        currentTime = currentDateAndTime.strftime("%H:%M")
        if time == currentTime:
            listOfTimeZones.append(timezone)
    return listOfTimeZones
            





##get a single timezone where it's a specific times
def getTimezone24h(time:str):
    

    ##make sure the input is formated correctly
    if len(time) != 5:
        raise Exception("ERROR: time not formated correctly (##:##)")
    num = 0
    minute = ""
    for character in time:
        if num == 2:
            if character != ":":
                raise Exception("ERROR: time not formated correctly (##:##)")
        else:
            if not character.isdigit():
                raise Exception("ERROR: time not formated correctly (##:##)")
        if num > 2:
            minute += character

        num += 1
    
    ##Make sure that the time is the current time
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%M")
    if not minute == currentTime:
        raise Exception("ERROR: Time is not correct, minutes must match current")

    ##check in what timesones the time matches
    for timezone in pytz.common_timezones:
        timezonee = pytz.timezone(timezone)
        currentDateAndTime = datetime.now(timezonee)
        currentTime = currentDateAndTime.strftime("%H:%M")
        if time == currentTime:
            if timezone in zones:
                break
    return timezone

