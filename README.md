Sleep prevention during Internet use
==============

This is a launch daemon that will prevent OS X from sleeping during internet use. The launchd daemon is used to set the sleep parameter of pmset based on a sample of the current internet traffic. The script is launch every 30 minutes to check the current internet usage.

Installation
--------------

The main script, netmonitor.sh, relies on the following:

1) netstat (should be installed already)
2) gtimeout (a part of coretutils)

Steps
--------------

1) Make sure coreutils is installed

	brew install coreutils

2) Place netmonitor.sh in the following directory

	/usr/local/bin/netmonitor.sh

Note: permissions should be 774

3) Place com.markedmonds.netmonitor.plist in the following directory:

	/Library/LaunchDaemons/com.markedmonds.netmonitor.plist

Note: permissions should be 644 and root should be the owner

4) Run the following commands to tell launchd to run the new script

	sudo launchctl load -w /Library/LaunchDaemons/com.markedmonds.netmonitor.plist

Configuration
--------------

The script can be modified to have higher or lower thresholds. The default is set to 60KB after sampling for a period of 10 seconds. The script sets the computer to sleep after 20 minutes if the threshold is not met. All of these values can be adjusted in netmonitor.sh.

The launch daemon plist is set to run every 30 minutes (3600 seconds). This too can be adjusted.