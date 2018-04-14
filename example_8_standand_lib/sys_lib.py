#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import sys


print(help(sys))

print(sys.argv) # ['F:\\Example Exercise\\Python\\example_8_standand_lib\\sys_lib.py']
print(sys.flags) # sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=0, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=0)

print(sys.hash_info) # sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003, algorithm='siphash24', hash_bits=64, seed_bits=128, cutoff=0)
print(sys.copyright)

print(sys.platform) # win32
print(sys.winver) # 3.6

# 日志输入输出
sys.stdin.read(10)
sys.stdout.write('Warning, log file not found starting a new one\n')
sys.stderr.write('Warning, log file not found starting a new one\n')

# 退出
sys.exit()