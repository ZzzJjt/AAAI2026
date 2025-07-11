### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a single-lane underground car park entry/exit system using photoelectric sensors and traffic lights, ensuring safe one-way passage by activating red lights when occupied and green lights when clear.

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

**R-T-F:**
🟥 R (Role) – Your Role

You are a PLC automation engineer tasked with programming a traffic light control system for a single-lane underground car park. The system must manage vehicle entry and exit from both the ground floor and basement, using sensors and memory flags, and control red and green lights accordingly to ensure safe one-way usage of the passage.

⸻

🟩 T (Task) – What You Need to Do

Write a Structured Text (ST) program in accordance with IEC 61131-3 standards that:
	1.	Monitors Sensors and Flags:
	•	X1: Photoelectric switch at ground floor (ON when a car passes)
	•	X2: Photoelectric switch at basement
	•	M1–M4: ON for one scan cycle when a car passes a sensor in a specific direction
	•	M20: TRUE if a car is in the passage from the ground floor
	•	M30: TRUE if a car is in the passage from the basement
	2.	Controls Outputs:
	•	Y1: Red lights for both ends of the passage (ON = stop)
	•	Y2: Green lights for both ends (ON = proceed)
	3.	Implements the Logic:
	•	When a car enters from the ground floor (M1 or M4), set M20 := TRUE
	•	When a car enters from the basement (M2 or M3), set M30 := TRUE
	•	When a car exits (opposite sensor triggers), reset M20 or M30
	•	If either M20 or M30 is TRUE, the passage is occupied:
	•	Set Y1 := TRUE (red), Y2 := FALSE (green)
	•	If the passage is clear (M20 = FALSE and M30 = FALSE):
	•	Set Y1 := FALSE (red off), Y2 := TRUE (green on)
	4.	Ensure Initial State:
	•	On startup, allow passage (Y2 := TRUE, Y1 := FALSE)

⸻

🟧 F (Format) – Expected Output

You are expected to deliver a modular and readable Structured Text program, for example:
// Car enters from ground floor
IF M1 OR M4 THEN
    M20 := TRUE;
END_IF;

// Car enters from basement
IF M2 OR M3 THEN
    M30 := TRUE;
END_IF;

// Car exits from ground floor
IF M3 OR M4 THEN
    M20 := FALSE;
END_IF;

// Car exits from basement
IF M1 OR M2 THEN
    M30 := FALSE;
END_IF;

// Light control logic
IF M20 OR M30 THEN
    Y1 := TRUE;   // Red ON
    Y2 := FALSE;  // Green OFF
ELSE
    Y1 := FALSE;  // Red OFF
    Y2 := TRUE;   // Green ON
END_IF;

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text program to control a single-lane underground car park entry/exit system using photoelectric sensors and traffic lights, ensuring safe one-way passage by activating red lights when occupied and green lights when clear.
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

**R-T-F:**
🟥 R (Role) – Your Role

You are a PLC automation engineer tasked with programming a traffic light control system for a single-lane underground car park. The system must manage vehicle entry and exit from both the ground floor and basement, using sensors and memory flags, and control red and green lights accordingly to ensure safe one-way usage of the passage.

⸻

🟩 T (Task) – What You Need to Do

Write a Structured Text (ST) program in accordance with IEC 61131-3 standards that:
	1.	Monitors Sensors and Flags:
	•	X1: Photoelectric switch at ground floor (ON when a car passes)
	•	X2: Photoelectric switch at basement
	•	M1–M4: ON for one scan cycle when a car passes a sensor in a specific direction
	•	M20: TRUE if a car is in the passage from the ground floor
	•	M30: TRUE if a car is in the passage from the basement
	2.	Controls Outputs:
	•	Y1: Red lights for both ends of the passage (ON = stop)
	•	Y2: Green lights for both ends (ON = proceed)
	3.	Implements the Logic:
	•	When a car enters from the ground floor (M1 or M4), set M20 := TRUE
	•	When a car enters from the basement (M2 or M3), set M30 := TRUE
	•	When a car exits (opposite sensor triggers), reset M20 or M30
	•	If either M20 or M30 is TRUE, the passage is occupied:
	•	Set Y1 := TRUE (red), Y2 := FALSE (green)
	•	If the passage is clear (M20 = FALSE and M30 = FALSE):
	•	Set Y1 := FALSE (red off), Y2 := TRUE (green on)
	4.	Ensure Initial State:
	•	On startup, allow passage (Y2 := TRUE, Y1 := FALSE)

⸻

🟧 F (Format) – Expected Output

You are expected to deliver a modular and readable Structured Text program, for example:
// Car enters from ground floor
IF M1 OR M4 THEN
    M20 := TRUE;
END_IF;

// Car enters from basement
IF M2 OR M3 THEN
    M30 := TRUE;
END_IF;

// Car exits from ground floor
IF M3 OR M4 THEN
    M20 := FALSE;
END_IF;

// Car exits from basement
IF M1 OR M2 THEN
    M30 := FALSE;
END_IF;

// Light control logic
IF M20 OR M30 THEN
    Y1 := TRUE;   // Red ON
    Y2 := FALSE;  // Green OFF
ELSE
    Y1 := FALSE;  // Red OFF
    Y2 := TRUE;   // Green ON
END_IF;
FUNCTION_BLOCK CarParkEntryExitControl
VAR_INPUT
    X1 : BOOL; // Ground floor entry sensor
    X2 : BOOL; // Basement entry sensor
END_VAR

VAR_OUTPUT
    Y1 : BOOL; // Red light at ground floor
    Y2 : BOOL; // Green light at basement
END_VAR

VAR
    M1 : BOOL; // Ground floor entry detected
    M2 : BOOL; // Basement entry detected
    M3 : BOOL; // Basement exit detected
    M4 : BOOL; // Ground floor exit detected
    M20 : BOOL; // Car in passage from ground floor
    M30 : BOOL; // Car in passage from basement
END_VAR

// Initialize outputs
Y1 := FALSE;
Y2 := FALSE;

// Process inputs
M1 := X1;
M2 := X2;

// Process outputs
IF M1 OR M2 THEN
    M20 := TRUE;
ELSE
    M20 := FALSE;
END_IF;

IF M3 OR M4 THEN
    M30 := TRUE;
ELSE
    M30 := FALSE;
END_IF;

// Process logic
IF M20 OR M30 THEN
    Y1 := TRUE;
    Y2 := FALSE;
ELSE
    Y1 := FALSE;
    Y2 := TRUE;
END_IF;
END_FUNCTION_BLOCK

// Example usage:

// Car enters from ground floor
IF CarParkEntryExitControl.M1 OR CarParkEntryExitControl.M4 THEN
    CarParkEntryExitControl.M20 := TRUE;
END_IF;

// Car enters from basement
IF CarParkEntryExitControl.CarParkEntryExitControl.M2 OR CarParkExitControl.M3 THEN
    CarParkEntryExitControl.M30 := TRUE;
END_IF;

// Car exits from ground floor
IF CarParkEntryExitControl.CarParkEntryExitControl.M3 OR CarParkEntryExitControl.M4 THEN
    CarParkEntryExitControl.M20 := FALSE;
END_IF;

// Car exits from basement
IF CarParkEntryExitControl.CarParkEntryExitControl.M1 OR CarParkEntryExitControl.M2 THEN
    Car
