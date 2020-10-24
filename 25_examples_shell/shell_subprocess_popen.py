#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-23
# @copyright by hoojo@2020
# @changelog python3 `shell -> subprocess popen` example


# ===============================================================================
# 标题：python3 call shell command subprocess popen example
# ===============================================================================
# 使用：利用python调用shell命令行
#
# subprocess.Popen("cmd", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#   args 必须是一个字符串或者序列类型（如：字符串、list、元组），用于指定进程的可执行文件及其参数。
#       如果是一个序列类型参数，则序列的第一个元素通常都必须是一个可执行文件的路径。
#       当然也可以使用executeable参数来指定可执行文件的路径。
#   bufsize： 指定缓存策略，0表示不缓冲，1表示行缓冲，其他大于1的数字表示缓冲区大小，负数 表示使用系统默认缓冲策略。
#   shell = True 表示直接在解释器中运行，即不会弹出黑的命令行。如果这个参数被设置为True，程序将通过shell来执行
#   env：它描述的是子进程的环境变量。如果为None，子进程的环境变量将从父进程继承而来
#   cwd：在执行子级之前设置当前目录。
#   executable：要执行的替换程序。
#   universal_newlines：对输出内容的结尾符号有改变。
#   close_fds： 如果该参数的值为True，则除了0,1和2之外的所有文件描述符都将会在子进程执行之前被关闭
#   preexec_fn： 用于指定一个将在子进程运行之前被调用的可执行对象，只在Unix平台下有效。
#   stdin,stdout,stderr：分别表示程序的标准输入、标准输出、标准错误。
#       有效的值可以是PIPE，存在的文件描述符，存在的文件对象或None，如果为None需从父进程继承过来，
#       stdout可以是PIPE，表示对子进程创建一个管道，
#       stderr可以是STDOUT，表示标准错误数据应该从应用程序中捕获并作为标准输出流stdout的文件句柄。
#
#   该方法返回shell指令运行后的结果
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


# help(subprocess.Popen)
# -------------------------------------------------------------------------------
# 执行dir命令
# -------------------------------------------------------------------------------
# 这里通过将stdout重定向到subprocess.PIPE上来取得cmd命令的输出，
# 如果想将stderr也重定向到subprocess.PIPE上,stderr=subprocess.STDOUT改成stderr=subprocess.PIPE即可
process = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print("pid: ", process.pid)
# 该方法和子进程交互，返回一个包含 输出和错误的元组，如果对应参数没有设置的，则无法返回
stdout_data, stderr_data = process.communicate()
# 可以设置 encoding 参数解决编码问题
print("stdout_data:", stdout_data.decode("gbk"))
print("stderr_data:", stderr_data)
print("return code: ", process.returncode)

print("------------------------------------------------------------------------")
# output:
# -------------------------------------------------------------------------------
# pid:  23308
# stdout_data:  驱动器 D 中的卷是 IDESpace
#  卷的序列号是 D09E-63C9
#
#  D:\work_private\python-examples\25_examples_shell 的目录
#
# 2020/10/23 周五  14:42    <DIR>          .
# 2020/10/23 周五  14:42    <DIR>          ..
# 2020/10/23 周五  11:56             2,569 shell_os_popen.py
# 2020/10/23 周五  11:21             2,351 shell_os_system.py
# 2020/10/23 周五  14:23             3,304 shell_subprocess.py
# 2020/10/23 周五  14:42             6,685 shell_subprocess_popen.py
#                4 个文件         14,909 字节
#                2 个目录 20,369,555,456 可用字节
#
# stderr_data: None
# return code:  0


# -------------------------------------------------------------------------------
# 执行 ping 命令
# -------------------------------------------------------------------------------
process = subprocess.Popen("ping -n 3 www.baidu.com", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print("pid: ", process.pid)

# 终止命令
# process.kill()

# 有些命令行是异步执行的不会马上返回输出
process.wait()

# 读取输出内容
# 通过process.stdout.read()来读取命令行输出，不过process.stdout.read()返回的是bytes,
# 要想取得str,可以直接调用process.stdout.read().decode('utf-8')
output = process.stdout.read().decode("gbk")
print(output)

print("return code: ", process.returncode)

print("------------------------------------------------------------------------")
# output:
# -------------------------------------------------------------------------------
# pid:  22888
#
# 正在 Ping www.a.shifen.com [163.177.151.110] 具有 32 字节的数据:
# 来自 163.177.151.110 的回复: 字节=32 时间=6ms TTL=55
# 来自 163.177.151.110 的回复: 字节=32 时间=5ms TTL=55
# 来自 163.177.151.110 的回复: 字节=32 时间=8ms TTL=55
#
# 163.177.151.110 的 Ping 统计信息:
#     数据包: 已发送 = 3，已接收 = 3，丢失 = 0 (0% 丢失)，
# 往返行程的估计时间(以毫秒为单位):
#     最短 = 5ms，最长 = 8ms，平均 = 6ms
#
# return code:  0


# -------------------------------------------------------------------------------
# 执行 python 命令
# -------------------------------------------------------------------------------
process = subprocess.Popen("python", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print("pid: ", process.pid)

# 接收输入交互性命令
process.stdin.write(b"print(1)\n")
process.stdin.writelines([b"print(2)\n", b"print(3)\n"])

# 该方法和子进程交互，返回一个包含 输出和错误的元组，如果对应参数没有设置的，则无法返回
stdout_data, stderr_data = process.communicate()
# 可以设置 encoding 参数解决编码问题
print("stdout_data:", stdout_data.decode("gbk"))
print("stderr_data:", stderr_data)

print("------------------------------------------------------------------------")
# output:
# -------------------------------------------------------------------------------
# pid:  22828
# stdout_data: 1
# 2
# 3
#
# stderr_data: b''


# -------------------------------------------------------------------------------
# 执行 python 命令
# -------------------------------------------------------------------------------
process = subprocess.Popen("python", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print("pid: ", process.pid)

# 接收输入交互性命令
# 该方法和子进程交互，返回一个包含 输出和错误的元组，如果对应参数没有设置的，则无法返回
stdout_data, stderr_data = process.communicate(input=b"print(2)\nprint(3)\n")
# 可以设置 encoding 参数解决编码问题
print("stdout_data:", stdout_data.decode("gbk"))
print("stderr_data:", stderr_data)

print("------------------------------------------------------------------------")
# output:
# -------------------------------------------------------------------------------
# pid:  20004
# stdout_data: 2
# 3
#
# stderr_data: None


# -------------------------------------------------------------------------------
# 实现类似df -Th | grep data命令的功能，实际上就是实现shell中管道的共功能
# -------------------------------------------------------------------------------
p1 = subprocess.Popen(['df', '-Th'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'data'], stdin=p1.stdout, stdout=subprocess.PIPE)
out, err = p2.communicate()
print(out)