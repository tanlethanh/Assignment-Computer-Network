import time

# # số giây tính từ epoch
# # viet boi Quantrimang.com
# seconds = 1562983783.9618232
local_time = time.ctime(time.time())
print("Local time:", local_time)	

result = time.localtime(time.time())
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("tm_second:", result.tm_sec)

print("{:8.2f}".format(3.145454543545))
data = bytes()
print(type(data))
