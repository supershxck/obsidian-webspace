> **March 15th, 2025**  **18:41:45** 
> **Topics:** [[Swift L1]] 
> **Tags:** #CS 
---

**CNC Level 2: Advanced CNC Programming & Multi-Axis Machining**

  

**Introduction**

  

Now that you’ve mastered **basic CNC programming**, it’s time to explore **advanced techniques** such as **multi-axis machining, parametric programming, and automation**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced G-Code & M-Code Commands**

✅ **4-Axis & 5-Axis CNC Machining**

✅ **Macro & Parametric Programming**

✅ **Subprograms & Loops in CNC**

✅ **CNC Probing & Tool Compensation**

✅ **CNC Automation with Robots**

✅ **Building an Advanced CNC Program**

  

By the end of this lesson, you will be able to **program complex CNC operations and automate machining tasks**.

---

**1. Advanced G-Code & M-Code Commands**

  

**1.1. Advanced G-Code**

|**G-Code**|**Function**|
|---|---|
|**G17, G18, G19**|Select Plane (XY, XZ, YZ)|
|**G41, G42**|Cutter Compensation (Left/Right)|
|**G43, G49**|Tool Length Compensation|
|**G53, G54-G59**|Work Coordinate Systems|
|**G70, G71**|Finishing & Roughing Cycles|
|**G73, G83**|Peck Drilling Cycles|

**Example: Cutter Compensation (G41/G42)**

```
G41 D1 ; Enable Left Cutter Compensation  
G01 X50 Y50 F200 ; Move tool with offset  
G40 ; Cancel Cutter Compensation  
```

**1.2. Advanced M-Code**

|**M-Code**|**Function**|
|---|---|
|**M97**|Call Local Subprogram|
|**M98**|Call External Subprogram|
|**M99**|Return from Subprogram|
|**M30**|End of Program (Reset)|
|**M60**|Automatic Pallet Change|

**Example: Calling a Subprogram**

```
M98 P1000 L2 ; Call subprogram O1000, repeat 2 times  
```

  

---

**2. Multi-Axis CNC Machining (4-Axis & 5-Axis)**

  

**2.1. Understanding Additional Axes**

|**Axis**|**Function**|
|---|---|
|**A-Axis**|Rotates around X-axis|
|**B-Axis**|Rotates around Y-axis|
|**C-Axis**|Rotates around Z-axis|

**2.2. 4-Axis CNC Milling**

• A **4th axis** (A-axis) allows for **rotary indexing**.

```
G01 X50 Y50 A90 F200 ; Move to X50, Y50, rotate A-axis 90°
```

**2.3. 5-Axis CNC Milling**

• A **5th axis** (B or C) allows the tool to tilt.

```
G01 X50 Y50 Z10 B30 C20 F200 ; Move with tool tilted
```

  

---

**3. Macro & Parametric Programming**

  

Macros allow **automated, flexible programming**.

  

**3.1. Variables in CNC (G-Code Parameters)**

|**Parameter**|**Function**|
|---|---|
|**#1 - #33**|Local Variables|
|**#100 - #199**|General Variables|
|**#500 - #999**|System Variables|

**Example: Simple Macro (Using Variables)**

```
#100 = 50 ; Set X position  
#101 = 100 ; Set Y position  

G01 X#100 Y#101 F200 ; Move to (50,100)
```

  

---

**4. Subprograms & Loops in CNC**

  

Subprograms help **reuse code**.

  

**4.1. Creating a Subprogram**

```
O1000 ; Subprogram Start  
G01 X50 Y50 F200  
M99 ; Return from Subprogram  
```

**4.2. Calling a Subprogram**

```
M98 P1000 L3 ; Call O1000, repeat 3 times
```

  

---

**5. CNC Probing & Tool Compensation**

  

**5.1. CNC Probing (G31)**

• Used for **workpiece measurement**.

```
G31 X100 Y50 Z0 F100 ; Probe to surface
```

**5.2. Tool Compensation (G43, G44)**

```
G43 H1 ; Apply tool offset  
```

  

---

**6. CNC Automation with Robots**

• Robots can **load/unload workpieces automatically**.

• Uses **PLC & CNC Integration (Modbus, Ethernet/IP)**.

  

**6.1. Basic Robot Pick & Place**

```
M60 ; Call Robot Load  
G01 X50 Y50 ; Perform Machining  
M61 ; Call Robot Unload  
```

  

---

**7. Building an Advanced CNC Program**

  

**Objective:**

• Machine a **rectangular pocket** using a **loop**.

• Use **tool compensation and work offsets**.

```
G21 ; Set mm Mode  
G90 ; Absolute Positioning  
G54 ; Work Offset  

#100 = 10 ; Set Pocket Depth  
#101 = 50 ; Set Pocket Length  
#102 = 30 ; Set Pocket Width  

M06 T1 ; Tool Change  
G43 H1 ; Apply Tool Compensation  
M03 S1200 ; Start Spindle  

WHILE [#100 GT 0] DO1  
    G01 X0 Y0 Z-#100 F200  
    G01 X#101  
    G01 Y#102  
    G01 X0  
    G01 Y0  
    #100 = #100 - 2 ; Reduce Depth  
END1  

M05 ; Stop Spindle  
M30 ; End Program  
```

  

---

**Conclusion**

  

**What You Learned in CNC Level 2:**

  

✅ **Advanced G-Code & M-Code Commands**

✅ **4-Axis & 5-Axis CNC Machining**

✅ **Macro & Parametric Programming**

✅ **Subprograms & Loops in CNC**

✅ **CNC Probing & Tool Compensation**

✅ **CNC Automation with Robots**

✅ **Built an Advanced CNC Program**

  

Now, you’re ready for **CNC Level 3**, where we explore **CAM Software, AI-Powered CNC Optimization, and CNC in Industry 4.0!** 🚀