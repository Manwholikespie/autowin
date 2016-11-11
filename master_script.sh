#!/bin/bash

#---Updates the software of the operating system---#
########## DONE DONE DONE ##########
echo "Upgrading software..."
sudo apt-get update -y && apt-get upgrade -y
echo "Done!"

echo; echo
########## DONE DONE DONE ##########





#---Changes the password requirments---#
echo "Password requirment changer starting..."
echo
echo "Securing basic password..."
sudo sed -i "/pam_unix.so/ s/$/ remember=5/" /etc/pam.d/common-password | grep pam_unix.so
echo "Operation complete."
echo "--->> installing cracklib so we can get more secure passwords."
sudo apt-get install libpam-cracklib
echo "Done."
echo "Securing cracklib..."
sudo sed -i "/pam_cracklib.so/ s/$/ ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1/" /etc/pam.d/common-password | grep pam_cracklib.so
echo "Changing your password..."
echo "Please set your new password to Mu$tangs1"
passwd
echo "Done."
echo

########## DONE DONE DONE ##########
#---Add password expiration---#
echo "Adding password expiration..."
sudo sed -i "/99999/ s// 90/" /etc/login.defs
sudo sed -i "/PASS_MIN_DAYS  0/ s//PASS_MIN_DAYS  10/" /etc/login.defs
echo "Done."
echo "Adding lockout..."
sudo echo "auth  required  pam_tally2.so deny=5 onerr=fail unlock_time=1800" >> /etc/pam.d/common-auth
echo "Done."
#---Activate auiditing---#
echo "Installing auditing tools..."
sudo apt-get install auditd
echo "Done."
echo "Enabling auditing..."
auditctl -e 1
echo "Done"
########## DONE DONE DONE ##########


#---list and delete user accounts---#
function delete {
cut -d: -f1 /etc/passwd
echo "Enter the user account you would like to delete:"
read baduser
sudo userdel -rf "$baduser"
echo "Would you like to delete another?"
read answer
if [ $answer = yes ]
then
    delete
else
    echo
    echo "Done!"
    echo
fi }
delete

#---Remove guest account---#
cat /etc/lightdm/lightdm.conf
echo "If this file does not deny guest access answer y or if it does answer n:"
read input

if [ $input = "y" ]
then
    echo "allow-guest=false" >> /etc/lightdm/lightdm.conf
fi

#---Firewall activation---#
echo "enabling firewall..."
sudo ufw enable
sudo ufw status verbose
echo "If this is not set to deny incoming and allow outgoing then say reset otherwise say ok"
read input
if [ $input = "yes" ]
then
    sudo ufw reset
fi
echo "Done."

#---Enable service viewing---#
echo "Installing bum..."
sudo apt-get install bum
echo "Done"
echo "Running bum..."
bum

echo "This script has completed"
