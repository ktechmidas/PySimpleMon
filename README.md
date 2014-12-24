Very simple script to ping a remote IP address and inform user via PushBullet when it is down. I use this to monitor my fully featured monitoring system (Usually Nagios) and inform me if that is down. 

Should work on /most/ Linux distributions with Python installed.

==Instructions==

You will need a PushBullet account and your API key:
https://docs.pushbullet.com/http/

Replace the following in the script with your key:
[PUT YOUR PUSHBULLET TOKEN HERE]

The script is set up to be "fire and forget" as it will generate a thread and continue if the user leaves the session after setting up.

==To Run==

Use: python monit.py 1.2.3.4

(Replacing 1.2.3.4 with the actual address you would like to monitor)

==TODO==

- The script will currently check every 5 minutes, when it is down it will check every hour and notify the user by PushBullet.
--This needs to be variable and changable, the user should be able to acknowledge the alert.

-A way to kill the script without having to kill the process. (Daemon?)
