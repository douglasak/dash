# dash
Amazon Dash Button - Raspberry Pi Service

This is a simple script that triggers an event in openHAB if the button on the Amazon Dash is pushed. The init script can be run as a service on a Raspberry Pi.

The init script is courtesy of: http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/

Copy the dash.sh script to /etc/init.d and then you can run "sudo /etc/init.d/dash.sh start" or status or stop.

To run at startup type: "sudo update-rc.d dash.sh defaults"
