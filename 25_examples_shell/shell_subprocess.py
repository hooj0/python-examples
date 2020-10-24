#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-23
# @copyright by hoojo@2020
# @changelog python3 `shell -> subprocess` example


# ===============================================================================
# 标题：python3 call shell command subprocess example
# ===============================================================================
# 使用：利用python调用shell命令行
#
# subprocess.getoutput(cmd)
#   输出命令执行结果
#
# subprocess.getstatusoutput(cmd)
#
#   其返回值是shell指令运行后返回的状态码，int类型，
#   0表示shell指令成功执行，256表示未找到，
#
#   该方法返回shell指令运行后的结果
# -------------------------------------------------------------------------------
# 描述：该方法适用于shell命令需要输出内容的场景
# -------------------------------------------------------------------------------
import subprocess


# help(subprocess.getoutput)
# -------------------------------------------------------------------------------
# 执行dir命令
# -------------------------------------------------------------------------------
status, output = subprocess.getstatusoutput("dir")
print("status: ", status)  # 0
print("output: ", output)

# output:
# -------------------------------------------------------------------------------
#  D:\work_private\python-examples\25_examples_shell 的目录
#
# 2020/10/23 周五  11:41    <DIR>          .
# 2020/10/23 周五  11:41    <DIR>          ..
# 2020/10/23 周五  11:35             2,101 shell_commands.py
# 2020/10/23 周五  11:32             2,290 shell_os_popen.py
# 2020/10/23 周五  11:21             2,351 shell_os_system.py
# 2020/10/23 周五  11:41             2,203 shell_subprocess.py
#                4 个文件          8,945 字节
#                2 个目录 20,369,559,552 可用字节


# -------------------------------------------------------------------------------
# 执行 echo 的命令
# -------------------------------------------------------------------------------
output = subprocess.getoutput("echo 'hello'")
print("output: ", output)   # hello


# -------------------------------------------------------------------------------
# 执行命令
# -------------------------------------------------------------------------------
# 执行命令，返回状态码(命令正常执行返回0，报错则返回1)
print(subprocess.call("echo 'hello'"))  # 0

# 执行命令，如果执行成功则返回状态码0，否则抛异常
print(subprocess.call("ping -n 2 www.baidu.com", shell=True))  # 0

# 执行命令，如果执行成功则返回状态码0，否则抛异常
print(subprocess.check_call("echo 'hello'"))  # 0

# 执行命令，如果执行成功则返回执行结果，否则抛异常
print(subprocess.check_output("echo hello"))  # 0
