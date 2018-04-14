#!/bin/bash
sudo apt-get update
sudo apt-get install python3 notify-osd python3-pip python3-tk at git
sudo pip3 install termcolor
sudo rm -rf /tmp/NamazNotifier
git clone https://surajsheikh:ca29066e4c937ee42bdbfbd7028dfe4534d14e41@github.com/surajsheikh/NamazNotifier.git /tmp/NamazNotifier

sudo cp /tmp/NamazNotifier/NamazNotifier.py /bin
sudo chmod 555 /bin/NamazNotifier.py

#write out current crontab
crontab -l > mycron
#echo new cron into cron file
export pyt = `which python3`
grep -v 'NamazNotifier' mycron > mycront
echo "@reboot $pyt /bin/NamazNotifier.py &" >> mycront
echo "30 00 * * * $pyt /bin/NamazNotifier.py" >> mycront
cat mycront
#install new cron file
#sudo crontab mycront
#sudo rm mycron
#sudo rm mycront

#sudo python3 /etc/NamazNotifier/NamazNotifier.py manual
#python3 /etc/NamazNotifier/NamazNotifier.py
