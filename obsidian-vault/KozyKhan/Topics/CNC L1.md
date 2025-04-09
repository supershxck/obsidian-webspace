> **March 15th, 2025**  **18:40:30** 
> **Topics:** [[CNC L2]] 
> **Tags:** #
---

**CNC Level 1: Introduction to CNC Programming & Machine Operation**

  

**Introduction**

  

A **CNC (Computer Numerical Control) machine** is a computer-controlled system used to **automate machining processes**, such as milling, turning, and drilling. It provides **high precision, repeatability, and efficiency** in manufacturing.

  

**What You’ll Learn in This Lesson:**

  

✅ **What is a CNC Machine?**

✅ **Types of CNC Machines (Milling, Turning, Laser, EDM, etc.)**

✅ **CNC Components & Axis Movement**

✅ **Introduction to G-Code & M-Code**

✅ **Basic CNC Operations (Tool Setup, Work Offsets, Speeds & Feeds)**

✅ **CNC Safety & Troubleshooting**

✅ **Building a Simple CNC Program**

  

By the end of this lesson, you will understand **how CNC machines work and how to write basic G-code programs**.

---

**1. What is a CNC Machine?**

  

A **CNC machine** is a manufacturing tool controlled by **computer programs** to perform **precise machining operations**.

  

**1.1. Why Use CNC Machines?**

  

✅ **High Precision** – Achieves **micron-level accuracy**

✅ **Automation** – Reduces **manual labor**

✅ **Efficiency** – Produces parts **faster** than manual machining

✅ **Repeatability** – Ensures **consistent quality**

---

**2. Types of CNC Machines**

  

**2.1. Common CNC Machine Types**

  

🔹 **CNC Milling Machine** – Cuts material using a rotating tool

🔹 **CNC Lathe (Turning Center)** – Rotates material and cuts with a stationary tool

🔹 **CNC Laser Cutter** – Uses high-energy laser beams to cut material

🔹 **CNC Plasma Cutter** – Uses a plasma torch to cut metal

🔹 **CNC Electrical Discharge Machining (EDM)** – Uses electrical discharges to remove material

  

**2.2. Difference Between CNC Milling vs. CNC Turning**

|**Feature**|**CNC Milling**|**CNC Turning**|
|---|---|---|
|Tool Movement|Rotating Cutting Tool|Stationary Tool|
|Workpiece|Fixed, Moved in Axes|Rotating Material|
|Common Use|Complex 3D Shapes|Cylindrical Parts|

  

---

**3. CNC Components & Axis Movement**

  

**3.1. Key CNC Machine Components**

  

🔹 **Control Unit** – Computer that interprets the CNC program

🔹 **Spindle** – Holds the cutting tool

🔹 **Tool Changer** – Automatically switches tools

🔹 **Worktable** – Holds the workpiece

🔹 **Coolant System** – Keeps tools from overheating

  

**3.2. Understanding CNC Axis Movements**

|**Axis**|**Description**|
|---|---|
|X-Axis|Left & Right Movement|
|Y-Axis|Front & Back Movement|
|Z-Axis|Up & Down Movement|
|A, B, C|Rotational Axes|

**Example: 3-Axis CNC Milling Machine**

```
X → Moves Left/Right
Y → Moves Forward/Backward
Z → Moves Up/Down
```

  

---

**4. Introduction to G-Code & M-Code**

  

**4.1. What is G-Code?**

• **G-Code** is the language used to control CNC machines.

• It tells the machine **how to move, where to cut, and how fast to operate**.

  

**4.2. What is M-Code?**

• **M-Code** controls **machine-specific commands**, such as **coolant, tool changes, and spindle control**.

---

**5. Basic CNC G-Code Commands**

  

**5.1. Essential G-Code Commands**

|**G-Code**|**Function**|
|---|---|
|**G00**|Rapid Positioning (Fast Move)|
|**G01**|Linear Interpolation (Cut)|
|**G02**|Clockwise Arc|
|**G03**|Counterclockwise Arc|
|**G28**|Return to Machine Home|
|**G90**|Absolute Positioning|
|**G91**|Relative Positioning|

