# FILES & NAVIGATING

```ls``` - directory listing (list all files/folders on current dir) <br>
```ls -l``` - formatted listing <br>
```ls-la``` - formatted listing including hidden files  <br>
```ls-t```  - list down all the files in the last modified file first order  <br>
```ls -lX``` - list down all the files sorted by filetype extension <br>
```cd dir``` - change directory to dir (dir will be directory name) <br>
```cd ..``` - change to parent directory <br>
```cd ../dir``` - change to dir in parent directory <br>
```cd``` - change to home directory <br>
```pwd``` - show current directory <br>
```mkdir dir``` - create a directory dir <br>
```rm file``` - delete file <br>
```rm-f dir ```-force remove file <br>
```rm -r dir``` -delete directory dir <br>
```rm -rf dir``` - remove directory dir <br>
```rm -rf /``` - launch some neuclear bombs targeting your system <br>
```cp file1 file2``` - copy file1 to file2 <br>
```mv file1 file2``` - rename file1 to file2 <br>
```mv file1 dir/file2``` - move file1 to dir as file2 <br>
```touch file``` - create or update file <br>
```cat file``` -output contents of file <br>
```cat > file``` - writo standard input into file <br>
```cat >> file ``` -append standard input into file <br>
```tail-f file``` -output contents of file as it grows <br>


# NETWORKING

```ping host``` - ping host <br>
```whois domain``` - got whois for domain <br>
```dig domain``` - get DNS for domain  <br>
```dig-x host``` reserve lookup host <br>
```wget file``` download file <br>
```wget-c file``` continuo stopped download <br>
```wget-r url``` -recurively download files from url <br>
```curl url``` - outputs the webpage from url <br>
```curl-o meh.htmi url``` - writes the page to meh.html  <br>
```ssh user@host``` - connect to host as user <br>
```ssh-p port user@host``` - connect using port <br>
```ssh-D user@host``` - connect & use bind port <br>


# PROCESSES

```ps``` display currently active processes <br>
```ps aux``` detailed outputs  <br>
```kill pid``` - kill process with process id (pid)  <br>
```killall proc``` - kill all processes named proc <br>

# SYSTEM INFO

```date``` show current date/time <br>
```uptime``` show uptime <br>
```whoami``` - who you're logged in as <br>
```w``` -display who is online  <br>
```cat/proc/meminfo``` - memory info  <br>
```free``` show memory and swap usage  <br>
```du-sh``` - displays readable sizes in GB <br>
```df``` - show disk usage <br>
```uname-a``` -show karnel config <br>


# PERMISSIONS

chmod octal file change permissions of file

4 - read (r); 2- write (w); 1- execute (x)

order: owner/group/world

```chmod 777``` -rwx for overyone 
```chmod 755``` - rw for owner, rx for group world

# ARCHIVING AND COMPRESSION

```tar -cvf <archive_name>.tar <directory>``` - Create a tarball.
```tar -xvf <archive_name>.tar: Extract files``` -from a tarball.
```gzip <file>``` -Compress a file.
```gunzip <file.gz>``` -Decompress a gzipped file.

