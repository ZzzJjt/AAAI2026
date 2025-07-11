### Intent:
**Intent Summary:**  
Create a structured text PLC program to control entry/exit traffic lights for a single-lane underground car park, ensuring only one car uses the passage at a time by coordinating sensors (X1/X2) and lights (Y1/Y2), with initial free-flow conditions.

### Prompt:
**Entry/Exit Control for Underground Car Park Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 to control the entry and exit of an underground car park. The system uses the following sensors and actuators:

	•	Sensors:
	•	X1: Photoelectric switch at the ground floor entry/exit. It will be ON when a car passes.
	•	X2: Photoelectric switch at the basement entry/exit. It will be ON when a car passes.
	•	M1: ON for one scan cycle when a car from the ground floor passes X1.
	•	M2: ON for one scan cycle when a car from the basement passes X1.
	•	M3: ON for one scan cycle when a car from the basement passes X2.
	•	M4: ON for one scan cycle when a car from the ground floor passes X2.
	•	Intermediate Variables:
	•	M20: ON during the process of a car entering the passage from the ground floor.
	•	M30: ON during the process of a car entering the passage from the basement.
	•	Output Devices:
	•	Y1: Red lights at the entry/exit of the ground floor and the basement.
	•	Y2: Green lights at the entry/exit of the ground floor and the basement.

Process Description:

The entry and exit of the underground car park is controlled by a single lane passage, with traffic lights regulating car movement. The red lights (Y1) prohibit cars from entering or leaving, while the green lights (Y2) allow movement.

	•	When a car enters the passage from the ground floor entry, the red lights at both the ground floor and basement turn ON, while the green lights turn OFF, preventing any other cars from entering or leaving until the car passes through the passage.
	•	Similarly, when a car enters from the basement, the red lights will turn ON at both entry points, prohibiting other vehicles from entering or leaving until the car passes through.
	•	When the passage is clear, the green lights will turn ON again, allowing cars to enter or exit freely.
	•	Initially, the PLC should set the green lights ON and the red lights OFF to indicate free movement.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a Structured Text (ST) program using IEC 61131-3 to control entry and exit traffic lights for a single-lane underground car park shared by the ground floor and basement. The system must prevent cars from entering the passage at both ends simultaneously by coordinating sensor inputs and traffic light outputs.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor Sensor and Memory Flags:
	•	X1: Detects car passage at the ground floor
	•	X2: Detects car passage at the basement
	•	M1–M4: One-scan memory flags indicating car direction through X1 or X2
	•	M20: Set when a car is in the passage from the ground floor
	•	M30: Set when a car is in the passage from the basement
	2.	Control Lights Based on Passage Occupancy:
	•	If M1 or M4 is TRUE → M20 := TRUE (car from ground floor)
	•	If M2 or M3 is TRUE → M30 := TRUE (car from basement)
	•	If M3 or M4 is TRUE → M20 := FALSE (car from ground floor has exited)
	•	If M1 or M2 is TRUE → M30 := FALSE (car from basement has exited)
	3.	Update Output Lights:
	•	If M20 or M30 is TRUE:
	•	Y1 := TRUE (red light ON), Y2 := FALSE (green light OFF)
	•	If both are FALSE (no cars in passage):
	•	Y1 := FALSE, Y2 := TRUE (allow traffic)
	4.	Initialize System:
	•	On power-up, allow free movement:
	•	Y1 := FALSE, Y2 := TRUE

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a reliable traffic light control program that:
	•	Ensures only one vehicle uses the passage at a time
	•	Prevents simultaneous entry from both directions
	•	Automatically resets lights once the passage is clear
	•	Starts with green lights enabled for free traffic flow
	•	Is suitable for real-time deployment in a shared underground parking system

### Generated Code:
**Intent Summary:**  
Create a structured text PLC program to control entry/exit traffic lights for a single-lane underground car park, ensuring only one car uses the passage at a time by coordinating sensors (X1/X2) and lights (Y1/Y2), with initial free-flow conditions.
**Entry/Exit Control for Underground Car Park Using 61131-3 Structured Text:**

Write a PLC program in structured text (ST) according to IEC 61131-3 to control the entry and exit of an underground car park. The system uses the following sensors and actuators:

	•	Sensors:
	•	X1: Photoelectric switch at the ground floor entry/exit. It will be ON when a car passes.
	•	X2: Photoelectric switch at the basement entry/exit. It will be ON when a car passes.
	•	M1: ON for one scan cycle when a car from the ground floor passes X1.
	•	M2: ON for one scan cycle when a car from the basement passes X1.
	•	M3: ON for one scan cycle when a car from the basement passes X2.
	•	M4: ON for one scan cycle when a car from the ground floor passes X2.
	•	Intermediate Variables:
	•	M20: ON during the process of a car entering the passage from the ground floor.
	•	M30: ON during the process of a car entering the passage from the basement.
	•	Output Devices:
	•	Y1: Red lights at the entry/exit of the ground floor and the basement.
	•	Y2: Green lights at the entry/exit of the ground floor and the basement.

