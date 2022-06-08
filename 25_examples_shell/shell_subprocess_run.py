#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-23
# @copyright by hoojo@2020
# @changelog python3 `shell -> subprocess run` example


# ===============================================================================
# 标题：python3 call shell command subprocess run example
# ===============================================================================
# 使用：利用python调用shell命令行
#
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False,
#       cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
#   python3.5中新增的函数， 执行指定的命令， 等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例
#
#   完整的函数形式很大程度上与Popen构造函数相同
#   ———— 除timeout、input和check之外，该函数的所有参数都传递给Popen接口。
#
#   encoding: 如果指定了该参数，则 stdin、stdout 和 stderr 可以接收字符串数据，并以该编码方式编码。否则只接收 bytes 类型的数据。
#   check：如果check为True且退出代码非零，则引发 CalledProcessError。 CalledProcessError对象将具有返回码
#           在returncode属性中，以及output＆stderr属性（如果这些流）被抓获。
#   timeout：如果给出了超时，并且过程耗时太长，则TimeoutExpired将会引发异常
#   input：有一个可选参数“输入”，使您可以将字符串传递给子进程的标准输入。
#           如果使用此参数您可能还不能使用Popen构造函数的“ stdin”参数，例如它将在内部使用。
#   如果传递了Universal_newlines = True，则“ input”参数必须为返回对象中的string和stdout / stderr将是字符串而不是个字节。
#
#   返回的实例将具有args，returncode，stdout和stderr。
#   默认情况下，不捕获stdout和stderr，并且这些属性将为无。传递stdout = PIPE和/或stderr = PIPE以便捕获它们。
# -------------------------------------------------------------------------------
# Popen类拥有的方法及属性
#   1、Popen.pid 获取子进程的进程ID。
#   2、Popen.returncode 获取进程的返回码。如果进程未结束，将返回None。
#   3、communicate(input=None)
#       该方法中的可选参数 input 应该是将被发送给子进程的数据，或者如没有数据发送给子进程，该参数应该是None。
#       input参数的数据类型必须是字节串，如果universal_newlines参数值为True，则input参数的数据类型必须是字符串。
#       该方法返回一个元组(stdout_data, stderr_data)，这些数据将会是字节穿或字符串（如果universal_newlines的值为True）。
#       如果在timeout指定的秒数后该进程还没有结束，将会抛出一个TimeoutExpired异常。捕获这个异常，然后重新尝试通信不会丢失任何输出的数据。
#       但是超时之后子进程并没有被杀死，为了合理的清除相应的内容，一个好的应用应该手动杀死这个子进程来结束通信。
#       需要注意的是，这里读取的数据是缓冲在内存中的，所以，如果数据大小非常大或者是无限的，就不应该使用这个方法。
#   4、poll() 检查子进程是否结束，并返回returncode属性。
#   5、wait() 等待子进程执行结束，并返回returncode属性，如果为0表示执行成功。
#   6、send_signal( sig) 发送信号给子进程。
#   7、terminate()  终止子进程。windows下将调用Windows API TerminateProcess（）来结束子进程。
#   8、kill() 终止子进程。windows下将调用Windows API TerminateProcess（）来结束子进程。
#       官方文档对这个函数的解释跟terminate()是一样的，表示杀死子进程。
# -------------------------------------------------------------------------------
# 描述：该类用于在一个新的进程中执行一个子程序。
# 即允许你去创建一个新的进程让其执行另外的程序，并与它进行通信，获取标准的输入、标准输出、标准错误以及返回码等
# -------------------------------------------------------------------------------
import subprocess


