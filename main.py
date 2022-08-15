import time
from cpusage import CPUsage

def main():
    cpusage = CPUsage()
    while True:
        cpusage.update()
        cpusage.print()
        
        time.sleep(1/3)

if __name__ == "__main__":
    main()