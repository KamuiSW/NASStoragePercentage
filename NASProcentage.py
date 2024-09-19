import shutil
import math

path = ""
total, used, free = shutil.disk_usage(__file__)

usedPercentage = used/total * 100

print(round(usedPercentage),"%")