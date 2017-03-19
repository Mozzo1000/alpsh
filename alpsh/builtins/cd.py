import os
from alpsh.constants import *

def cd(args):	
	#If there is any arguments typed
	if len(args) > 0:
		#And if the argument typed is a folder
		if os.path.isdir(args[0]):
			#Then change the directory to the one specified in the args
			os.chdir(args[0])
		else:
			#The argument specified is NOT a directory, aka directory not found
			print("Directory not found!")
	else:
		#No argument typed, change directory to the users home folder
		os.chdir(os.path.expanduser('~'))
	return SHELL_STATUS_RUN
