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
grep -v 'NamazNotifier' mycron > mycront
echo "@reboot python3 /etc/NamazNotifier/NamazNotifier.py &" >> mycront
echo "30 00 * * * /etc/NamazNotifier/runner.sh" >> mycront
#install new cron file
sudo crontab mycront
sudo rm mycron
sudo rm mycront

sudo python3 /etc/NamazNotifier/NamazNotifier.py manual
python3 /etc/NamazNotifier/NamazNotifier.py
