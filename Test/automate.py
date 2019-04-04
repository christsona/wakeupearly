import time
import os


def automate_script():
    os.system("py test.py")

def main():
    timenow = time.asctime(time.localtime(time.time()))
    while timenow !='Thu Apr  4 01:02:00 2019':
        timenow = time.asctime(time.localtime(time.time()))

    automate_script()
main()
