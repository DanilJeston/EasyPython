# -*- coding:utf-8 -*-
# from EasyScript.EasyTokens import *
# from EasyScript.EasyLexer import *
# from EasyScript.EasyPyErrors import *
# from EasyScript.EasyRun import *
# from EasyCode import *
from EasyScript import *
import sys
import datetime
import platform


def get_release_time(release_year, release_months, release_day, release_hour,
                     release_min, release_sec):
    release_months_dict = {
        '1': "Jan",
        '2': "Feb",
        '3': "Mar",
        '4': "Apr",
        '5': "May",
        '6': "Jun",
        '7': "Jul",
        '8': "Aug",
        '9': "Sept",
        '10': "Oct",
        '11': "Nov",
        '12': "Dec"
    }  # 创建月份字典

    # 发布日期↓
    release_date_time = "{months} {day} {year}, {hour}:{min}:{sec}".format(
        months=release_months_dict[str(release_months)],
        day=str(release_day),
        year=str(release_year),
        hour=str(release_hour),
        min=str(release_min),
        sec=str(release_sec))
    return release_date_time


def shell():
    Ctrl_C_Press = 0  # 记录Ctrl + C按下了几次
    Ctrl_Z_Press = 0  # 记录Ctrl + Z按下了几次
    version = "0.1.2"  # 版本
    release_months = 11  # 月份
    release_day = 6  # 天
    release_year = 2021  # 年
    release_hour = 16  # 小时
    release_min = 26  # 分钟
    release_sec = 40  # 秒
    commit_hash_code = "25aab89" # 前七位哈希值
    release_date_time = get_release_time(release_year, release_months,
                                         release_day, release_hour,
                                         release_min, release_sec)
    # start_help_info = '"help", "copyright", "credits" or "license"'
    # 启动时显示的帮助信息↓
    start_help_info = '"help", "copyright"'
    # 输出启动信息↓
    print(f"""
EasyPy(EasyPython) {version} ({commit_hash_code}:{version}), Released in {release_date_time}, Run EasyPy on {sys.platform}, {platform.platform()}.
Type {start_help_info} for more information.
Source Code:https://gitee.com/ky-studio/EasyPython
    """)
    while True:
        # 用try是为了检测Ctrl + C
        try:
            # 获取输入内容
            command = input("EasyPy >>> ")
            if command == 'exit':
                # 判断内容如果是exit执行退出操作
                print('GoodBye, Thank you for using.')
                sys.exit()
            elif command == '':
                # 如果为空，跳过
                pass
            elif command == 'help':
                # 如果输入help显示帮助文档
                help_docs = "Sorry, The help document is not completed."
                print(help_docs)
            elif command == 'copyright':
                # 如果输入copyright，显示版权信息
                author = "yps and __init__"
                if datetime.datetime.now().year == 2021:
                    year = "2021"
                else:
                    year = '2021 - ' + str(datetime.datetime.now().year)
                print("Copyright © {year} , {author}. All rights reserved".
                      format(year=year, author=author))  # 版权信息提示
            elif command == 'rules':
                pass
            else:
                # 获取返回值与错误
                result, error = run('<stdin>', command)
                # 如果错误值有内容输出错误值，反之输出返回值
                if error:
                    print(error.as_string())
                else:
                    print(result)

        except KeyboardInterrupt:
            if Ctrl_C_Press < 1:
                print(
                    "\n\"Ctrl + C\" has been pressed. if you want exit, please press the key again."
                )
                Ctrl_C_Press += 1
            else:
                print("\nGoodbye, Thank you for using.")
                sys.exit()

        except EOFError:
            if Ctrl_Z_Press < 1:
                print(
                    "\n\"Ctrl + Z\" has been pressed. if you want exit, please press the key again."
                )
                Ctrl_Z_Press += 1
            else:
                print("\nGoodbye, Thank you for using.")
                sys.exit()


shell()
