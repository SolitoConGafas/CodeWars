# Solution to 4 Kyu Kata in codewars.com

"""
DESCRIPTION
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
"""

def format_duration(seconds):
    
    output = str()
    
    year_duration = 60*60*24*365
    day_duration = 60*60*24
    hour_duration = 60*60
    minute_duration = 60

    years = seconds // year_duration
    seconds -= years*year_duration

    days = seconds // day_duration
    seconds -= days*day_duration

    hours = seconds // hour_duration
    seconds -= hours*hour_duration

    minutes = seconds // minute_duration
    seconds -= minutes*minute_duration

    time_breakdown = [years, days, hours, minutes,seconds]

    time_dictionary = {
        0:'years',
        1:'days',
        2:'hours',
        3:'minutes',
        4:'seconds'
    }

    variables = []

    for count, item in enumerate(time_breakdown):
        if item != 0:
            if item == 1:
                variables += [[str(item),time_dictionary[count][:-1]]]
            else:
                variables += [[str(item),time_dictionary[count]]]

    pieces = [' '.join(i) for i in variables]

    if len(variables) == 0:
        output = 'now'
    elif len(variables) == 1:
        output += pieces[0]
    elif len(variables) == 2:
        output += pieces[0] + ' and ' + pieces[-1]
    elif len(variables) >= 3:
        output += pieces[0] + ', '
        for sentence in pieces[1:-1]:
            output += sentence + ', '
        output = output[:-2]
        output += ' and ' + pieces[-1]
    return(output)