Process Description:

The entry and exit of the underground car park is controlled by a single lane passage, with traffic lights regulating car movement. The red lights (Y1) prohibit cars from entering or leaving, while the green lights (Y2) allow movement.

	•	When a car enters the passage from the ground floor entry, the red lights at both the ground floor and basement turn ON, while the green lights turn OFF, preventing any other cars from entering or leaving until the car passes through the passage.
	•	Similarly, when a car enters from the basement, the red lights will turn ON at both entry points, prohibiting other vehicles from entering or leaving until the car passes through.
	•	When the passage is clear, the green lights will turn ON again, allowing cars to enter or exit freely.
	•	Initially, the PLC should set the green lights ON and the red lights OFF to indicate free movement.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a Structured Text (ST) program using IEC 61131-3 to control entry and exit traffic lights for a single-lane underground car park shared by the ground floor and basement. The system must prevent cars from entering the passage at both ends simultaneously by coordinating sensor inputs and traffic light outputs.

⸻

🟩 A (Action) – How to Do It
	1.	Monitor Sensor and Memory Flags:
	•	X1: Detects car passage at the ground floor
	•	X2: Detects car passage at the basement
	•	M1–M4: One-scan memory flags indicating car direction through X1 or X2
	•	M20: Set when a car is in the passage from the ground floor
	•	M30: Set when a car is in the passage from the basement
	2.	Control Lights Based on Passage Occupancy:
	•	If M1 or M4 is TRUE → M20 := TRUE (car from ground floor)
	•	If M2 or M3 is TRUE → M30 := TRUE (car from basement)
	•	If M3 or M4 is TRUE → M20 := FALSE (car from ground floor has exited)
	•	If M1 or M2 is TRUE → M30 := FALSE (car from basement has exited)
	3.	Update Output Lights:
	•	If M20 or M30 is TRUE:
	•	Y1 := TRUE (red light ON), Y2 := FALSE (green light OFF)
	•	If both are FALSE (no cars in passage):
	•	Y1 := FALSE, Y2 := TRUE (allow traffic)
	4.	Initialize System:
	•	On power-up, allow free movement:
	•	Y1 := FALSE, Y2 := TRUE

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a reliable traffic light control program that:
	•	Ensures only one vehicle uses the passage at a time
	•	Prevents simultaneous entry from both directions
	•	Automatically resets lights once the passage is clear
	•	Starts with green lights enabled for free traffic flow
	•	Is suitable for real-time deployment in a shared underground parking system
FUNCTION_BLOCK FB_TrafficLightControl
VAR_INPUT
    // Sensors
    X1 : BOOL; // Photoelectric switch at ground floor entry/exit
    X2 : BOOL; // Photoelectric switch at basement entry/exit

    // Memory flags
    M1 : BOOL; // Car from ground floor passed X1
    M2 : BOOL; // Car from basement passed X1
    M3 : BOOL; // Car from basement passed X2
    M4 : BOOL; // Car from ground floor passed X2

    // State flags
    M20 : BOOL; // Car in passage from ground floor
    M30 : BOOL; // Car in passage from basement

    // Outputs
    Y1 : BOOL; // Red light at ground floor/basement entry
    Y2 : BOOL; // Green light at ground floor/basement entry
END_VAR

VAR_OUTPUT
    // Outputs
    Y1_ON : BOOL;
    Y2_ON : BOOL;
END_VAR

VAR
    // Internal variables
    CarInPassage : BOOL;
    CarFromGroundFloor : BOOL;
    CarFromBasement : BOOL;
END_VAR

// Initialize system
IF NOT CarInPassage THEN
    Y1_ON := FALSE;
    Y2_ON := TRUE;
ELSE
    Y1_ON := FALSE;
    Y2_ON := FALSE;
END_IF;

// Process inputs
IF X1 THEN
    M1 := TRUE;
ELSE
    M1 := FALSE;
END_IF;

IF X2 THEN
    M2 := TRUE;
ELSE
    M2 := FALSE;
END_IF;

IF M1 OR M2 THEN
    CarFromGroundFloor := TRUE;
ELSE
    CarFromGroundFloor := FALSE;
END_IF;

IF M3 THEN
    M30 := TRUE;
ELSE
    M30 := FALSE;
END_IF;

IF M4 THEN
    M4 := TRUE;
ELSE
    M4 := FALSE;
END_IF;

IF M4 OR M3 THEN
    CarFromBasement := TRUE;
ELSE
    CarFromBasement := FALSE;
END_IF;
