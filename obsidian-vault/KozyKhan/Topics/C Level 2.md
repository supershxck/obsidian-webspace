> **March 16th, 2025**  **22:31:00** 
> **Topics:** [[
> **Tags:** #CS  
---

**C Programming Level 2: Advanced Concepts and System Programming**

  

**Introduction**

  

Now that you’ve mastered **C basics**, it’s time to explore **advanced pointers, memory management, data structures, system programming, and multi-threading**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced Pointers & Dynamic Memory Allocation**

✅ **Data Structures (Linked Lists, Stacks, Queues, Trees)**

✅ **File Handling (Appending, Reading & Writing Structured Data)**

✅ **Working with Strings & String Manipulation**

✅ **System Programming (Process Control, Signals, File Permissions)**

✅ **Multi-threading with POSIX Threads**

✅ **Building a Full C Application**

  

By the end of this lesson, you will be able to **write optimized C programs, manipulate data structures, and work with advanced system operations**.

---

**1. Advanced Pointers & Dynamic Memory Allocation**

  

**1.1. Pointer to Pointer**

```
#include <stdio.h>

int main() {
    int x = 10;
    int *ptr = &x;
    int **ptr2 = &ptr;

    printf("Value of x: %d\n", x);
    printf("Address of x: %p\n", &x);
    printf("Pointer to x: %p, Value: %d\n", ptr, *ptr);
    printf("Pointer to Pointer: %p, Value at pointer to pointer: %d\n", ptr2, **ptr2);

    return 0;
}
```

**1.2. Dynamic Memory Allocation**

```
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr;
    int n = 5;

    arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        arr[i] = i * 2;
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    free(arr);  // Free allocated memory
    return 0;
}
```

  

---

**2. Data Structures in C**

  

**2.1. Implementing a Linked List**

```
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

void printList(struct Node *head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node *head = (struct Node *)malloc(sizeof(struct Node));
    struct Node *second = (struct Node *)malloc(sizeof(struct Node));
    struct Node *third = (struct Node *)malloc(sizeof(struct Node));

    head->data = 10;
    head->next = second;

    second->data = 20;
    second->next = third;

    third->data = 30;
    third->next = NULL;

    printList(head);
    free(head);
    free(second);
    free(third);
    return 0;
}
```

**2.2. Implementing a Stack**

```
#include <stdio.h>
#include <stdlib.h>

#define MAX 5

int stack[MAX], top = -1;

void push(int val) {
    if (top == MAX - 1)
        printf("Stack Overflow\n");
    else
        stack[++top] = val;
}

int pop() {
    if (top == -1) {
        printf("Stack Underflow\n");
        return -1;
    }
    return stack[top--];
}

int main() {
    push(10);
    push(20);
    push(30);
    printf("Popped: %d\n", pop());
    return 0;
}
```

  

---

**3. File Handling (Appending, Reading & Writing Structured Data)**

  

**3.1. Appending Data to a File**

```
#include <stdio.h>

int main() {
    FILE *file = fopen("data.txt", "a");
    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    fprintf(file, "New line appended!\n");
    fclose(file);

    return 0;
}
```

**3.2. Reading Structured Data from a File**

```
#include <stdio.h>

int main() {
    FILE *file = fopen("data.txt", "r");
    char buffer[100];

    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    while (fgets(buffer, 100, file) != NULL) {
        printf("%s", buffer);
    }

    fclose(file);
    return 0;
}
```

  

---

**4. System Programming (Process Control, Signals, File Permissions)**

  

**4.1. Creating a Child Process (Fork)**

```
#include <stdio.h>
#include <unistd.h>

int main() {
    int pid = fork();

    if (pid == 0)
        printf("Child Process: PID %d\n", getpid());
    else
        printf("Parent Process: PID %d\n", getpid());

    return 0;
}
```

**4.2. Handling Signals (SIGINT)**

```
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>

void handleSignal(int sig) {
    printf("Received signal %d. Exiting...\n", sig);
    exit(0);
}

int main() {
    signal(SIGINT, handleSignal);
    while (1) {
        printf("Running... Press Ctrl+C to stop.\n");
        sleep(1);
    }
    return 0;
}
```

  

---

**5. Multi-Threading in C (POSIX Threads)**

  

**5.1. Creating Threads**

```
#include <stdio.h>
#include <pthread.h>

void *printMessage(void *arg) {
    printf("Hello from thread!\n");
    return NULL;
}

int main() {
    pthread_t thread;
    pthread_create(&thread, NULL, printMessage, NULL);
    pthread_join(thread, NULL);
    return 0;
}
```

  

---

**6. String Manipulation**

  

**6.1. String Copy & Concatenation**

```
#include <stdio.h>
#include <string.h>

int main() {
    char str1[50] = "Hello";
    char str2[50] = "World";

    strcat(str1, " ");
    strcat(str1, str2);

    printf("Concatenated String: %s\n", str1);
    return 0;
}
```

**6.2. Finding Substring in a String**

```
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "C programming is fun!";
    char *substr = strstr(str, "programming");

    if (substr)
        printf("Substring found at position: %ld\n", substr - str);
    else
        printf("Substring not found\n");

    return 0;
}
```

  

---

**7. Building a Full C Application**

  

**7.1. Implementing a Simple Contact Management System**

```
#include <stdio.h>
#include <stdlib.h>

struct Contact {
    char name[50];
    char phone[15];
};

int main() {
    struct Contact contacts[3];
    
    for (int i = 0; i < 3; i++) {
        printf("Enter name: ");
        scanf("%s", contacts[i].name);
        printf("Enter phone: ");
        scanf("%s", contacts[i].phone);
    }

    FILE *file = fopen("contacts.txt", "w");
    for (int i = 0; i < 3; i++)
        fprintf(file, "%s %s\n", contacts[i].name, contacts[i].phone);
    
    fclose(file);
    printf("Contacts saved successfully!\n");

    return 0;
}
```

  

---

**8. Conclusion**

  

**What You Learned in C Level 2:**

  

✅ **Advanced Pointers & Dynamic Memory Allocation**

✅ **Data Structures (Linked Lists, Stacks, Queues, Trees)**

✅ **File Handling (Appending, Reading & Writing Structured Data)**

✅ **Working with Strings & String Manipulation**

✅ **System Programming (Process Control, Signals, File Permissions)**

✅ **Multi-threading with POSIX Threads**

✅ **Built a Full C Application**

  

Now, you’re ready for **C Level 3**, where we explore **Networking, IPC (Inter-Process Communication), Advanced Data Structures, and Embedded Systems Programming!** 🚀