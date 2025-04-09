> **March 15th, 2025**  **19:08:02** 
> **Topics:** [[Shell Scripting L2]] 
> **Tags:** #CS 
---

**Shell Scripting Level 1: Introduction to Bash Scripting**

  

**Introduction**

  

Shell scripting allows **automation of tasks, system administration, and process management** in Unix/Linux environments. Bash (Bourne Again Shell) is the most commonly used shell.

  

**What You’ll Learn in This Lesson:**

  

✅ **Shell Basics (Shebang, Running Scripts, Variables, Input/Output)**

✅ **Control Flow (If-Else, Loops, Case Statements)**

✅ **Functions & Arguments**

✅ **File Handling & Permissions**

✅ **Working with System Commands (ls, grep, awk, sed, find, crontab)**

✅ **Building a Simple Shell Script Application**

  

By the end of this lesson, you will be able to **write basic shell scripts to automate tasks and manage files and processes**.

---

**1. Setting Up & Running Shell Scripts**

  

**1.1. Creating & Running a Shell Script**

1. Open a terminal and create a script:

```
nano myscript.sh
```

  

1. Add the following:

```
#!/bin/bash
echo "Hello, World!"
```

  

1. Save and exit (CTRL+X, Y, Enter).

2. Make it executable:

```
chmod +x myscript.sh
```

  

1. Run the script:

```
./myscript.sh
```

  

  

**1.2. The Shebang (#!)**

• The #! at the beginning tells the system which interpreter to use (/bin/bash, /bin/sh, etc.).

• Example for Bash:

```
#!/bin/bash
```

  

---

**2. Variables & User Input**

  

**2.1. Declaring Variables**

```
#!/bin/bash
name="Alice"
age=25
echo "Name: $name, Age: $age"
```

**2.2. Taking User Input**

```
#!/bin/bash
echo "Enter your name:"
read name
echo "Hello, $name!"
```

**2.3. Command Substitution**

```
#!/bin/bash
date_today=$(date)
echo "Today's date is $date_today"
```

  

---

**3. Control Flow (If-Else, Loops, Case Statements)**

  

**3.1. If-Else Statement**

```
#!/bin/bash
echo "Enter a number:"
read num
if [ $num -gt 10 ]; then
    echo "Number is greater than 10"
else
    echo "Number is 10 or less"
fi
```

**3.2. For Loop**

```
#!/bin/bash
for i in {1..5}; do
    echo "Iteration $i"
done
```

**3.3. While Loop**

```
#!/bin/bash
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

**3.4. Case Statement**

```
#!/bin/bash
echo "Enter your favorite fruit:"
read fruit
case $fruit in
    "apple") echo "You like apples!" ;;
    "banana") echo "Bananas are great!" ;;
    *) echo "Nice choice!" ;;
esac
```

  

---

**4. Functions & Arguments**

  

**4.1. Defining & Calling Functions**

```
#!/bin/bash
greet() {
    echo "Hello, $1!"
}
greet "Alice"
```

**4.2. Passing Multiple Arguments**

```
#!/bin/bash
sum() {
    echo "Sum: $(($1 + $2))"
}
sum 5 10
```

  

---

**5. File Handling & Permissions**

  

**5.1. Creating, Writing & Reading Files**

```
#!/bin/bash
echo "This is a test file" > test.txt
cat test.txt
```

**5.2. Checking If a File Exists**

```
#!/bin/bash
if [ -f "test.txt" ]; then
    echo "File exists"
else
    echo "File does not exist"
fi
```

**5.3. Deleting a File**

```
#!/bin/bash
rm -i test.txt  # Prompts before deletion
```

  

---

**6. Working with System Commands**

  

**6.1. Listing Files (ls)**

```
#!/bin/bash
ls -lh  # Lists files with sizes in human-readable format
```

**6.2. Searching in Files (grep)**

```
#!/bin/bash
grep "Hello" test.txt  # Finds lines containing "Hello"
```

**6.3. Finding Files (find)**

```
#!/bin/bash
find /home -name "*.txt"  # Finds all text files in home directory
```

**6.4. Replacing Text (sed)**

```
#!/bin/bash
sed -i 's/oldtext/newtext/g' test.txt  # Replaces "oldtext" with "newtext"
```

**6.5. Scheduling Jobs (crontab)**

  

Edit cron jobs:

```
crontab -e
```

Run script every minute:

```
* * * * * /path/to/myscript.sh
```

  

---

**7. Building a Simple Shell Script Application**

  

**7.1. Script to Backup Files**

```
#!/bin/bash
backup_dir="backup_$(date +%Y%m%d_%H%M%S)"
mkdir $backup_dir
cp *.txt $backup_dir
echo "Backup completed to $backup_dir"
```

**7.2. Disk Space Monitor**

```
#!/bin/bash
df -h | grep "^/dev"
```

**7.3. Network Ping Test**

```
#!/bin/bash
ping -c 4 google.com
```

  

---

**8. Conclusion**

  

**What You Learned in Shell Scripting Level 1:**

  

✅ **Shell Basics (Shebang, Running Scripts, Variables, Input/Output)**

✅ **Control Flow (If-Else, Loops, Case Statements)**

✅ **Functions & Arguments**

✅ **File Handling & Permissions**

✅ **Working with System Commands (ls, grep, awk, sed, find, crontab)**

✅ **Built a Simple Shell Script Application**

  

Now, you’re ready for **Shell Scripting Level 2**, where we explore **AWK, Advanced File Processing, Networking, Automation, and System Monitoring!** 🚀