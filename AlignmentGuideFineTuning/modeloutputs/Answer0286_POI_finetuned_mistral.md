### Intent:
The task is to create a PLC program in Structured Text that controls a single-lane underground car park entry/exit system using photoelectric sensors and traffic lights to ensure safe one-way vehicle passage by managing red/green light states based on vehicle detection.  

**Intent Summary:**  
*"Develop a safety-interlocked traffic control system for a single-lane underground car park passage using photoelectric sensors and light signals to enforce one-directional vehicle movement at a time."*  

(Key focus: **unidirectional occupancy control** via sensor-triggered light states, prioritizing collision prevention.)

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

**C-A-R-E:**

🟥 C (Context) – The Background

In an underground car park with a single-lane passage, it’s crucial to safely control vehicle entry and exit to prevent head-on collisions. The system must detect vehicles coming from both the ground floor and basement, and manage traffic lights to ensure only one car occupies the passage at a time. This can be achieved using a PLC programmed in IEC 61131-3 Structured Text, which interprets signals from photoelectric sensors and manages light outputs.

⸻

🟩 A (Action) – The Implementation Task

Write a Structured Text program to control the traffic flow through the passage. Use:

Sensors:
	•	X1: Photoelectric switch at ground floor (ON when car passes)
	•	X2: Photoelectric switch at basement (ON when car passes)
	•	M1–M4: Pulse flags (ON for 1 scan when car passes a certain sensor from a direction)

Memory Flags:
	•	M20: Passage occupied by a car entering from the ground floor
	•	M30: Passage occupied by a car entering from the basement

Actuators:
	•	Y1: Red lights (ON = stop)
	•	Y2: Green lights (ON = go)

Logic:
	•	When a car enters from either side, activate red lights (Y1 := TRUE) and deactivate green lights (Y2 := FALSE) at both ends.
	•	When the passage is clear, restore green lights and turn off red lights.
	•	Initially, the system should allow passage (Y2 := TRUE, Y1 := FALSE).

⸻

🟨 R (Result) – The Expected Outcome

The program will:
	•	Allow only one car at a time to use the passage
	•	Automatically detect when the passage is occupied or cleared
	•	Control red and green lights to manage safe access
	•	Reset to a default “ready” state when the passage becomes empty
	•	Be suitable for real-time use in industrial or commercial garage access control

⸻

🟦 E (Example) – Code Snippet
// Set passage occupancy
IF M1 OR M4 THEN
    M20 := TRUE; // Ground floor entry
END_IF;
IF M2 OR M3 THEN
    M30 := TRUE; // Basement entry
END_IF;

// Clear passage occupancy after exit
IF M3 OR M4 THEN
    M20 := FALSE;
END_IF;
IF M1 OR M2 THEN
    M30 := FALSE;
END_IF;

// Light control
IF M20 OR M30 THEN
    Y1 := TRUE;   // Red light ON
    Y2 := FALSE;  // Green light OFF
ELSE
    Y1 := FALSE;  // Red light OFF
    Y2 := TRUE;   // Green light ON
END_IF;

### Generated Code:
The task is to create a PLC program in Structured Text that controls a single-lane underground car park entry/exit system using photoelectric sensors and traffic lights to ensure safe one-way vehicle passage by managing red/green light states based on vehicle detection.  

**Intent Summary:**  
*"Develop a safety-interlocked traffic control system for a single-lane underground car park passage using photoelectric sensors and light signals to enforce one-directional vehicle movement at a time."*  

(Key focus: **unidirectional occupancy control** via sensor-triggered light states, prioritizing collision prevention.)
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

**C-A-R-E:**

🟥 C (Context) – The Background

In an underground car park with a single-lane passage, it’s crucial to safely control vehicle entry and exit to prevent head-on collisions. The system must detect vehicles coming from both the ground floor and basement, and manage traffic lights to ensure only one car occupies the passage at a time. This can be achieved using a PLC programmed in IEC 61131-3 Structured Text, which interprets signals from photoelectric sensors and manages light outputs.

