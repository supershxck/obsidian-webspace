> **March 15th, 2025**  **19:08:48** 
> **Topics:** [[TypeScript L1]] 
> **Tags:** #CS 
---

**Shell Scripting Level 2: Advanced Bash Scripting & Automation**

  

**Introduction**

  

Now that you’ve mastered **basic shell scripting**, it’s time to explore **advanced topics like automation, file processing, networking, and system monitoring**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Working with Arrays & Associative Arrays**

✅ **AWK & Sed for Text Processing**

✅ **Networking & Process Management**

✅ **Error Handling & Debugging Scripts**

✅ **Automating System Administration Tasks**

✅ **Scheduling Jobs & Log Monitoring**

✅ **Building a Full Shell Automation System**

  

By the end of this lesson, you will be able to **write advanced shell scripts for automation, system monitoring, and networking tasks**.

---

**1. Working with Arrays & Associative Arrays**

  

**1.1. Defining and Accessing Arrays**

```
#!/bin/bash
fruits=("Apple" "Banana" "Cherry")
echo "First fruit: ${fruits[0]}"
echo "All fruits: ${fruits[@]}"
```

**1.2. Looping Through an Array**

```
#!/bin/bash
for fruit in "${fruits[@]}"; do
    echo "I like $fruit"
done
```

**1.3. Associative Arrays**

```
#!/bin/bash
declare -A person
person[name]="Alice"
person[age]=30
echo "Name: ${person[name]}, Age: ${person[age]}"
```

  

---

**2. AWK & Sed for Text Processing**

  

**2.1. Using AWK to Process Files**

```
#!/bin/bash
awk '{print $1, $3}' employees.txt  # Print 1st and 3rd columns
```

**2.2. Using AWK for Conditional Processing**

```
#!/bin/bash
awk '$3 > 50000 {print $1, $3}' employees.txt  # Print names where salary > 50000
```

**2.3. Using Sed for Find & Replace**

```
#!/bin/bash
sed -i 's/oldword/newword/g' file.txt  # Replace all occurrences of "oldword" with "newword"
```

**2.4. Extracting Specific Lines with Sed**

```
#!/bin/bash
sed -n '3,5p' file.txt  # Print lines 3 to 5
```

  

---

**3. Networking & Process Management**

  

**3.1. Checking Open Ports**

```
#!/bin/bash
netstat -tulnp  # List open ports
```

**3.2. Pinging a Server**

```
#!/bin/bash
ping -c 4 google.com
```

**3.3. Monitoring Network Traffic**

```
#!/bin/bash
ifconfig eth0
```

**3.4. Killing Processes**

```
#!/bin/bash
ps aux | grep firefox  # Find process ID of Firefox
kill -9 <PID>  # Replace <PID> with actual process ID
```

  

---

**4. Error Handling & Debugging Scripts**

  

**4.1. Using set -e to Stop on Errors**

```
#!/bin/bash
set -e  # Stop script on error
ls /nonexistent_folder  # This will cause an error and stop execution
```

**4.2. Logging Errors to a File**

```
#!/bin/bash
exec 2>>errors.log  # Redirect errors to a log file
ls /nonexistent_folder
```

**4.3. Debugging with set -x**

```
#!/bin/bash
set -x  # Enable debug mode
echo "Debugging script..."
set +x  # Disable debug mode
```

  

---

**5. Automating System Administration Tasks**

  

**5.1. Disk Space Monitoring**

```
#!/bin/bash
df -h | grep "^/dev"
```

**5.2. CPU & Memory Usage Report**

```
#!/bin/bash
echo "CPU Usage:"
top -b -n1 | grep "Cpu(s)"
echo "Memory Usage:"
free -h
```

**5.3. Automated Backup Script**

```
#!/bin/bash
backup_dir="/backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p $backup_dir
cp /var/log/syslog $backup_dir/
echo "Backup completed to $backup_dir"
```

  

---

**6. Scheduling Jobs & Log Monitoring**

  

**6.1. Creating a Cron Job**

  

Edit the cron table:

```
crontab -e
```

Run a script every day at midnight:

```
0 0 * * * /path/to/myscript.sh
```

**6.2. Monitoring Log Files in Real-Time**

```
#!/bin/bash
tail -f /var/log/syslog
```

**6.3. Sending Alerts Based on Logs**

```
#!/bin/bash
tail -f /var/log/auth.log | while read line; do
    if [[ "$line" == *"failed password"* ]]; then
        echo "ALERT: Failed SSH login detected!"
    fi
done
```

  

---

**7. Building a Full Shell Automation System**

  

**7.1. Automated User Account Creation**

```
#!/bin/bash
echo "Enter username:"
read username
sudo useradd -m $username
echo "User $username created!"
```

**7.2. Server Health Check Script**

```
#!/bin/bash
echo "Checking system health..."
df -h
free -h
top -b -n1 | grep "Cpu(s)"
uptime
```

**7.3. Automated Software Updates**

```
#!/bin/bash
sudo apt update && sudo apt upgrade -y
echo "System updated!"
```

  

---

**8. Conclusion**

  

**What You Learned in Shell Scripting Level 2:**

  

✅ **Working with Arrays & Associative Arrays**

✅ **AWK & Sed for Text Processing**

✅ **Networking & Process Management**

✅ **Error Handling & Debugging Scripts**

✅ **Automating System Administration Tasks**

✅ **Scheduling Jobs & Log Monitoring**

✅ **Built a Full Shell Automation System**

  

Now, you’re ready for **Shell Scripting Level 3**, where we explore **Advanced System Security, Cloud Automation, Log Analysis, and AI Integration in Shell Scripts!** 🚀