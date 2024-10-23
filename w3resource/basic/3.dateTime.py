"""
Task: Display current date and time as : YYYY-MM-DD HH:mm:SS
"""

from time import localtime, strftime

print("Time: {}".format(strftime("%Y-%m-%d %H:%M:%S", localtime())))
