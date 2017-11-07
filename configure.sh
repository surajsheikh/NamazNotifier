#!/bin/bash
sudo apt-get update
sudo apt-get install python3 notify-osd python3-pip python3-tk at git
sudo pip3 install termcolor
sudo rm -rf /etc/NamazNotifier
sudo git clone https://surajsheikh:ca29066e4c937ee42bdbfbd7028dfe4534d14e41@github.com/surajsheikh/NamazNotifier.git /etc/NamazNotifier

sudo cp /etc/NamazNotifier/NamazNotifier.py /bin
#write out current crontab
sudo crontab -l > mycron
#echo new cron into cron file
echo "@reboot python3 /etc/NamazNotifier/NamazNotifier.py &" >> mycron
#install new cron file
sudo crontab mycron
sudo rm mycron

sudo python3 /etc/NamazNotifier/NamazNotifier.py manual
python3 /etc/NamazNotifier/NamazNotifier.py
