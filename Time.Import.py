import datetime

now = datetime.datetime.now()
print(now)
print("Current year: %d" % now.year)
print("Current month: %d" % now.month)
print("Current day: %d" % now.day)
print("Current hour: %d" % now.hour)
print("Current minute: %d" % now.minute)
print("Current second: %d" % now.second)
print("Curren microseconds: %d" % now.microsecond)

print(now.strftime("%Y-%m-%d %H:%M"))
