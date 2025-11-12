# inet_4031_adduser_script
INET4031 Add Users Script and User List

## Program Description

This program automates the process of adding users to a system, setting up the password, and assigning groups. Normal commands for this task would be to use $ sudo adduser user01. This program uses the file create-users.input to retrieve the usernames and automatically adding the users to their groups rather than doing so individually.
 
## Program User Operation

Every user added has 5 fields made up of the username, password, LastName, FirstName, and group.

## Input File Format

The fields are separated with colons and will only be accepted if it matches exactly 5 fields. If not, it will continue.Using match, if a line starts with a "#" it will skip it and not be added.

## Command Execution

The code should be run by using the command ./create-users.py < createusers.input and if the file is not executed, use chmod a+x create-users.py

## "Dry Run"

To ensure there are no errors, doing a dry run to test the code should be done by commenting out the os commands. This prevents the system from actually adding users allows for testing to check if certain parts are working.
