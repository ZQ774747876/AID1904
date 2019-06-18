"""
信号方法处理僵尸进程
"""
import signal
import os
#子进程退出时，父进程会忽略，此时紫禁城自动由系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