**Example: Moving to a Position**

```
G00 X50 Y25 Z10  ; Move to (X50, Y25, Z10) at rapid speed
G01 X100 Y50 F200 ; Cut to (X100, Y50) at 200mm/min feedrate
```

**5.2. Essential M-Code Commands**

|**M-Code**|**Function**|
|---|---|
|**M03**|Start Spindle Clockwise|
|**M04**|Start Spindle Counterclockwise|
|**M05**|Stop Spindle|
|**M06**|Tool Change|
|**M08**|Coolant On|
|**M09**|Coolant Off|
|**M30**|Program End|

**Example: Start Spindle & Coolant**

```
M03 S1000 ; Start spindle at 1000 RPM
M08       ; Turn coolant ON
```

  

---

**6. Basic CNC Operations**

  

**6.1. Tool Setup & Tool Offsets**

1. **Insert the correct tool** into the spindle.

2. **Set tool length offset** to ensure proper depth.

3. **Use a tool probe** to measure tool length.

  

**Example: Setting Tool Offset (T1)**

```
G43 H1  ; Apply Tool Offset for Tool 1
```

**6.2. Work Offsets & Machine Zero**

• **G54 to G59** – Work Offset Commands (Set Workpiece Zero)

• **G28** – Machine Home

  

**Example: Setting Workpiece Zero**

```
G54 ; Use Work Offset 1
G00 X0 Y0 Z0 ; Move to Zero Position
```

**6.3. Feeds & Speeds**

• **Feed Rate (F)** – Speed at which the tool moves

• **Spindle Speed (S)** – Rotational speed of the tool

  

**Example: Setting Feed & Speed**

```
G01 X100 Y50 F200 ; Move with a feed rate of 200 mm/min
M03 S1500 ; Set spindle speed to 1500 RPM
```

  

---

**7. CNC Safety & Troubleshooting**

  

**7.1. Safety Tips**

  

✅ **Use Safety Glasses & Gloves** – Protects against flying debris

✅ **Double-Check G-Code** – Prevents crashes

✅ **Use Emergency Stop (E-Stop)** – Stops the machine instantly

✅ **Secure Workpiece** – Prevents vibrations and movement

  

**7.2. Common CNC Errors & Solutions**

|**Issue**|**Possible Cause**|**Solution**|
|---|---|---|
|Tool Breakage|Incorrect Feeds/Speeds|Adjust feed & speed|
|Material Burning|Tool moving too slow|Increase feed rate|
|Workpiece Shifted|Loose clamping|Re-tighten clamps|
|G-Code Error|Syntax mistake|Debug program|

  

---

**8. Building a Simple CNC Program**

  

**Objective:**

• Start the **spindle at 1200 RPM**

• Move to **X50, Y50** at **rapid speed**

• Cut a **50mm straight line**

• Stop the **spindle and coolant**

```
G21        ; Use millimeters
G90        ; Absolute positioning
G54        ; Work offset

M06 T1     ; Select Tool 1
M03 S1200  ; Start spindle at 1200 RPM
M08        ; Turn on coolant

G00 X50 Y50 ; Rapid move to start position
G01 X100 Y50 F200 ; Cut a straight line at 200mm/min

M09        ; Coolant OFF
M05        ; Spindle OFF
M30        ; End program
```

  

---

**Conclusion**

  

**What You Learned in CNC Level 1:**

  

✅ **CNC Machine Basics & Types**

✅ **CNC Components & Axis Movements**

✅ **G-Code & M-Code Programming**

✅ **Basic CNC Operations (Tool Setup, Work Offsets, Feeds & Speeds)**

✅ **CNC Safety & Troubleshooting**

✅ **Built a Simple CNC Program**

  

Now, you’re ready for **CNC Level 2**, where we explore **Advanced CNC Programming, 4-Axis & 5-Axis Machining, and CNC Automation with Robots!** 🚀