⸻

🟩 A (Action) – The Implementation Task

Write a Structured Text program to control the traffic flow through the passage. Use:

Sensors:
	•	X1: Photoelectric switch at ground floor (ON when car passes)
	•	X2: Photoelectric switch at basement (ON when car passes)
	•	M1–M4: Pulse flags (ON for 1 scan when car passes a certain sensor from a direction)

Memory Flags:
	•	M20: Passage occupied by a car entering from the ground floor
	•	M30: Passage occupied by a car entering from the basement

Actuators:
	•	Y1: Red lights (ON = stop)
	•	Y2: Green lights (ON = go)

Logic:
	•	When a car enters from either side, activate red lights (Y1 := TRUE) and deactivate green lights (Y2 := FALSE) at both ends.
	•	When the passage is clear, restore green lights and turn off red lights.
	•	Initially, the system should allow passage (Y2 := TRUE, Y1 := FALSE).

⸻

🟨 R (Result) – The Expected Outcome

The program will:
	•	Allow only one car at a time to use the passage
	•	Automatically detect when the passage is occupied or cleared
	•	Control red and green lights to manage safe access
	•	Reset to a default “ready” state when the passage becomes empty
	•	Be suitable for real-time use in industrial or commercial garage access control

⸻

🟦 E (Example) – Code Snippet
// Set passage occupancy
IF M1 OR M4 THEN
    M20 := TRUE; // Ground floor entry
END_IF;
IF M2 OR M3 THEN
    M30 := TRUE; // Basement entry
END_IF;

// Clear passage occupancy after exit
IF M3 OR M4 THEN
    M20 := FALSE;
END_IF;
IF M1 OR M2 THEN
    M30 := FALSE;
END_IF;

// Light control
IF M20 OR M30 THEN
    Y1 := TRUE;   // Red light ON
    Y2 := FALSE;  // Green light OFF
ELSE
    Y1 := FALSE;  // Red light OFF
    Y2 := TRUE;   // Green light ON
END_IF;
This logic ensures safe, unidirectional passage control using photoelectric sensors and light signals, with automatic state transitions and interlocking.
FUNCTION_BLOCK FB_ParkingLotEntryControl
VAR_INPUT
    X1 : BOOL; // Photoelectric switch at ground floor entry
    X2 : BOOL; // Photoelectric switch at basement entry
    M1 : BOOL; // Pulse flag: Car from ground floor passed X1
    M2 : BOOL; // Pulse flag: Car from basement passed X1
    M3 : BOOL; // Pulse flag: Car from basement passed X2
    M4 : BOOL; // Pulse flag: Car from ground floor passed X2
END_VAR

VAR_OUTPUT
    Y1 : BOOL; // Red lights at entry/exit of ground floor and basement
    Y2 : BOOL; // Green lights at entry/exit of ground floor and basement
END_VAR

VAR
    M20 : BOOL; // Car from ground floor in passage
    M30 : BOOL; // Car from basement in passage
    M21 : BOOL; // Car from ground floor exited passage
    M31 : BOOL; // Car from basement exited passage
    M22 : BOOL; // Car from ground floor entered passage
    M32 : BOOL; // Car from basement entered passage
END_VAR

// Reset outputs
Y1 := FALSE;
Y2 := TRUE;

// Track car movement
IF M1 THEN
    M21 := TRUE;
    M22 := TRUE;
ELSIF M21 THEN
    M21 := FALSE;
END_IF;

IF M2 THEN
    M31 := TRUE;
    M32 := TRUE;
ELSIF M31 THEN
    M31 := FALSE;
END_IF;

// Detect car entry from ground floor
IF M22 THEN
    M20 := TRUE;
    M22 := FALSE;
ELSIF M32 THEN
    M30 := TRUE;
    M32 := FALSE;
END_IF;

// Detect car exit from ground floor
IF M1 OR M2 THEN
    M21 :=
