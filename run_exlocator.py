#!/usr/bin/env python
#coding:utf-8

import os
import sys
import commands

def main():
    len(sys.argv)
    dir = sys.argv[1]
    for folder in os.listdir(dir):
        path = os.path.join(dir,folder)
        cmd = 'java -jar CrashTester.jar %s'%path 
        os.system(cmd)
if __name__ == '__main__':
	main()
