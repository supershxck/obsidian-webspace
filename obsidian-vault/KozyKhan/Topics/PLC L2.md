> **March 15th, 2025**  **18:39:46** 
> **Topics:** [[CNC L1]] 
> **Tags:** #
---

**PLC Level 2: Advanced PLC Programming & Industrial Automation**

  

**Introduction**

  

Now that you’ve learned **basic PLC programming**, it’s time to explore **advanced industrial automation concepts**. This level focuses on **real-world PLC applications, networking, and industrial protocols**.

  

**What You’ll Learn in This Lesson:**

  

✅ **Advanced PLC Programming Techniques (State Machines, Sequencers, PID Control)**

✅ **Networking & Communication (Modbus, PROFIBUS, MQTT, OPC UA)**

✅ **Human-Machine Interface (HMI) & SCADA Integration**

✅ **Data Logging & Industrial IoT (IIoT)**

✅ **Error Handling & Redundancy in PLC Systems**

✅ **PLC Troubleshooting & Diagnostics**

✅ **Building a Real-World Industrial Control System**

  

By the end of this lesson, you will be able to **develop and integrate complex automation systems**.

---

**1. Advanced PLC Programming Techniques**

  

**1.1. State Machine Programming**

  

State machines are used to **control sequential operations**.

  

**Example: Traffic Light Control in Ladder Logic**

```
Green_Light   ---[ ]--[TON T1 10s]--(Red_Light)
Red_Light     ---[ ]--[TON T2 5s]--(Yellow_Light)
Yellow_Light  ---[ ]--[TON T3 3s]--(Green_Light)
```

**Structured Text (ST) Version:**

```
CASE State OF
    0: Green := TRUE; Timer1 := TON(10s); IF Timer1.DONE THEN State := 1; END_IF;
    1: Green := FALSE; Red := TRUE; Timer2 := TON(5s); IF Timer2.DONE THEN State := 2; END_IF;
    2: Red := FALSE; Yellow := TRUE; Timer3 := TON(3s); IF Timer3.DONE THEN State := 0; END_IF;
END_CASE;
```

  

---

**1.2. Sequencers (Process Control)**

  

A **sequencer** is used when a process must follow a predefined sequence.

  

**Example: Bottle Filling Process**

1. Move bottle under the filling station

2. Fill the bottle

3. Move to the capping station

4. Seal the bottle

5. Move bottle to the next process

```
Step_1 ---[ ]--(Move_Conveyor)
Step_2 ---[ ]--(Fill_Bottle)
Step_3 ---[ ]--(Move_To_Cap)
Step_4 ---[ ]--(Seal_Bottle)
Step_5 ---[ ]--(Move_Conveyor)
```

  

---

**1.3. PID Control (Proportional-Integral-Derivative)**

  

PID controllers **maintain process stability**, such as **temperature, pressure, and speed control**.

  

**Example: Temperature Control**

```
(Temperature Sensor) ---[PID]---(Heater)
```

**Structured Text (ST) PID Controller:**

```
PID_Heater := PID_Process(T_Setpoint, T_Measured, Kp, Ki, Kd);
```

• **Kp** = Proportional gain

• **Ki** = Integral gain

• **Kd** = Derivative gain

---

**2. Networking & Communication**

  

PLCs communicate with other **devices, sensors, and controllers** using industrial protocols.

  

**2.1. Modbus (RS-485, TCP/IP)**

• **Widely used** in industrial communication

• **Master-Slave architecture**

  

**Example: Modbus TCP Communication (Structured Text)**

```
Modbus_Write("192.168.1.100", 40001, 100);
Modbus_Read("192.168.1.100", 40002);
```

  

---

**2.2. PROFIBUS & PROFINET (Siemens PLCs)**

• **PROFIBUS** – Serial-based

• **PROFINET** – Ethernet-based

  

Example: **PROFINET I/O Mapping**

```
(Device 1) ---[PROFINET]--- (PLC) ---[PROFINET]--- (HMI)
```

  

