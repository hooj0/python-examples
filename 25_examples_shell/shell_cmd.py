#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-21 09:52:29
# @copyright by hoojo@2018
# @changelog Added python3 `shell->shell cmd` example


import subprocess

# help(subprocess)

print(subprocess.call('ls'))

'''
call(*popenargs, timeout=None, **kwargs)
        Run command with arguments.  Wait for command to complete or
        timeout, then return the returncode attribute.
        
        The arguments are the same as for the Popen constructor.  Example:
        
        retcode = call(["ls", "-l"])
    
    check_call(*popenargs, **kwargs)
        Run command with arguments.  Wait for command to complete.  If
        the exit code was zero then return, otherwise raise
        CalledProcessError.  The CalledProcessError object will have the
        return code in the returncode attribute.
        
        The arguments are the same as for the call function.  Example:
        
        check_call(["ls", "-l"])
    
    check_output(*popenargs, timeout=None, **kwargs)
        Run command with arguments and return its output.
        
        If the exit code was non-zero it raises a CalledProcessError.  The
        CalledProcessError object will have the return code in the returncode
        attribute and output in the output attribute.
        
        The arguments are the same as for the Popen constructor.  Example:
        
        >>> check_output(["ls", "-l", "/dev/null"])
        b'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'
        
        The stdout argument is not allowed as it is used internally.
        To capture standard error in the result, use stderr=STDOUT.
        
        >>> check_output(["/bin/sh", "-c",
        ...               "ls -l non_existent_file ; exit 0"],
        ...              stderr=STDOUT)
        b'ls: non_existent_file: No such file or directory\n'
        
        There is an additional optional argument, "input", allowing you to
        pass a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it too will be used internally.  Example:
        
        >>> check_output(["sed", "-e", "s/foo/bar/"],
        ...              input=b"when in the course of fooman events\n")
        b'when in the course of barman events\n'
        
        If universal_newlines=True is passed, the "input" argument must be a
        string and the return value will be a string rather than bytes.
    
    getoutput(cmd)
        Return output (stdout or stderr) of executing cmd in a shell.
        
        Like getstatusoutput(), except the exit status is ignored and the return
        value is a string containing the command's output.  Example:
        
        >>> import subprocess
        >>> subprocess.getoutput('ls /bin/ls')
        '/bin/ls'
    
    getstatusoutput(cmd)
        Return (status, output) of executing cmd in a shell.
        
        Execute the string 'cmd' in a shell with 'check_output' and
        return a 2-tuple (status, output). The locale encoding is used
        to decode the output and process newlines.
        
        A trailing newline is stripped from the output.
        The exit status for the command can be interpreted
        according to the rules for the function 'wait'. Example:
        
        >>> import subprocess
        >>> subprocess.getstatusoutput('ls /bin/ls')
        (0, '/bin/ls')
        >>> subprocess.getstatusoutput('cat /bin/junk')
        (256, 'cat: /bin/junk: No such file or directory')
        >>> subprocess.getstatusoutput('/bin/junk')
        (256, 'sh: /bin/junk: not found')
    
    run(*popenargs, input=None, timeout=None, check=False, **kwargs)
        Run command with arguments and return a CompletedProcess instance.
        
        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them.
        
        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.
        
        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.
        
        There is an optional argument "input", allowing you to
        pass a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.
        
        The other arguments are the same as for the Popen constructor.
        
        If universal_newlines=True is passed, the "input" argument must be a
        string and stdout/stderr in the returned object will be strings rather than
        bytes.
'''
        
