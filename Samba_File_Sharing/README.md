# Samba File Sharing
## Installation

1. Open the Raspberry Pi terminal
2. Enter this command to fully update your raspberry pi: `sudo apt update -y && sudo apt update --fix-missing -y && sudo apt-get update -y && sudo apt-get update --fix-missing -y && sudo apt upgrade -y && sudo apt upgrade --fix-missing -y && sudo apt full-upgrade -y && sudo apt full-upgrade --fix-missing -y && sudo apt autoremove -y && sudo apt autoremove --fix-missing -y && sudo apt clean -y`
3. Enter this command to install Samba and Samba Common Bin: `sudo apt install samba samba-common-bin -y`
4. Next we need to set a folder to share. To do so enter this command: `sudo nano /etc/samba/smb.conf`
5. Navigate to the bottom of this file and add these lines (Make sure you change the YourPiUsername to you Raspberry Pi's username);

[Shared-Pi]  
path=/home/YourPiUsername  
writeable=Yes  
create mask=0777  
directory mask=0777  
public=no

6. 
