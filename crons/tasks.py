import os
import sys
import subprocess
import datetime



def tasks():
    """ Get an IP """
    cmd_ip = "ipconfig"
    os.system(cmd_ip)

    """ Get hostname """
    cmd_hostname = "hostname"
    os.system(cmd_hostname)

    """ """