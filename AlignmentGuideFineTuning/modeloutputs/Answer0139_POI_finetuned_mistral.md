### Intent:
The task is to create a fixed traffic light control system in IEC 61131-3 Structured Text that implements a state machine with timed transitions, pedestrian crossing support, emergency vehicle priority, and safe light sequencing while adhering to PLC programming standards.

### Prompt:
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**B-A-B:**

🟥 Before – The Current Situation

You are working with IEC 61131-3 Structured Text, a standard language used in industrial automation for programmable logic controllers (PLCs). Developers often struggle to find a single, consolidated reference that lists all valid keywords, especially for control flow, data types, and functions, along with practical usage examples.

⸻

🟩 After – The Desired Outcome

You will have a comprehensive, well-organized programming reference that includes:
	•	All reserved keywords and standard identifiers in IEC 61131-3 Structured Text
	•	Control structures such as IF, CASE, FOR, WHILE, etc.
	•	Data types including BOOL, INT, REAL, ARRAY, STRUCT, and more
	•	Standard functions and function blocks, like TON, CTU, ABS, SQRT, with example usages
	•	Brief code snippets to demonstrate how the most important constructs are used in practice

⸻

🟦 Bridge – What You Need to Do

Compile and present a structured reference document that includes:
	1.	A keyword category breakdown:
	•	Control flow (IF, ELSIF, END_IF, CASE, FOR, REPEAT, etc.)
	•	Data types (BOOL, INT, REAL, TIME, STRING, etc.)
	•	Operators (AND, OR, MOD, NOT, etc.)
	•	System constants (TRUE, FALSE, MAX, MIN, etc.)
	2.	A section on standard functions and function blocks with:
	•	Brief descriptions
	•	IEC 61131-3-compliant usage examples
	•	Notes on any vendor-specific behavior, if applicable
	3.	A downloadable or easily searchable format, such as:
	•	A table or checklist format for fast lookup
	•	Highlighted example blocks like:

 VAR
  x: INT := 5;
  y: INT := 10;
  result: BOOL;
END_VAR

IF x < y THEN
  result := TRUE;
END_IF;

### Generated Code:
The task is to create a fixed traffic light control system in IEC 61131-3 Structured Text that implements a state machine with timed transitions, pedestrian crossing support, emergency vehicle priority, and safe light sequencing while adhering to PLC programming standards.
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**B-A-B:**

🟥 Before – The Current Situation

You are working with IEC 61131-3 Structured Text, a standard language used in industrial automation for programmable logic controllers (PLCs). Developers often struggle to find a single, consolidated reference that lists all valid keywords, especially for control flow, data types, and functions, along with practical usage examples.

⸻

🟩 After – The Desired Outcome

You will have a comprehensive, well-organized programming reference that includes:
	•	All reserved keywords and standard identifiers in IEC 61131-3 Structured Text
	•	Control structures such as IF, CASE, FOR, WHILE, etc.
	•	Data types including BOOL, INT, REAL, ARRAY, STRUCT, and more
	•	Standard functions and function blocks, like TON, CTU, ABS, SQRT, with example usages
	•	Brief code snippets to demonstrate how the most important constructs are used in practice

⸻

🟦 Bridge – What You Need to Do

Compile and present a structured reference document that includes:
	1.	A keyword category breakdown:
	•	Control flow (IF, ELSIF, END_IF, CASE, FOR, REPEAT, etc.)
	•	Data types (BOOL, INT, REAL, TIME, STRING, etc.)
	•	Operators (AND, OR, MOD, NOT, etc.)
	•	System constants (TRUE, FALSE, MAX, MIN, etc.)
	2.	A section on standard functions and function blocks with:
	•	Brief descriptions
	•	IEC 61131-3-compliant usage examples
	•	Notes on any vendor-specific behavior, if applicable
	3.	A downloadable or easily searchable format, such as:
	•	A table or checklist format for fast lookup
	•	Highlighted example blocks like:

 VAR
  x: INT := 5;
  y: INT := 10;
  result: BOOL;
END_VAR

IF x < y THEN
  result := TRUE;
END_IF;
This will help developers:
	•	Avoid syntax errors
	•	Learn and apply new constructs quickly
	•	Write clean, maintainable PLC code that meets industrial standards
FUNCTION_BLOCK FixedTrafficLightControl
VAR_INPUT
    Enable : BOOL; // Enable signal to start traffic light operation
END_VAR

VAR_OUTPUT
    RedLight : BOOL; // Red light output
    GreenLight : BOOL; // Green light output
    YellowLight : BOOL; // Yellow light output
    PedestrianCrossing : BOOL; // Pedestrian crossing output
    EmergencyVehicle : BOOL; // Emergency vehicle override output
END_VAR

VAR
    State : INT := 0; // Traffic light state (0 = Red, 1 = Green, 2 = Yellow, 3 = Pedestrian, 4 = Emergency)
    Timer : TON; // Timer for light transitions
    PedestrianRequest : BOOL; // Pedestrian request input
    EmergencyRequest : BOOL; // Emergency vehicle request input
END_VAR

// Initialize outputs
RedLight := FALSE;
GreenLight := FALSE;
YellowLight := FALSE;
PedestrianCrossing := FALSE;
EmergencyVehicle := FALSE;

// Main control loop
IF Enable THEN
    CASE State OF
        0: // Red light
            GreenLight := FALSE;
            YellowLight := FALSE;
            PedestrianCrossing := FALSE;
            EmergencyVehicle := FALSE;
            RedLight := TRUE;
            Timer(IN := NOT RedLight, PT := T#10s); // Hold red light for 10 seconds
            IF Timer.Q THEN
                State := 1; // Transition to green light
                Timer(IN := FALSE);
            END_IF;

        1: // Green light
            RedLight := FALSE;
            YellowLight := FALSE;
            PedestrianCrossing := FALSE;
            EmergencyVehicle := FALSE;
            GreenLight := TRUE;
            Timer(IN := NOT GreenLight, PT := T#10s); // Hold green light for 10 seconds
            IF Timer.Q THEN
                State :=
