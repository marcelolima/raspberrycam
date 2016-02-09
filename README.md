Raspberry Motion Cam
====================
Personal project to create a IP Camera using RPI and a Wifi Dongle. It also automatically uploads the videos to a google drive account.


Files
=====
uploader.cfg:
		Fill your gmail data

script_ip.py:
		Send the local(eth0, eth1 and wlan0) 
		and public IP to the specified email address  

uploader.py:
		Upload the captured motion to gdrive and
		send an email

motion-mmalcam.cfg:
		Motion detection and camera settings

records folder:
		Store the videos (will delete them after uploading)
		
Usage
=====
1) Execute
		$ sudo chmod +x script_ip.py

2) Add these lines to /etc/rc.local (before the exit function)

	python [PATH_TO_mmal]/script_ip.py
	(this will make the raspberry send its IP address when it boots)
and
	[PATH_TO_mmal]/motion -c [PATH_TO_mmal]/motion-mmalcam.conf
	(this will start motion on daemon)


3) Check if /etc/rc.local is executable

4) Configure the wireless adapter to auto-connect on boot:
   Use those configurations on /etc/network/interfaces
	auto wlan0
	allow-hotplug wlan0
	iface wlan0 inet dhcp
	wpa-ssid "SSID"
	wpa-psk "PASSWORD"

5) See what dependencies you are missing using

	$ sudo apt-get -s install motion
  
   And install each one.

