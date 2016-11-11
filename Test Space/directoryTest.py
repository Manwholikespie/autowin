import os

#os.system("cd ~/Desktop && mkdir autowin && cd autowin && mkdir processes users general logs scans configs network && cd users && touch allusers.log passwd.log group.log")

os.system("""
cd /Users/robert/Documents/Prog/AutoWin/Test\ Space;
mkdir autowin;
cd autowin;
mkdir processes users general logs scans configs network;
cd users;
touch allusers.log passwd.log group.log
""")
