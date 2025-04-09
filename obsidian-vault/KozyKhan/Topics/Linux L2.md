> **March 16th, 2025**  **15:50:54** 
> **Topics:** [[VB.Net L1]] 
> **Tags:** #CS 
---

**Linux Level 2: Intermediate to Advanced Linux Administration & Automation**

  

**Introduction**

  

Now that you’ve learned **Linux basics**, it’s time to explore **advanced shell scripting, system administration, networking, user management, security, and automation**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced Bash Scripting (Variables, Loops, Functions, Logging)**

✅ **User & Group Management (Permissions, sudo, SSH Access)**

✅ **System Monitoring & Logs (dmesg, journalctl, syslog, uptime)**

✅ **Networking & Firewalls (iptables, ufw, SSH Tunneling)**

✅ **Disk Management (fdisk, LVM, mount, fstab)**

✅ **Cron Jobs & Automation (crontab, systemd timers)**

✅ **Deploying a Web Server (Apache/Nginx, PHP, MySQL, SSL)**

✅ **Building an Automated Linux Server Maintenance Script**

  

By the end of this lesson, you will be able to **administer Linux systems efficiently, automate tasks, manage users, secure networks, and deploy web applications**.

---

**1. Advanced Bash Scripting**

  

**1.1. Using Variables & Arguments**

```
#!/bin/bash
name=${1:-"Guest"}  # Default value if no argument is given
echo "Hello, $name!"
```

Run the script:

```
./script.sh Alice
```

**1.2. Loops in Bash**

```
#!/bin/bash
for i in {1..5}; do
    echo "Iteration: $i"
done
```

**1.3. Functions in Bash**

```
#!/bin/bash
greet() {
    echo "Hello, $1!"
}
greet "Alice"
```

**1.4. Logging Script Output**

```
#!/bin/bash
logfile="/var/log/myscript.log"
echo "Script executed at $(date)" >> $logfile
```

  

---

**2. User & Group Management**

  

**2.1. Creating & Managing Users**

```
sudo useradd -m alice  # Create user
sudo passwd alice      # Set password
sudo usermod -aG sudo alice  # Add user to sudoers
```

**2.2. Managing Groups**

```
sudo groupadd developers
sudo usermod -aG developers alice
```

**2.3. Checking User & Group Information**

```
id alice
groups alice
```

**2.4. Disabling a User Account**

```
sudo passwd -l alice  # Lock account
sudo passwd -u alice  # Unlock account
```

**2.5. Managing SSH Access**

```
sudo systemctl restart ssh
nano /etc/ssh/sshd_config  # Edit SSH config (disable root login)
```

  

---

**3. System Monitoring & Logs**

  

**3.1. Checking System Performance**

```
top        # Real-time system monitoring
htop       # Advanced system monitoring (install: sudo apt install htop)
uptime     # Check system uptime
free -h    # View memory usage
```

**3.2. Viewing System Logs**

```
dmesg | tail -20       # Kernel logs
journalctl -xe         # System logs
sudo tail -f /var/log/syslog  # Real-time system logs
```

**3.3. Monitoring Active Processes**

```
ps aux | grep nginx
kill -9 <PID>
```

  

---

**4. Networking & Firewalls**

  

**4.1. Configuring Firewalls with UFW**

```
sudo ufw enable
sudo ufw allow 22       # Allow SSH
sudo ufw allow 80       # Allow HTTP
sudo ufw deny 8080      # Deny a port
sudo ufw status         # Check firewall rules
```

**4.2. Using iptables for Advanced Firewall Rules**

```
sudo iptables -L        # List rules
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT  # Allow HTTP
```

**4.3. SSH Tunneling**

```
ssh -L 8080:localhost:80 user@remote-server
```

  

---

**5. Disk Management & Storage**

  

**5.1. Checking Disk Space**

```
df -h
du -sh /home
```

**5.2. Formatting & Mounting Disks**

```
sudo mkfs.ext4 /dev/sdb1
sudo mount /dev/sdb1 /mnt
```

**5.3. Configuring fstab for Auto-Mounting**

  

Edit /etc/fstab:

```
/dev/sdb1  /mnt  ext4  defaults  0  2
```

  

---

**6. Automating Tasks with Cron Jobs**

  

**6.1. Scheduling a Job Every Day at Midnight**

```
crontab -e
```

Add the following line:

```
0 0 * * * /path/to/script.sh
```

**6.2. Running a Job Every 5 Minutes**

```
*/5 * * * * /path/to/task.sh
```

**6.3. Using systemd Timers Instead of Cron**

  

Create a systemd service /etc/systemd/system/myscript.service:

```
[Unit]
Description=Run My Script

[Service]
ExecStart=/path/to/script.sh
```

Create a systemd timer /etc/systemd/system/myscript.timer:

```
[Unit]
Description=Run My Script Every 10 Minutes

[Timer]
OnBootSec=5min
OnUnitActiveSec=10min
Unit=myscript.service

[Install]
WantedBy=timers.target
```

Enable and start:

```
sudo systemctl enable myscript.timer
sudo systemctl start myscript.timer
```

  

---

**7. Deploying a Web Server**

  

**7.1. Installing Apache & PHP**

```
sudo apt install apache2 php libapache2-mod-php
sudo systemctl start apache2
```

**7.2. Installing MySQL**

```
sudo apt install mysql-server
sudo mysql_secure_installation
```

**7.3. Configuring Apache Virtual Hosts**

  

Edit /etc/apache2/sites-available/mysite.conf:

```
<VirtualHost *:80>
    DocumentRoot /var/www/mysite
    ServerName mysite.com
    <Directory /var/www/mysite>
        AllowOverride All
    </Directory>
</VirtualHost>
```

Enable the site and restart Apache:

```
sudo a2ensite mysite.conf
sudo systemctl restart apache2
```

  

---

**8. Building an Automated Linux Server Maintenance Script**

```
#!/bin/bash

# Log file location
LOGFILE="/var/log/maintenance.log"

echo "Starting system maintenance..." >> $LOGFILE
echo "Updating system packages..." >> $LOGFILE
sudo apt update && sudo apt upgrade -y >> $LOGFILE

echo "Cleaning up unused packages..." >> $LOGFILE
sudo apt autoremove -y >> $LOGFILE

echo "Checking disk space..." >> $LOGFILE
df -h >> $LOGFILE

echo "System maintenance completed on $(date)" >> $LOGFILE
```

Make the script executable:

```
chmod +x maintenance.sh
```

Schedule it using cron:

```
crontab -e
```

Add:

```
0 3 * * 7 /path/to/maintenance.sh
```

This runs **every Sunday at 3 AM**.

---

**9. Conclusion**

  

**What You Learned in Linux Level 2:**

  

✅ **Advanced Bash Scripting (Variables, Loops, Functions, Logging)**

✅ **User & Group Management (Permissions, sudo, SSH Access)**

✅ **System Monitoring & Logs (dmesg, journalctl, syslog, uptime)**

✅ **Networking & Firewalls (iptables, ufw, SSH Tunneling)**

✅ **Disk Management (fdisk, LVM, mount, fstab)**

✅ **Cron Jobs & Automation (crontab, systemd timers)**

✅ **Deploying a Web Server (Apache/Nginx, PHP, MySQL, SSL)**

✅ **Built an Automated Linux Server Maintenance Script**

  

Now, you’re ready for **Linux Level 3**, where we explore **Linux Security, Containers (Docker, Kubernetes), High Availability, and Cloud Deployments!** 🚀