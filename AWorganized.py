#todo: research lynis, auditd, bum, hardinfo, bastille, nessus, openVAS
import os

# ================================================================================
# these color codes were taken and edited from
# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'

    def disable(self):
        self.PINK = ''
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.WHITE = ''
        self.CYAN = ''
        self.ENDC = ''
# ================================================================================










# ================================================================================
# PRE-SCRIPT SYSTEM EXAMINATION
print(bcolors.RED + "Looking at what has already been done before we install some stuff..." + bcolors.ENDC)
os.system("mkdir ~/Desktop/prescriptfiles")
os.system("cp /var/log/dpkg* ~/Desktop/prescriptfiles")
os.system("cp -r /var/log/apt ~/Desktop/prescriptfiles")

# make a file to store information about /etc/group,passwd
os.system("touch ~/Desktop/prescriptfiles/origallusers.log ~/Desktop/prescriptfiles/origpasswd.log ~/Desktop/prescriptfiles/origgroup.log")
# save list of users
os.system("awk -F':' '{ print $1}' /etc/passwd > ~/Desktop/prescriptfiles/origallusers.log")
# list of groups
os.system("cat /etc/group > origgroup.log")
# list of users with their hashed passwords
os.system("cat /etc/passwd > origpasswd.log")
# ================================================================================










# ================================================================================
# INSTALLING PACKAGES
def installPackage(package):
    print(bcolors.CYAN + "Installing " + package + "..." + bcolors.ENDC)
    installCommand = "sudo apt-get -y install " + package
    os.system(installCommand)
    print(bcolors.GREEN + package + " installed successfully." + bcolors.ENDC)

installPackage("clamav")
installPackage("unhide")
installPackage("rkhunter")
installPackage("chkrootkit")
installPackage("logwatch libdate-manip-perl")
installPackage("ufw")
installPackage("gufw")
installPackage("tiger")
installPackage("nmap")
installPackage("apparmor apparmor-profiles")
installPackage("bum")
installPackage("lynis")
installPackage("hardinfo")
installPackage("auditd")
# ================================================================================










# ================================================================================
# AUTOWIN BASE DIRECTORY
print(bcolors.RED + "Building a directory on your Desktop to store outputs, and other useful data." + bcolors.ENDC)
os.system("""
cd ~/Desktop;
mkdir autowin;

cd autowin;
mkdir processes users general logs scans configs network;

cd processes;
touch psauxoutput.log;
cd ..;

cd users;
touch allusers.log passwd.log group.log;
cd ..;

cd general;
cd ..;

cd logs;
touch varlog.log;
cd ..;

cd scans;
cd ..;

cd configs;
mkdir var;
cd ..;

cd network;
touch nmapports.log hosts.log;
cd ..;

""")
print(bcolors.GREEN + "Directory created successfully on your Desktop." + bcolors.ENDC)
##dir (~/Desktop/): +autowin
##dir (~/D/autowin): +processes +users +general +logs +scans +configs
##files (~/D/a/users): +allusers.log +passwd.log +group.log
### TODO: go back later, once I have a more definite idea of what files and
### folders I need, and comment a nice, detailed tree chart of all of it.
# ================================================================================









# ================================================================================
### PROCESSES
print(bcolors.RED + "Looking through processes..." + bcolors.ENDC)
print(bcolors.YELLOW + "Saving output to processes/psauxoutput.log" + bcolors.ENDC)
os.system("ps aux > ~/Desktop/autowin/processes/psauxoutput.log")

print(bcolors.YELLOW + "Saving crontab config files to processes/" + bcolors.ENDC)
os.system("cp /etc/cron* ~/Desktop/autowin/processes/")
### should I change this later to show the path of a different place?
# ================================================================================











# ================================================================================
### SOURCES.LIST
os.system("""
cd /etc;
cp sources.list sources.list.backup;
rm sources.list;
wget https://help.ubuntu.com/12.04/sample/sources.list;
""")
## TODO: do I want to have this set to multiple urls, just in case this one goes down?
# ================================================================================












