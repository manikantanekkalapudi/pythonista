'''Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones in Python
video-> https://youtu.be/eirjjyP2qcQ
'''
# Importing datetime module
import datetime
'''
Naive datetime-> Doesn't have information like timezones and daylight saving info and are easy to work with.
Aware datetime-> Has information like timezones and daylight saving info
'''

# Create a date
d = datetime.date(2017, 7, 26) # Don't add 0 just pass single digits to avoid syntax error
print(d)

# Today's date-> Current local date
tday = datetime.date.today()
print(tday)
# print(tday.day)  # Just day
# print(tday.year) # Just year

# Get weekday
print(tday.weekday())    # Return day of the week, where Monday == 0 and Sunday == 6.
print(tday.isoweekday()) # Return day of the week, where Monday == 1 and Sunday == 7.

# Time delats
tdelta = datetime.timedelta(days=7)
print(tday + tdelta) # Date for the same day in next week or 7 days

# timedelta = date1 + date2
bday = datetime.date(2020, 7, 15)
till_day = bday -tday
print(till_day.days)

# datetime.time
t = datetime.time(10, 15, 13, 666)
print(t)

# Datetime-> Both date and time
dt = datetime.datetime(2020, 7, 15, 10, 15, 13, 666)
print(dt)
print(dt.date())
print(dt.time())
print(dt.month)

# Timedeltas with Datetime
tdelta = datetime.timedelta(hours=15)
print(dt + tdelta)

# Alternative Datetime constructors
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

# The below two gives the same o/p but with a millisecond output
print(dt_today)    # Returns a local datetime with timezone of none
print(dt_now)      # Gives an option to give a timezone and if left empty it's same as above
print(dt_utcnow)   # This is not a timezone aware datetime(none of the above are). It gives an UTC time with timezone set to None

# Install pytz using pip> 3rd part library recommended in datetime module doc
# Importing pytz module
import pytz

dt = datetime.datetime(2016, 12, 5, 13, 44, 55, tzinfo=pytz.UTC)
print(dt) # There is +00:00 at the end-> This is a UTC offset
 
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# Convert datetime from one timezone to another timezone
dt_mtn = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata')) # Timezone should be reffered from pytz module
print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)

# Navie datetime -> Aware datetime
dt_now = datetime.datetime.now()
# print(dt_now)

dt_east = dt_now.astimezone(pytz.timezone('US/Eastern')) # This can be done in Python 3.7.x
print(dt_east)

# ISO format
print(dt_mtn.isoformat())

# Format the time using format codes
print(dt_mtn.strftime('%B %d, %Y'))

# Parse string to datetime format
dt_str = 'July 24, 2017'
print(datetime.datetime.strptime(dt_str, '%B %d, %Y'))

'''
strftime->  Datetime to String
strptime -> String to Datetime
'''