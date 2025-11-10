#!/usr/bin/python3

# INET4031
# Your Name
# Data Created
# Date Last Modified

#import os is used to interact with operating system, import re used to provide regular expression operations.
#import sys used to provide access to system specific functions for Python.
import os
import re
import sys


def main():
    dry_run_input = input("Run in dry-run mode? (Y/N): ").strip().upper()
    dry_run = dry_run_input == "Y"

    for line in sys.stdin:

        #For every line, checks code for lines that start with "^#"
        match = re.match("^#",line)

        #Separates lines with  ":" to separate variables
        fields = line.strip().split(':')

        #The if statement is used to pass over lines where either match or length of fields does not equal 5 so that it doesn't
	#add data fields to an empty group.
        if match or len(fields) != 5:
            continue

        #Assigns username to the first field and password to the next field. gecos is used to add the fields for the second and third entries together.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #The split is being done to split the groups with a comma.
        groups = fields[4].split(',')

        #Shows a message for the user of the account being created.
        print("==> Creating account for %s..." % (username))
        #Command to create the account by using gecos
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #If uncommented, it will begin to add users to the system.
        #print cmd
        #os.system(cmd)

        #Shows a messagge of the password being set for the user.
        print("==> Setting the password for %s..." % (username))
        #Make a command to set the password for the user.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #If uncommented, it will run the command to set the password.
        #print cmd
        #os.system(cmd)

        for group in groups:
            #If the group has an actual value, add the user to the group and run adduser command.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
