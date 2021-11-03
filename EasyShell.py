# -*- coding:utf-8 -*-
# from EasyScript.EasyTokens import *
# from EasyScript.EasyLexer import *
# from EasyScript.EasyPyErrors import *
# from EasyScript.EasyRun import *
# from EasyCode import *
from EasyScript import *
import sys
# import platform

    

def shell():
    exit_buttom_press = 0
    release_months_dict = {
        '1'  : "Jan",
        '2'  : "Feb",
        '3'  : "Mar",
        '4'  : "Apr",
        '5'  : "May",
        '6'  : "Jun",
        '7'  : "Jul",
        '8'  : "Aug",
        '9'  : 'Sept',
        '10' : "Oct",
        '11' : "Nov",
        '12' : "Dec"
    }
    version = 1.0
    release_months = 11
    release_day = 3
    release_year = 2021
    release_hour = 20
    release_min = 54
    release_sec = 30
    release_date_time = "{months} {day} {year}, {hour}:{min}:{sec}".format(
        months = release_months_dict[str(release_months)], 
        day = str(release_day), year = str(release_year), 
        hour = str(release_hour), min = str(release_min), 
        sec = str(release_sec))
    # start_help_info = '"help", "copyright", "credits" or "license"'
    start_help_info = '"help"'
    print("""
EasyPy(EasyPython) {version} (v{version}, {date_time}), Run EasyPy on {system_version}.
Type {start_help_info} for more information.
    """.format(version = version, 
               date_time = release_date_time, 
               
               system_version = sys.platform,
               start_help_info = start_help_info
               ))
    while True:
        try:
            text = input("EasyPy >>> ")
            # print("\n")
            if text == 'exit':
                print('GoodBye, Thank you for using.')
                sys.exit()
            elif text == '':
                pass
            else:
                result, error = run('<stdin>', text)

                if error:
                    print(error.as_string())
                else:
                    print(result)
        except KeyboardInterrupt:
            if exit_buttom_press < 1:
                print("\n\"Ctrl + C\" has been pressed. if you want exit, please press the key again.")
                exit_buttom_press += 1
            else:
                print("\nGoodbye, Thank you for using.")
                sys.exit()

shell()
