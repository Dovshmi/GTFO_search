# GTFO_search
GTFO_searching script

Hello every one,
Here is a little script I like to call
GTFO_Search!!!!!!!
this tool searches in the GTFO search engine(https://gtfobins.github.io/), after a while it print to the terminal a new table with all the Exploits.
You see this tool is a Beast!!!!

OK Ok ok, so lets see how we use it
first you wiil need to install some pips:

pip install BeautifulSoup4 # the web scraping tool.
pip insatll alive_progress # shows you the progress of the script
pip install prettytable # outputs a pretty table (:

after that:
gtfo.py /path/to/file, --help or -h for help menu

Now you ask "what "/path/to/file"/
Well, this is the SUID file that you have to input to the script.
Inside this TEXT file, you input the suids you found inside the attacked VM.

Example?

1 and only: Lets say that you have a reverse shell inside a linux VM, and you want to priv this mechine.
One very good option is to use sudo -l to see if we have some options to use sudo,
bu another option lets you to see the SUIDS for the reverse shell host.
we have two commands:
$ find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
-rwsr-xr-x 1 root root 114784 Jun 28  2021 /usr/sbin/SUID1
-rwsr-xr-x 1 root root 48128 Dec 14 12:15 /usr/sbin/SUID2
-rwsr-xr-- 1 root dip 403752 Jan  7  2021 /usr/sbin/SUID3
-rwxr-sr-x 1 root shadow 38912 Dec  6 21:11 /usr/sbin/SUID4

Or the command
$ find / -perm -u=s -type f 2>/dev/null
/usr/sbin/SUID1
/usr/bin/SUID2
/usr/bin/SUID3
/usr/lib/openssh/SUID4

Like you can see, the second options gives you a short output.
but it doesent metter, beacause you cat copy the out put of these command into a TEXT file in the attacking meechine.

Oh and if tou want to do the hard work and to create a text file only with the suid name,
like:
vim suids_to_crack.txt
SUID1
SUID2
SUID3
SUID4
:qw

Nice now you will use the script and see a table with all the information:
+-----------------------------------------+-----------------------------------------+-------------------------------------------+
|                   ssh                   |                   apt                   |                   mount                   |
+-----------------------------------------+-----------------------------------------+-------------------------------------------+
| https://gtfobins.github.io/gtfobins/ssh | https://gtfobins.github.io/gtfobins/apt | https://gtfobins.github.io/gtfobins/mount |
|                  Shell                  |                  Shell                  |                    Sudo                   |
|               File upload               |                   Sudo                  |                Null/Nothing               |
|              File download              |               Null/Nothing              |                Null/Nothing               |
|                File read                |               Null/Nothing              |                Null/Nothing               |
|                   Sudo                  |               Null/Nothing              |                Null/Nothing               |
+-----------------------------------------+-----------------------------------------+-------------------------------------------+     

![This is an image](Screemshot.png)


