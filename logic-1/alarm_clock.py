"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

"""

def alarm_clock(a, vacation):
    if vacation and 1 <= a <= 5:
        return '10:00'
    elif vacation and (a == 0 or a == 6):
        return "off"
    elif not vacation and 1 <= a <= 5:
        return '7:00'
    else:
        return "10:00"

print(alarm_clock(1, True))
print(alarm_clock(5, False))
print(alarm_clock(0, False))