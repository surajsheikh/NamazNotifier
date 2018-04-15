#!/bin/bash
sudo apt-get update
sudo apt-get install python3 notify-osd python3-pip python3-tk at git
sudo pip3 install termcolor
rm -rf /tmp/NamazNotifier
sudo rm -rf /etc/namaznotifier/
sudo mkdir /etc/namaznotifier/
sudo touch /etc/namaznotifier/namaznotifier.dict
sudo chmod 666 /etc/namaznotifier/namaznotifier.dict
sudo chmod 777 /etc/namaznotifier/
git clone https://surajsheikh:ca29066e4c937ee42bdbfbd7028dfe4534d14e41@github.com/surajsheikh/NamazNotifier.git /tmp/NamazNotifier

sudo cp /tmp/NamazNotifier/NamazNotifier.py /bin
sudo chmod 555 /bin/NamazNotifier.py

#write out current crontab
crontab -l > mycron
#echo new cron into cron file
pyt=`which python3`
grep -v 'NamazNotifier' mycron > mycront
echo "@reboot echo '$pyt /bin/NamazNotifier.py' | at now + 3 minutes" >> mycront
#echo "30 00 * * * $pyt /bin/NamazNotifier.py" >> mycront

#install new cron file
crontab mycront
rm mycron
rm mycront

$pyt /bin/NamazNotifier.py manual
$pyt /bin/NamazNotifier.py
