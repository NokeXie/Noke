import win32api
from win32api import GetSystemMetrics
def DisplaySize():
    return GetSystemMetrics(0), GetSystemMetrics(1)

a, b = DisplaySize()
print(a,b)