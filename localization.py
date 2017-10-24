import rospy
import subprocess
from time import sleep

cmd = "/home/jacob/CLionProjects/apriltags/build/bin/apriltags_demo"
while(True):
	result = subprocess.check_output(cmd, shell=True)
	print result
	sleep(1)