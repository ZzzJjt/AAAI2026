### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PLC program to control single-lane underground parking entry/exit traffic lights (red/green) using photoelectric sensors, ensuring only one car occupies the passage at a time while blocking conflicting movements.

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

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC control engineer responsible for developing an IEC 61131-3 Structured Text program to manage the entry and exit of vehicles in a single-lane underground parking garage. Your system must ensure safe and coordinated traffic control between the ground floor and basement.

⸻

🟩 I (Input) – What You’re Given

📥 Sensors and Pulse Flags:
	•	X1: Photoelectric switch at ground floor (ON when car passes)
	•	X2: Photoelectric switch at basement (ON when car passes)
	•	M1: ON for 1 scan when a car enters from ground floor through X1
	•	M2: ON for 1 scan when a car enters from basement through X1
	•	M3: ON for 1 scan when a car enters from basement through X2
	•	M4: ON for 1 scan when a car enters from ground floor through X2

🧠 Intermediate Control States:
	•	M20: TRUE when a car is traveling through the passage from the ground floor
	•	M30: TRUE when a car is traveling from the basement

🚦 Outputs:
	•	Y1: Red lights (entry/exit blocked)
	•	Y2: Green lights (entry/exit allowed)

⸻

🟧 S (Steps) – What You Need to Do
	1.	Initialize the System:
	•	On startup, set Y1 := FALSE (red lights off), Y2 := TRUE (green lights on), indicating the passage is free.
	2.	Detect Passage Occupancy:
	•	When a car starts entering from the ground floor (M1 or M4), set M20 := TRUE.
	•	When a car starts entering from the basement (M2 or M3), set M30 := TRUE.
	3.	Track Passage Exit:
	•	When a car completes passage from the ground (M3 or M4), reset M20 := FALSE.
	•	When a car completes passage from the basement (M1 or M2), reset M30 := FALSE.
	4.	Control Traffic Lights:
	•	If either M20 or M30 is TRUE, the passage is occupied:
	•	Set Y1 := TRUE (red), Y2 := FALSE (green).
	•	If both are FALSE, the passage is free:
	•	Set Y1 := FALSE, Y2 := TRUE.

⸻

🟦 E (Expectation) – What Success Looks Like

You will deliver a fully functional Structured Text control program that:
	•	Ensures only one car enters the passage at a time
	•	Controls red and green lights based on real-time passage usage
	•	Detects car presence and direction using photoelectric sensors and pulse flags
	•	Resets the system state when the passage becomes clear
	•	Starts with green lights on and red lights off by default
	•	Is easily maintainable, logically structured, and ready for real-world deployment

⸻

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text PLC program to control single-lane underground parking entry/exit traffic lights (red/green) using photoelectric sensors, ensuring only one car occupies the passage at a time while blocking conflicting movements.
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

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC control engineer responsible for developing an IEC 61131-3 Structured Text program to manage the entry and exit of vehicles in a single-lane underground parking garage. Your system must ensure safe and coordinated traffic control between the ground floor and basement.

⸻

🟩 I (Input) – What You’re Given

📥 Sensors and Pulse Flags:
	•	X1: Photoelectric switch at ground floor (ON when car passes)
	•	X2: Photoelectric switch at basement (ON when car passes)
	•	M1: ON for 1 scan when a car enters from ground floor through X1
	•	M2: ON for 1 scan when a car enters from basement through X1
	•	M3: ON for 1 scan when a car enters from basement through X2
	•	M4: ON for 1 scan when a car enters from ground floor through X2

🧠 Intermediate Control States:
	•	M20: TRUE when a car is traveling through the passage from the ground floor
	•	M30: TRUE when a car is traveling from the basement

🚦 Outputs:
	•	Y1: Red lights (entry/exit blocked)
	•	Y2: Green lights (entry/exit allowed)

⸻

🟧 S (Steps) – What You Need to Do
	1.	Initialize the System:
	•	On startup, set Y1 := FALSE (red lights off), Y2 := TRUE (green lights on), indicating the passage is free.
	2.	Detect Passage Occupancy:
	•	When a car starts entering from the ground floor (M1 or M4), set M20 := TRUE.
	•	When a car starts entering from the basement (M2 or M3), set M30 := TRUE.
	3.	Track Passage Exit:
	•	When a car completes passage from the ground (M3 or M4), reset M20 := FALSE.
	•	When a car completes passage from the basement (M1 or M2), reset M30 := FALSE.
	4.	Control Traffic Lights:
	•	If either M20 or M30 is TRUE, the passage is occupied:
	•	Set Y1 := TRUE (red), Y2 := FALSE (green).
	•	If both are FALSE, the passage is free:
	•	Set Y1 := FALSE, Y2 := TRUE.

⸻

🟦 E (Expectation) – What Success Looks Like

You will deliver a fully functional Structured Text control program that:
	•	Ensures only one car enters the passage at a time
	•	Controls red and green lights based on real-time passage usage
	•	Detects car presence and direction using photoelectric sensors and pulse flags
	•	Resets the system state when the passage becomes clear
	•	Starts with green lights on and red lights off by default
	•	Is easily maintainable, logically structured, and ready for real-world deployment

⸻

✅ Example Code (Structured Text)

VAR
    // Inputs
    X1, X2 : BOOL;                      // Photoelectric switches
    M1, M2, M3, M4 : BOOL;              // Pulse flags

    // States
    M20, M30 : BOOL;                    // Passage occupancy

    // Outputs
    Y1, Y2 : BOOL;                      // Red and green lights
END_VAR

// Initialize outputs
Y1 := FALSE;
Y2 := TRUE;

// Logic
IF M1 THEN
    M20 := TRUE;
ELSIF M4 THEN
    M20 := TRUE;
ELSIF M2 THEN
    M30 := TRUE;
ELSIF M3 THEN
    M30 := TRUE;
ELSE
    M20 := FALSE;
    M30 := FALSE;
END_IF;

IF M20 OR M30 THEN
    Y1 := TRUE;
    Y2 := FALSE;
ELSE
    Y1 := FALSE;
    Y2 := TRUE;
END_IF;
(* IEC 61131-3 Structured Text Program: ParkingControl *)
(* Purpose: Controls entry and exit of underground parking using photoelectric sensors *)

PROGRAM ParkingControl
VAR
    (* Inputs *)
    X1 : BOOL;                         (* Photoelectric switch at ground floor entry *)
    X2 : BOOL;                         (* Photoelectric switch at basement entry *)
    M1 : BOOL;                         (* Pulse flag: Car enters from ground floor *)
    M2 : BOOL;                         (* Pulse flag: Car enters from basement *)
    M3 : BOOL;                         (* Pulse flag: Car exits from ground floor *)
    M4 : BOOL;                         (* Pulse flag: Car exits from basement *)

    (* Outputs *)
    Y1 : BOOL;                         (* Red lights: Entry/exit blocked *)
    Y2 : BOOL;                         (* Green lights: Entry/exit allowed *)

    (* Internal Variables *)
    M20 : BOOL;                        (*
