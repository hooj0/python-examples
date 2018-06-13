###进程管理
###os模块提供了许多进程管理相关的操作，如果熟悉Unix下的系统编程的话，那么看到这些函数会觉得很熟悉，因为这些函数都是对相应的C API的Python实现，让我们看看都有些什么函数：

'''
os.abort()
向调用该函数的进程发送一个SIGABRT信号，在Unix系统上默认的行为是产生一个core文件。
注意：当调用os.abort()函数的时候不会调用python的信号处理函数signal.signal()。

os.exe系列函数
os.execl(path, arg0, arg1, ...)
os.execle(path, arg0, arg1, ..., env)
os.execlp(file, arg0, arg1, ...)
os.execlpe(file, arg0, arg1, ..., env)
os.execv(path, args)
os.execve(path, args, env)
os.execvp(file, args)
os.execvpe(file, args, env)

这些函数都执行一个新的程序，然后用新的程序替换当前子进程的进程空间，而该子进程从新程序的main函数开始执行。在Unix下，该新程序的进程id是原来被替换的子进程的进程id。在原来子进程中打开的所有描述符默认都是可用的，不会被关闭。
execv*系列的函数表示其接受的参数是以一个list或者是一个tuple表示的参数表
execl*系列的函数表示其接受的参数是一个个独立的参数传递进去的。
exec*p*系列函数表示在执行参数传递过去的命令时使用PATH环境变量来查找命令
exec*e系列函数表示在执行命令的时候读取该参数指定的环境变量作为默认的环境配置，最后的env参数必须是一个mapping对象，可以是一个dict类型的对象。

os._exit(n)
退出进程，并且返回退出状态n，在退出的时候不会执行清理工作，直接退出。
注意：正常的退出应该使用sys.exit(n)，而_exit()函数一般只用在fork之后的子进程中调用以退出。

可用的退出状态(并不适用所有的Unix平台都可用):
os.EX_OK - 正常退出
os.EX_USAGE - 命令执行不正确，如命令参数错误
os.EX_DATAERR - 输入数据有误
os.EX_NOINPUT - 输入文件不存在或者不可读
os.EX_NOUSER - 指定的用户不存在
os.EX_NOHOST - 指定的主机id不存在
os.EX_UNAVAILABLE - 请求的服务不可用
os.EX_SOFTWARE - 内部软件错误
os.EX_OSERR - 操作系统错误
os.EX_OSFILE - 系统文件不存在
os.EX_CANTCREAT - 无法创建指定的输出文件
os.EX_IOERR - 在进行I/O操作时出错
os.EX_PROTOCOL - 协议切换操作非法，或者协议切换不可用
os.EX_NOPERM - 没有权限执行该操作
os.EX_CONFIG - 配置错误

os.fork()
fork出一个子进程，在子进程中返回0，在父进程中返回子进程ID，如果发生错误，则抛出OSError异常
注意：在一些平台下如FreeBSD，Cygwin和OS/2 EMX系统中使用该函数会有问题。

os.kill(pid, sig)
发送一个信号sig给进程id为pid的进程

os.nice(increment)
增加increment到进程的nice值，返回一个新的nice值。

os.system(command)
在一个shell中执行command命令，这是一个对C函数system()的python实现，具有相同的限制条件。在Unix系统中，返回值是命令执行后的退出状态值。由于POSIX没有为C函数system()的返回值指定明确的含义，所以os.system()的返回值依赖具体的系统。

os.times()
返回一个由浮点数组成的5元组，指定进程的累积运行时间，单位为秒(s)。时间包括：user time，system time，子进程的user time，子进程的system time 以及一个经过的墙上钟表时间。

os.wait()
等待任何一个子进程结束，返回一个tuple，包括子进程的进程ID和退出状态信息：一个16位的数字，低8位是杀死该子进程的信号编号，而高8位是退出状态(如果信号编号是0)，其中低8位的最高位如果被置位，则表示产生了一个core文件。

os.waitpid(pid, options)
等待进程id为pid的进程结束，返回一个tuple，包括进程的进程ID和退出信息(和os.wait()一样)，参数options会影响该函数的行为。在默认情况下，options的值为0。
如果pid是一个正数，waitpid()请求获取一个pid指定的进程的退出信息，如果pid为0，则等待并获取当前进程组中的任何子进程的值。如果pid为-1，则等待当前进程的任何子进程，如果pid小于-1，则获取进程组id为pid的绝对值的任何一个进程。当系统调用返回-1时，抛出一个OSError异常。

os.wait3(options)
和waitpid()函数类似，区别是不需要指定pid，函数返回一个3元组，包括结束的子进程的进程id，退出状态以及资源的使用信息。关于资源使用可以使用resource.getusage()来获取详细的信息。

os.wait4(pid, options)
和waitpid()函数类似，但是函数返回一个3元组外，这点和wait3()函数类似。

waitpid()函数的options选项：
os.WNOHANG - 如果没有子进程退出，则不阻塞waitpid()调用
os.WCONTINUED - 如果子进程从stop状态变为继续执行，则返回进程自前一次报告以来的信息。
os.WUNTRACED - 如果子进程被停止过而且其状态信息还没有报告过，则报告子进程的信息。
 

如下的函数用于处理那些自system()，wait()和waitpid()返回的状态信息，并将这些状态信息作为如下函数的参数传递。
os.WCOREDUMP(status)
如果一个core文件被创建，则返回True，否则返回False。

os.WIFCONTINUED(status)
如果一个进程被停止过，并且继续执行，则返回True，否则返回False。

os.WIFSTOPPED(status)
如果子进程被停止过，则返回True，否则返回False。

os.WIFSIGNALED(status)
如果进程由于信号而退出，则返回True，否则返回False。

os.WIFEXITED(status)
如果进程是以exit()方式退出的，则返回True，否则返回False。

os.WEXITSTATUS(status)
如果WIFEXITED(status)返回True，则返回一个整数，该整数是exit()调用的参数。否则返回值是未定义的。

os.WSTOPSIG(status)
返回导致进程停止的信号

os.WTERMSIG(status)
返回导致进程退出的信号
'''
import os


'''
向调用该函数的进程发送一个SIGABRT信号，在Unix系统上默认的行为是产生一个core文件。
注意：当调用os.abort()函数的时候不会调用python的信号处理函数signal.signal()。
'''
#print(os.abort())

'''
os.exe系列函数
'''
#print(os.execl("C:\Windows\System32\cmd.exe", "ping 127.0.0.1"))
#print(os.execle("C:\Windows\System32\cmd.exe", "javac -version", "JAVA_HOME"))
#print(os.execle('f:\foo.txt'))

#print(os.execlp('f:\foo.txt'))

##os.execv("F:/Example Exercise/Python/example_3/run.py")

# 打开文件
fd = os.open("F:/Example Exercise/Python/example_3/run.py", os.O_RDWR|os.O_CREAT)
print(os.fdopen(fd))

print(os.fsdecode("哈"))
print(os.fsencode("哈"))

print(os.fspath("F:/Example Exercise/Python/example_3/run.py"))

print(os.pipe())
