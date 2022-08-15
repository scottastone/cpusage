import psutil
import colorama
from colorama import Fore, Back, Style

class CPUsage():
    def __init__(self):
        self.cpu_usage: float = 0.0
        self.cpu_frequency = 0
        self.memory_usage = 0
        self.uptime: float = 0.0
        self.cpu_fan = psutil.sensors_fans()
        self._printed_message: str = ""

        # self.data = []

        colorama.init()
        self.update()

    def update(self):
        self.cpu_usage = psutil.cpu_percent()
        self.cpu_frequency = psutil.cpu_freq(percpu=1)
        self.memory_usage = psutil.virtual_memory().percent
        self.ram_used = psutil.virtual_memory().used
        self.temperature = psutil.sensors_temperatures()
        self.uptime = psutil.cpu_stats
        self.cpu_fan = psutil.sensors_fans()

        # self.data.append(self.cpu_frequency)

    def print(self):
        self._pretty_print()

    def _pretty_print(self):
        print(Style.DIM + "------------------------")

        # CPU usage
        if self.cpu_usage < 50:
            print(Fore.GREEN + f"CPU: {self.cpu_usage:1.2f}%" + Fore.RESET)
        else:
            print(Fore.RED + f"CPU: {self.cpu_usage:1.2f}%" + Fore.RESET)

        # CPU frequency
        if len(self.cpu_frequency) > 1:
            for i, freq in enumerate(self.cpu_frequency):
                if freq.current < 1000:
                    print(Fore.RED + f"\tCore{i}: {freq.current:7.2f} MHz [{self.temperature['coretemp'][i].current}C] 🔥" + Fore.RESET)
                else:
                    print(Fore.GREEN + f"\tCore{i}: {freq.current:7.2f} MHz [{self.temperature['coretemp'][i].current}C] 🔥" + Fore.RESET)
        else:
            print(Fore.GREEN + f"CPU[all]: {self.cpu_frequency:1.2f} MHz" + Fore.RESET)

        #  Memory
        print(Fore.GREEN + f"Memory: {self.ram_used} ({self.memory_usage:1.2f}%)" + Fore.RESET)

        # Uptime
        print(Fore.GREEN + f"Uptime: {self.uptime}" + Fore.RESET)

        #print(Fore.GREEN + f"Data: {len(self.data)}" + Fore.RESET)
