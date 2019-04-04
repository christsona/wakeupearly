import time
import os


def automate_script():
    os.system("py automator.py")

def main():
    timenow = time.asctime(time.localtime(time.time()))
    while timenow !='Thu Apr  4 12:48:00 2019':
        timenow = time.asctime(time.localtime(time.time()))

    automate_script()
main()