# ================================================================================
### UPDATES AND PATCHES
print(bcolors.RED + "Installing updates and patches for programs..." + bcolors.ENDC)
os.system("sudo apt-get autoclean")
print(bcolors.GREEN + "Autoclean installed successfully." + bcolors.ENDC)
os.system("sudo apt-get update -y")
print(bcolors.GREEN + "Updated successfully.")
os.system("sudo apt-get upgrade -y")
print(bcolors.GREEN + "Upgraded successfully.")
print(bcolors.CYAN + "Cleaning once more..." + bcolors.ENDC)
os.system("sudo apt-get autoclean")
# ================================================================================











# ================================================================================
### LOGS
print(bcolors.YELLOW + "Saving /var/log to logs/varlog.log" + bcolors.ENDC)
os.system("ls /var/log > ~/Desktop/autowin/logs/varlog.log")
# ================================================================================











# ================================================================================
# USERS
print(bcolors.RED + "Configuring accounts and their passwords..." + bcolors.ENDC)
print(bcolors.YELLOW + "Saving output to users/passwd.log" + bcolors.ENDC)
os.system("cat /etc/passwd > ~/Desktop/autowin/users/passwd.log")

print(bcolors.YELLOW + "Saving list of groups to users/group.log" + bcolors.ENDC)
os.system("cat /etc/group > ~/Desktop/autowin/users/group.log")

print(bcolors.YELLOW + "Saving list of users to users/allusers.log" + bcolors.ENDC)
os.system("cut -d: -f1 < /etc/passwd | sort > ~/Desktop/autowin/users/allusers.log")
# ================================================================================











# ================================================================================
## PASSWORD EXPIRATION
print(bcolors.YELLOW + "Editing password expiration preferences..." + bcolors.ENDC)
os.system('sudo sed -i "/99999/ s// 90/" /etc/login.defs')
os.system('sudo sed -i "/PASS_MIN_DAYS  0/ s//PASS_MIN_DAYS  10/" /etc/login.defs')
print(bcolors.GREEN + "Preferences altered successfully.")
# ================================================================================











# ================================================================================
## ACCOUNT LOCKOUTS
#print(bcolors.YELLOW + "Enabling account lockout..." + bcolors.ENDC)
#os.system('sudo echo "auth  required  pam_tally2.so deny=5 onerr=fail unlock_time=1800" >> /etc/pam.d/common-auth')
#print(bcolors.GREEN + "Preferences altered successfully. Be careful.")

# This shall be disabled for now, as this thing locked me out last practice image...
# ================================================================================








# ================================================================================
## AUDITING
#os.system("auditctl -e 1")
#print(bcolors.GREEN + "Auditing enabled." + bcolors.ENDC)
# ================================================================================









# ================================================================================
# CONFIGURATION FILES
print(bcolors.RED + "Beginning to duplicate important config files..." + bcolors.ENDC)
os.system("cp /etc/lightdm/lightdm.conf ~/Desktop/autowin/configs/lightdm.conf")
os.system("cp /var/www/* ~/Desktop/autowin/configs/var/")
# ================================================================================











# ================================================================================
# MEDIA FILES
# courtesy of https://github.com/JoshuaTatum/cyberpatriot/blob/master/harrisburg-linux.sh

def findAndDelete(directory,extension):
    deleteCommand = "find " + directory + " -name " + extension + " -type f -delete"
    os.system(deleteCommand)

