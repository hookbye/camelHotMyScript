# -*- coding : utf-8 -*-

import sys
import os

def gitCmd(cmd):
	os.system("" + cmd)

def gitPush():
	gitCmd("git add -A")
	commitInfo = raw_input()
	print commitInfo == ""
	if commitInfo == "":
		commitInfo = "\"quick commit for save\""
	gitCmd("git ci -m "+commitInfo)
	gitCmd("git pl")
	gitCmd("git ps")
if __name__ == '__main__':
	gitPush()