> **March 16th, 2025**  **15:47:37** 
> **Topics:** [[Linux L2]] 
> **Tags:** #
---

**Linux Level 1: Introduction to Linux & Basic Commands**

  

**Introduction**

  

Linux is an **open-source operating system** widely used for **servers, development, cybersecurity, and embedded systems**. This lesson will introduce you to **Linux basics, file management, process control, and user permissions**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Linux Basics (Filesystem Structure, Terminal, Users & Groups)**

✅ **Essential Commands (ls, cd, cp, mv, rm, cat, grep, find)**

✅ **File & Directory Permissions (chmod, chown, umask)**

✅ **Process Management (ps, kill, top, htop, jobs, fg, bg)**

✅ **Networking Basics (ping, ifconfig, netstat, curl, wget)**

✅ **Package Management (apt, yum, pacman, snap, flatpak)**

✅ **Building a Simple Bash Script in Linux**

  

By the end of this lesson, you will be able to **navigate Linux efficiently, manage files, control processes, and automate tasks**.

---

**1. Understanding Linux & Filesystem Structure**

  

**1.1. The Linux Filesystem Hierarchy**

|**Directory**|**Purpose**|
|---|---|
|/|Root directory (everything starts here)|
|/home|User home directories|
|/etc|System configuration files|
|/var|Logs, temporary files|
|/bin|Essential user binaries (ls, cat, cp, mv)|
|/usr/bin|Installed user programs|
|/sbin|System binaries (shutdown, reboot)|
|/dev|Device files (hard drives, USB, keyboard)|
|/proc|System information (processes, CPU, memory)|

  

---

**2. Essential Linux Commands**

  

**2.1. Navigating the Filesystem**

```
pwd        # Show current directory
ls         # List files and directories
ls -l      # Detailed list with permissions
cd /home   # Change directory to /home
cd ..      # Move up one directory
cd ~       # Go to home directory
```

**2.2. File & Directory Operations**

```
touch file.txt      # Create a new empty file
mkdir new_folder    # Create a new directory
cp file.txt backup/ # Copy file to backup folder
mv file.txt docs/   # Move file to docs folder
rm file.txt         # Delete a file
rm -r folder/       # Delete a directory and its contents
```

**2.3. Viewing & Editing Files**

```
cat file.txt        # View file contents
less file.txt       # View large file (scrollable)
nano file.txt       # Edit file using Nano editor
vim file.txt        # Edit file using Vim editor
echo "Hello" > file.txt  # Write text to a file
echo "New Line" >> file.txt  # Append text to a file
```

  

---

**3. File & Directory Permissions**

  

**3.1. Checking File Permissions**

```
ls -l file.txt
```

Example output:

```
-rw-r--r--  1 user user  1024 Mar 1 10:00 file.txt
```

• r (read), w (write), x (execute)

• **First character (- or d)**: File (-) or directory (d)

• **Owner, Group, Others**: rw- r-- r-- (Owner can read/write, others can only read)

  

**3.2. Changing File Permissions**

```
chmod 755 script.sh   # Owner full, others read/execute
chmod +x script.sh    # Make file executable
chmod -w file.txt     # Remove write permission
```

**3.3. Changing Ownership**

```
sudo chown user:user file.txt  # Change file owner
sudo chown -R user:user dir/   # Change owner recursively
```

  

---

**4. Process Management**

  

**4.1. Viewing Processes**

```
ps aux        # Show running processes
top           # Interactive process viewer
htop          # Advanced process viewer (install with: sudo apt install htop)
```

**4.2. Managing Processes**

```
kill PID      # Terminate a process by ID
kill -9 PID   # Force kill a process
pkill firefox # Kill process by name
jobs          # List background processes
fg 1          # Bring process 1 to foreground
bg 1          # Move process 1 to background
```

  

---

**5. Networking Basics**

  

**5.1. Checking Network Information**

```
ip a        # Show IP address
ifconfig    # (Alternative) Show network interfaces
hostname -I # Show current IP
```

**5.2. Testing Network Connectivity**

```
ping google.com    # Check internet connectivity
wget example.com   # Download file from the internet
curl example.com   # Fetch page content
netstat -tulnp     # Show open ports and services
```

  

---

**6. Package Management**

  

**6.1. Debian-based Systems (Ubuntu, Debian)**

```
sudo apt update           # Update package list
sudo apt upgrade          # Upgrade all installed packages
sudo apt install vim      # Install a package
sudo apt remove vim       # Remove a package
```

**6.2. Red Hat-based Systems (CentOS, Fedora)**

```
sudo yum update
sudo yum install vim
sudo yum remove vim
```

**6.3. Arch-based Systems**

```
sudo pacman -Syu         # Update system
sudo pacman -S vim       # Install package
```

**6.4. Universal Package Managers**

```
snap install package    # Install a snap package
flatpak install package # Install a Flatpak package
```

  

---

**7. Creating a Simple Bash Script**

  

**7.1. Writing a Script**

1. Create a new script file:

```
nano myscript.sh
```

  

1. Add the following:

```
#!/bin/bash
echo "Hello, Linux!"
date
uptime
```

  

1. Save and exit (CTRL+X, Y, Enter).

2. Make the script executable:

```
chmod +x myscript.sh
```

  

1. Run the script:

```
./myscript.sh
```

  

---

**8. Conclusion**

  

**What You Learned in Linux Level 1:**

  

✅ **Linux Basics (Filesystem Structure, Terminal, Users & Groups)**

✅ **Essential Commands (ls, cd, cp, mv, rm, cat, grep, find)**

✅ **File & Directory Permissions (chmod, chown, umask)**

✅ **Process Management (ps, kill, top, htop, jobs, fg, bg)**

✅ **Networking Basics (ping, ifconfig, netstat, curl, wget)**

✅ **Package Management (apt, yum, pacman, snap, flatpak)**

✅ **Built a Simple Bash Script in Linux**

  

Now, you’re ready for **Linux Level 2**, where we explore **Advanced Bash Scripting, System Administration, User Management, Firewalls, and Automation!** 🚀