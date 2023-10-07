# Samba File Sharing
## Setup

1. Open the Raspberry Pi terminal
2. Enter this command to fully update your raspberry pi: `sudo apt update -y && sudo apt update --fix-missing -y && sudo apt-get update -y && sudo apt-get update --fix-missing -y && sudo apt upgrade -y && sudo apt upgrade --fix-missing -y && sudo apt full-upgrade -y && sudo apt full-upgrade --fix-missing -y && sudo apt autoremove -y && sudo apt autoremove --fix-missing -y && sudo apt clean -y`
3. Enter this command to install Samba and Samba Common Bin: `sudo apt install samba -y samba-common-bin`
4. Next we need to set a folder to share. To do so enter this command: `sudo nano /etc/samba/smb.conf`
5. Navigate to the bottom of this file and add these lines (Make sure you change the YourPiUsername to you Raspberry Pi's username);

[Shared-Pi]  
path=/Home/YourPiUsername  
writeable=Yes  
create mask=0777  
directory mask=0777  
public=no

6. Press `ctrl+x` then when prompted `y` then press `enter`
7. Now we need to add a samba password. to do so enter this command: `sudo smbpasswd -a YourPiUsername` (Again make sure you change the YourPiUsername to you Raspberry Pi's username)
8. When prompted enter your desired password (Note the password you enter will not show up on the screen but is still being entered)
9. Then restart smb using this command: `sudo systemctl restart smbd`

## Connecting

1. First we need to find the ip address of our pi using this command: `hostname -I` make note of the first output
2. Now back in your windows pc navigate to the this pc folder and then right click and press `Add a network location`
3. Then `Next` then `Choose a custom network location` and `Next`
4. Next enter your raspberry pi's ip address after two backslashes with the folder you shared eg. `\\192.168.1.219\Home`
5. Now you Pi should appear in the this pc menu on your windows device
