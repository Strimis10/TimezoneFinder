# TimezioneFinder

Timezonefinder is a package that lets you know in what timezones it's a specific time

*getTimezones

    `from TimezoneFinder import TimezoneFinder24h
    print(TimezoneFinder24h.getTimezone("13:29"))`





        Gettimezones
        ##get a list of all timezones where it's a specific time

    from TimezoneFinder import TimezoneFinder24h
    print(TimezoneFinder24h.getTimezone("13:29"))

    RESULT:
    ['Africa/Blantyre', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Ceuta', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Tripoli', 'Africa/Windhoek', 'Antarctica/Troll', 'Arctic/Longyearbyen', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Copenhagen', 'Europe/Gibraltar', 'Europe/Kaliningrad', 'Europe/Ljubljana', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Monaco', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Rome', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Skopje', 'Europe/Stockholm', 'Europe/Tirane', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zurich']



        Gettimezone
        ##get a single timezone where it's a specific times
    
    from TimezoneFinder import TimezoneFinder24h
    print(TimezoneFinder24h.getTimezones("13:29"))

    RESULT:
    Atlantic/Cape_Verde