---

**2.3. MQTT (IIoT Protocol)**

  

MQTT is used for **Industrial IoT (IIoT) and cloud-based monitoring**.

  

**Example: PLC Publishing Data to an MQTT Broker**

```
MQTT_Publish("broker.hivemq.com", "temperature_sensor", Temperature);
```

  

---

**3. Human-Machine Interface (HMI) & SCADA Integration**

  

HMI and SCADA are used to **monitor and control PLC systems**.

  

**3.1. Configuring an HMI Screen**

• **Create buttons for Start/Stop**

• **Display real-time process data**

• **Use alarms for warnings**

  

**Example: Connecting Siemens WinCC HMI with PLC**

1. Open **Siemens WinCC**

2. Configure **Tags** to read/write PLC variables

3. Create **HMI Buttons** for Start/Stop

4. Link **HMI Alarms** to PLC fault conditions

---

**4. Data Logging & Industrial IoT (IIoT)**

  

**4.1. Logging Data to an SQL Database**

```
DB_Connection := SQL_Connect("db_server", "user", "password");
SQL_Insert(DB_Connection, "INSERT INTO production_log (temperature, speed) VALUES (?, ?)", Temp, Speed);
```

**4.2. Sending Data to the Cloud**

```
MQTT_Publish("cloud.broker.com", "machine_data", Data_Array);
```

  

---

**5. Error Handling & Redundancy in PLC Systems**

  

**5.1. PLC Fault Detection**

  

**Example: Detecting a Sensor Failure**

```
(Sensor Input) ---[ ]---(Timer 5s)---(Alarm)
```

If the **sensor doesn’t respond within 5 seconds**, trigger an **alarm**.

  

**5.2. PLC Redundancy (Failover Systems)**

• **Dual PLCs in hot standby mode**

• **Automatic switchover if one PLC fails**

---

**6. PLC Troubleshooting & Diagnostics**

  

**6.1. Common PLC Errors**

|**Issue**|**Possible Cause**|**Solution**|
|---|---|---|
|PLC Not Responding|Power failure|Check power supply|
|I/O Not Updating|Bad wiring or faulty sensor|Inspect wiring and connections|
|Communication Error|Incorrect IP or cable fault|Verify network settings|

**6.2. Using PLC Diagnostics Tools**

• **Siemens TIA Portal** – Diagnose faults in Siemens PLCs

• **Allen-Bradley RSLogix 5000** – Monitor logic execution

---

**7. Building a Real-World Industrial Control System**

  

**Project: Automated Conveyor System**

  

**Objective:**

• Move conveyor when **Start Button** is pressed

• Stop conveyor when **End Sensor** detects an object

• Flash a warning light if conveyor runs **too long without an object detected**

  

**Ladder Logic Diagram**

```
(Start Button) ---[ ]------(Conveyor Motor)
(End Sensor)   ---[/]------(Stop Conveyor)
(Timer 30s)    ---[ ]------(Warning Light)
```

**Structured Text (ST) Version**

```
IF Start_Button THEN
    Conveyor := TRUE;
    TON(Timer1, 30s);
END_IF;

IF End_Sensor THEN
    Conveyor := FALSE;
END_IF;

IF Timer1.DONE THEN
    Warning_Light := TRUE;
END_IF;
```

  

---

**Conclusion**

  

**What You Learned in PLC Level 2:**

  

✅ **State Machines, Sequencers, and PID Control**

✅ **Networking & Communication (Modbus, PROFIBUS, MQTT, OPC UA)**

✅ **HMI & SCADA Integration**

✅ **Data Logging & Industrial IoT (IIoT)**

✅ **Error Handling & Redundancy**

✅ **PLC Troubleshooting & Diagnostics**

✅ **Built a Real-World Industrial Control System**

  

Now, you’re ready for **PLC Level 3**, where we explore **Advanced Motion Control, Robotics, AI in Industrial Automation, and Cybersecurity for PLCs!** 🚀