print(bcolors.RED + "Deleting media files..." + bcolors.ENDC)
### from root directory
## TODO:  print out the files it is deleting, or copy them somewhere else...
## TODO: ... so that I can answer the questions.
findAndDelete("/","'*.mp3'")
findAndDelete("/","'*.mov'")
findAndDelete("/","'*.mp4'")
findAndDelete("/","'*.avi'")
findAndDelete("/","'*.mpg'")
findAndDelete("/","'*.mpeg'")
findAndDelete("/","'*.flac'")
findAndDelete("/","'*.m4a'")
findAndDelete("/","'*.flv'")
findAndDelete("/","'*.ogg'")
# ================================================================================











# ================================================================================
### from home directory
findAndDelete("/home","'*.gif'")
findAndDelete("/home","'*.png'")
findAndDelete("/home","'*.jpg'")
findAndDelete("/home","'*.jpeg'")
print(bcolors.GREEN + "Media files deleted." + bcolors.ENDC)
# ================================================================================











# ================================================================================
# NETWORK
print(bcolors.RED + "Scanning open ports..." + bcolors.ENDC)
os.system("nmap localhost > ~/Desktop/autowin/network/nmapports.log")

print(bcolors.YELLOW + "Saving hosts file to network/hosts.log" + bcolors.ENDC)
os.system("cat /etc/hosts > ~/Desktop/autowin/network/hosts.log")

print(bcolors.RED + "Enabling firewall..." + bcolors.ENDC)
os.system("sudo ufw enable")
# ================================================================================











# ================================================================================
## TODO: Going to have to find more ports to block...
#Block NFS
os.system("iptables -A INPUT -p tcp -s 0/0 -d 0/0 --dport 2049 -j DROP")
os.system("iptables -A INPUT -p udp -s 0/0 -d 0/0 --dport 2049 -j DROP")

#Block X-Windows
os.system("iptables -A INPUT -p tcp -s 0/0 -d 0/0 --dport 6000:6009 -j DROP")

#Block X-Windows font server
os.system("iptables -A INPUT -p tcp -s 0/0 -d 0/0 --dport 7100 -j DROP")

#Block printer port
os.system("iptables -A INPUT -p tcp -s 0/0 -d 0/0 --dport 515 -j DROP")
os.system("iptables -A INPUT -p udp -s 0/0 -d 0/0 --dport 515 -j DROP")

#Block Sun rpc/NFS
os.system("iptables -A INPUT -p tcp -s 0/0 -d 0/0 --dport 111 -j DROP")
os.system("iptables -A INPUT -p udp -s 0/0 -d 0/0 --dport 111 -j DROP")

#Deny outside packets from internet which claim to be from your loopback interface.
os.system("iptables -A INPUT -p all -s localhost  -i eth0 -j DROP")

# AUDITING
os.system("sudo lynis -c -Q")
# The question will be, where and how are these logs saved?
# ================================================================================











# ================================================================================
# ROOTKITS
print(bcolors.RED + "Using rkhunter to detect rootkits..." + bcolors.ENDC)
os.system("sudo rkhunter --check --sk")
print(bcolors.YELLOW + "Saving output to scans/rkhunter.log" + bcolors.ENDC)
os.system("cat /var/log/rkhunter.log > ~/Desktop/autowin/scans/rkhunter.log")
print(bcolors.RED + "Using chkrootkit to detect rootkits..." + bcolors.ENDC)
os.system("sudo chkrootkit")
# ================================================================================










# ================================================================================
# ANTIVIRUSES
## This part should be done last, as it will take the most time.
## I want to get most of the points in the shortest amount of time, of course.
## That means I want to get finished with this and start reading thorugh the logs.


#print(bcolors.RED + "Launching tiger..." + bcolors.ENDC)
#os.system("sudo tiger")

## TODO: tiger isn't working for crap right now... eventualy replace it with...
## TODO: something else or try to fix it.


### TODO # add something that will save the output log for tiger into the dir
print(bcolors.RED + "Now scanning with ClamAV" +bcolors.ENDC)
os.system("clamscan -r --quiet --bell /home")
# ================================================================================



# add command for unhide

# add thing to manage users and groups

# turn off automatic login




exit()
