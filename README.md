Sleep prevention during Internet use
==============

This is a launch daemon that will prevent OS X from sleeping during internet use. In Mavericks, OS X will sleep the machine without regard to the current internet usage (rather annoying if you are uploading/downloading a large file). The launchd daemon is used to set the sleep parameter of pmset based on a sample of the current internet traffic. The default configuration only prevents sleep while connected to AC power. The script is launched every 30 minutes to check the current internet usage.

Installation
--------------

1) Place netmonitor.py in the following directory

	/usr/local/bin/netmonitor.py

Note: permissions should be 774

2) Place com.markedmonds.netmonitor.plist in the following directory:

	/Library/LaunchDaemons/com.markedmonds.netmonitor.plist

Note: permissions should be 644 and root should be the owner

3) Run the following commands to tell launchd to run the new script

	sudo launchctl load -w /Library/LaunchDaemons/com.markedmonds.netmonitor.plist

Configuration
--------------

The script can be modified to have higher or lower thresholds. The default is set to 60KB after sampling for a period of 10 seconds. The script sets the computer to sleep after 20 minutes if the threshold is not met. The pmset command can be changed to include all power management configurations (such as battery and AC, or just battery). The scripts defaults to only disabling sleep while connected to AC power. All of these values can be adjusted in netmonitor.py.

The launch daemon plist is set to run every 30 minutes (1800 seconds). This too can be adjusted.

Should you adjust any values in the plist, you need to reload the launch daemon with launchctl:

	sudo launchctl unload -w /Library/LaunchDaemons/com.markedmonds.netmonitor.plist

	sudo launchctl load -w /Library/LaunchDaemons/com.markedmonds.netmonitor.plist