# help(subprocess.run)
# -------------------------------------------------------------------------------
# 执行 echo 命令
# -------------------------------------------------------------------------------
process = subprocess.run("echo hello", stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
print(process)  # CompletedProcess(args='echo hello', returncode=0)
print("args: ", process.args)
print("return code:", process.returncode)
# 设置 universal_newlines=True 返回 字符串
print("stdout: ", process.stdout)
print("stderr: ", process.stderr)


print("------------------------------------------------------------------------")
# output:
# -------------------------------------------------------------------------------
# CompletedProcess(args='echo hello', returncode=0, stdout='hello\n', stderr='')
# args:  echo hello
# return code: 0
# stdout:  hello
#
# stderr:


# -------------------------------------------------------------------------------
# 执行 ping 命令
# -------------------------------------------------------------------------------
# 设置 shell=True 否则找不到命令，表示直接在解释器中运行
process = subprocess.run("dir", stdout=subprocess.PIPE, shell=True)
print(process)
print("args: ", process.args)
print("return code:", process.returncode)
# 没有设置universal_newlines=True，返回字节
print("stdout: ", process.stdout.decode("gbk"))
# 没有设置参数 stderr
print("stderr: ", process.stderr)   # None


print("------------------------------------------------------------------------")
# output:
# -------------------------------------------------------------------------------
# CompletedProcess(args='dir', returncode=0, stdout=b' \xc7\xfd\xb6\xaf\xc6\xf7 D \xd6\xd0\xb5\xc4\xbe\xed\xca\xc7 IDESpace\r\n \xbe\xed\xb5\xc4\xd0\xf2\xc1\xd0\xba\xc5\xca\xc7 D09E-63C9\r\n\r\n D:\\work_private\\python-examples\\25_examples_shell \xb5\xc4\xc4\xbf\xc2\xbc\r\n\r\n2020/10/23 \xd6\xdc\xce\xe5  15:21    <DIR>          .\r\n2020/10/23 \xd6\xdc\xce\xe5  15:21    <DIR>          ..\r\n2020/10/23 \xd6\xdc\xce\xe5  11:56             2,569 shell_os_popen.py\r\n2020/10/23 \xd6\xdc\xce\xe5  11:21             2,351 shell_os_system.py\r\n2020/10/23 \xd6\xdc\xce\xe5  14:23             3,304 shell_subprocess.py\r\n2020/10/23 \xd6\xdc\xce\xe5  14:59             7,427 shell_subprocess_popen.py\r\n2020/10/23 \xd6\xdc\xce\xe5  15:21             6,756 shell_subprocess_run.py\r\n               5 \xb8\xf6\xce\xc4\xbc\xfe         22,407 \xd7\xd6\xbd\xda\r\n               2 \xb8\xf6\xc4\xbf\xc2\xbc 20,369,547,264 \xbf\xc9\xd3\xc3\xd7\xd6\xbd\xda\r\n')
# args:  dir
# return code: 0
# stdout:   驱动器 D 中的卷是 IDESpace
#  卷的序列号是 D09E-63C9
#
#  D:\work_private\python-examples\25_examples_shell 的目录
#
# 2020/10/23 周五  15:21    <DIR>          .
# 2020/10/23 周五  15:21    <DIR>          ..
# 2020/10/23 周五  11:56             2,569 shell_os_popen.py
# 2020/10/23 周五  11:21             2,351 shell_os_system.py
# 2020/10/23 周五  14:23             3,304 shell_subprocess.py
# 2020/10/23 周五  14:59             7,427 shell_subprocess_popen.py
# 2020/10/23 周五  15:21             6,756 shell_subprocess_run.py
#                5 个文件         22,407 字节
#                2 个目录 20,369,547,264 可用字节
#
# stderr:  None


# -------------------------------------------------------------------------------
# 执行 ping 命令
# -------------------------------------------------------------------------------
# 设置编码encoding="gbk"，stdout直接返回字符串
process = subprocess.run("ping -t www.baidu.com -n 2", stdout=subprocess.PIPE, encoding="gbk")
print("args: ", process.args)
print("return code:", process.returncode)
# 设置编码encoding="gbk"，stdout直接返回字符串
print("stdout: ", process.stdout)
print("stderr: ", process.stderr)

print("------------------------------------------------------------------------")
# output:
# -------------------------------------------------------------------------------
# args:  ping -t www.baidu.com -n 2
# return code: 0
# stdout:
# 正在 Ping www.a.shifen.com [163.177.151.110] 具有 32 字节的数据:
# 来自 163.177.151.110 的回复: 字节=32 时间=5ms TTL=55
# 来自 163.177.151.110 的回复: 字节=32 时间=5ms TTL=55
#
# 163.177.151.110 的 Ping 统计信息:
#     数据包: 已发送 = 2，已接收 = 2，丢失 = 0 (0% 丢失)，
# 往返行程的估计时间(以毫秒为单位):
#     最短 = 5ms，最长 = 5ms，平均 = 5ms
#
# stderr:  None


# -------------------------------------------------------------------------------
# 执行 exit 命令
# -------------------------------------------------------------------------------
# check 参数引发异常
subprocess.run("exit 1", shell=True, check=True)

# -------------------------------------------------------------------------------
# 执行 uglifyjs 命令
# -------------------------------------------------------------------------------
process = subprocess.run("uglifyjs --help", stdout=subprocess.PIPE, shell=True, universal_newlines=True, encoding="utf-8")
print(process)
print("args: ", process.args)
print("return code:", process.returncode)
# 没有设置universal_newlines=True，返回字节
# print("stdout: ", process.stdout.decode("utf-8"))
print("stdout: ", process.stdout)
# 没有设置参数 stderr
print("stderr: ", process.stderr)   # None
