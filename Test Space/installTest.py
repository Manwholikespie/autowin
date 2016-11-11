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

def installPackage(package):
    print bcolors.CYAN + "Installing " + package + "..." + bcolors.ENDC
    installCommand = "sudo apt-get -y install " + package
    print installCommand
    print bcolors.GREEN + package + " installed successfully.\n" + bcolors.ENDC

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
