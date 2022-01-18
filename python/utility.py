# Github repository: https://github.com/Christina-hshi/Bioinformatics-starter_kit.git
# By Christina HUAN SHI

import sys
from datetime import datetime
from colorama import Fore

def get_time_str():
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  return dt_string

class logger:
  def info(self, info_):
    print("["+get_time_str()+"] "+Fore.GREEN+info_+Fore.RESET)
  def warning(self, info_):
    print("["+get_time_str()+"] "+Fore.YELLOW+info_+Fore.RESET)
  def error(self, info_):
    print("["+get_time_str()+"] "+Fore.RED+info_+Fore.RESET)
    sys.exit(1)
logging = logger()
