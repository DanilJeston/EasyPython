# -*- coding:utf-8 -*-
from EasyScript import *
import sys
import yaml
import os
import argparse
import platform
import datetime

with open("EasyScript/config.yml") as f:
    config = yaml.safe_load(f.read())

if config['options']['fix-move-keys']:
    import readline

# 初始化argparse
# prog: Usage中的程序名
# description: -h 中的程序介绍
ArgParser = argparse.ArgumentParser(prog="EasyPython",
                                    description="""\
    an easy to learn and easy to use programming language developed in Python.
    """)

# 初始化非共存组
NonCoexistentGroup = ArgParser.add_mutually_exclusive_group()

# 添加选项 -i
# action: 动作
# help: -h 选项下显示的内容
NonCoexistentGroup.add_argument("-i",
                                "--interactive",
                                action="store_true",
                                help="Use interactive mode. [Default Option]")

# 添加选项 -f
# type: 自动转化类型
# help: -h 选项下显示的内容
NonCoexistentGroup.add_argument("-f",
                                "--file",
                                type=str,
                                help="Run the easypython code file.")

# 添加选项
# action: 动作
# help: -h 选项下显示的内容
ArgParser.add_argument("-v",
                       "--version",
                       action="store_true",
                       help="Get the version of the EasyPython.")

# 添加选项
ArgParser.add_argument("--fix-move-keys",
                       action="store_true",
                       help="Fix the problem of moving keys.")

# 分析参数
args = ArgParser.parse_args()
# print(args)

# 如果无任何参数
if args.interactive is False and args.version is False and not args.file:
    # 互交模式启动
    args.interactive = True
else:
    # 否则不进行任何操作
    pass
# 主版本号
MAJAR_VERSION = config['options']['majar-version']

# 副版本号
MINOR_VERSION = config['options']['minor-version']
# 补丁号
PATCH_VERSION = config['options']['patch-version']


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


def shell(name="<stdin>", RunFile=False, command=""):
    version = f"{str(MAJAR_VERSION)}.{str(MINOR_VERSION)}.{str(PATCH_VERSION)}"
    release_months = 12  # 月份
    release_day = 15  # 天
    release_year = 2021  # 年
    release_hour = 12  # 小时
    release_min = 11  # 分钟
    release_sec = 10  # 秒
    release_date_time = get_release_time(release_year, release_months,
                                         release_day, release_hour,
                                         release_min, release_sec)
    # 启动时显示的帮助信息
    start_help_info = '"help", "copyright"'
    # 输出启动信息
    if not RunFile:
        print(
            f"EasyPy(EasyPython) v{version}, (Released in {release_date_time}).\nRun EasyPy on {sys.platform}, {platform.platform()}.\nType {start_help_info} for more information.\nSource Code:https://gitee.com/ky-studio/EasyPython"
        )
    # 循环
    while True:
        # 获取用户输入信息
        if not RunFile:
            command = input('EasyPy >>> ')

        # 如果用户输入了exit
        if command == 'exit':
            # 退出并打印信息
            sys.exit("Good bye, Thanks for using.")

        elif command == '' or command == '\n':
            pass

        elif command == 'copyright':
            author = "yps and __init__"
            if datetime.datetime.now().year == 2021:
                year = "2021"
            else:
                year = '2021 - ' + str(datetime.datetime.now().year)
            print("Copyleft © {year} , {author}. Some rights reserved".format(
                year=year, author=author))  # 版权信息提示

        else:
            # 获取返回值与错误
            result, error = run(name, command)

            # 如果错误有具体内容
            if error:
                # 调用error的as_string方法
                print(error.as_string())
            # 如果有返回值
            elif result:
                # 打印返回值
                print(result)

        if RunFile:
            break


if __name__ == '__main__':
    if config["options"]["fix-move-keys"] is False:
        print(
            "Tips: If you have problems with your move keys, please add the '--fix-move-keys' option"
        )
    else:
        pass
    # 如果给有 -f 参数
    if args.file:
        # 如果可以读取文件
        if os.access(args.file, os.R_OK):
            path, temp = os.path.split(args.file)
            file_name, extension = os.path.splitext(temp)
            with open(args.file) as f:
                command = f.readline()
                while command[len(command) - 1:] == '\n':
                    shell(f"{file_name}{extension}", True, command)
                    command = f.readline()
                shell(f"{file_name}{extension}", True, command)
        else:
            raise PermissionError(f"Cannot open file {args.file}.")
    # 如果带有 --fix-move-keys
    if args.fix_move_keys is True:
        if not config['options']['fix-move-keys']:
            user_input = input(
                'It is detected that you have added the --fix-move-keys option. Do you need to fix the problem permanently? [Y/n]:'
            )
            if user_input == 'y' or user_input == 'Y' or user_input == '':
                with open("EasyScript/config.yml", 'w') as f:
                    config['options']['fix-move-keys'] = True
                    f.write(yaml.dump(config))
                import readline
    # 如果有给 -i 或任何参数也没有
    if args.interactive:
        # 进入shell
        shell()
    # 如果有 -v 参数
    if args.version:
        # 打印版本号
        print(
            f"EasyPython {str(MAJAR_VERSION)}.{str(MINOR_VERSION)}.{str(PATCH_VERSION)}"
        )
