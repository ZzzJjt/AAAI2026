### Intent:
**Intent Summary:**  
Create a Structured Text program to control a urea production reaction by managing ammonia and CO₂ valve operations, monitoring pressure/temperature conditions, and timing the reaction process until completion.  

(Key elements: valve control, condition monitoring, timed reaction, process automation)

### Prompt:
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**C-A-R-E:**

🟥 C (Context)

IEC 61131-3 Structured Text is a widely used programming language in industrial automation. Despite its standardized nature, many developers lack a single, comprehensive reference that clearly lists all valid keywords, data types, and control structures, along with practical usage examples. This makes learning, troubleshooting, and implementing efficient code more challenging—especially for new programmers or teams working across different vendors.

⸻

🟩 A (Action)

Create a comprehensive, categorized reference document that includes:
	•	All reserved keywords in Structured Text (ST), such as control structures (IF, CASE, FOR, WHILE, etc.)
	•	Core data types (BOOL, INT, REAL, TIME, STRING, ARRAY, etc.)
	•	Logical and arithmetic operators (AND, OR, MOD, NOT, +, -, etc.)
	•	System constants and standard function blocks (TRUE, FALSE, TON, CTU, ABS, SQRT, etc.)
	•	Code examples for commonly used constructs (e.g., how to use a timer, write a loop, or declare arrays)

⸻

🟨 R (Result)

The result will be a clear, structured, and practical programming reference for IEC 61131-3 Structured Text, which:
	•	Makes it faster and easier for developers to write compliant and efficient code
	•	Serves as a daily reference tool for both new and experienced automation engineers
	•	Helps reduce syntax errors, debugging time, and onboarding effort
	•	Can be formatted as a PDF cheat sheet, a webpage, or even an IDE-integrated tooltip system

⸻

🟦 E (Example)

IF-THEN-ELSE syntax:

VAR
  Temp : REAL := 85.0;
  Overheat : BOOL;
END_VAR

IF Temp > 100.0 THEN
  Overheat := TRUE;
ELSE
  Overheat := FALSE;
END_IF;

TON (On-delay timer) function block:

VAR
  Timer1 : TON;
  Start  : BOOL;
END_VAR

Timer1(IN := Start, PT := T#5s);
IF Timer1.Q THEN
  // Execute action when timer completes
END_IF;

### Generated Code:
**Intent Summary:**  
Create a Structured Text program to control a urea production reaction by managing ammonia and CO₂ valve operations, monitoring pressure/temperature conditions, and timing the reaction process until completion.  

(Key elements: valve control, condition monitoring, timed reaction, process automation)
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**C-A-R-E:**

🟥 C (Context)

IEC 61131-3 Structured Text is a widely used programming language in industrial automation. Despite its standardized nature, many developers lack a single, comprehensive reference that clearly lists all valid keywords, data types, and control structures, along with practical usage examples. This makes learning, troubleshooting, and implementing efficient code more challenging—especially for new programmers or teams working across different vendors.

⸻

🟩 A (Action)

Create a comprehensive, categorized reference document that includes:
	•	All reserved keywords in Structured Text (ST), such as control structures (IF, CASE, FOR, WHILE, etc.)
	•	Core data types (BOOL, INT, REAL, TIME, STRING, ARRAY, etc.)
	•	Logical and arithmetic operators (AND, OR, MOD, NOT, +, -, etc.)
	•	System constants and standard function blocks (TRUE, FALSE, TON, CTU, ABS, SQRT, etc.)
	•	Code examples for commonly used constructs (e.g., how to use a timer, write a loop, or declare arrays)

⸻

🟨 R (Result)

The result will be a clear, structured, and practical programming reference for IEC 61131-3 Structured Text, which:
	•	Makes it faster and easier for developers to write compliant and efficient code
	•	Serves as a daily reference tool for both new and experienced automation engineers
	•	Helps reduce syntax errors, debugging time, and onboarding effort
	•	Can be formatted as a PDF cheat sheet, a webpage, or even an IDE-integrated tooltip system

⸻

🟦 E (Example)

IF-THEN-ELSE syntax:

VAR
  Temp : REAL := 85.0;
  Overheat : BOOL;
END_VAR

IF Temp > 100.0 THEN
  Overheat := TRUE;
ELSE
  Overheat := FALSE;
END_IF;

TON (On-delay timer) function block:

VAR
  Timer1 : TON;
  Start  : BOOL;
END_VAR

Timer1(IN := Start, PT := T#5s);
IF Timer1.Q THEN
  // Execute action when timer completes
END_IF;

// Example array declaration:

VAR
  MyArray : ARRAY[1..10] OF INT := [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
END_VAR

// Example loop:

FOR i := 1 TO 10 DO
  // Perform action on each element
END_FOR;

// Example condition:

IF i = 5 THEN
  // Execute special action for index 5
END_IF;
FUNCTION_BLOCK UreaReactionControlFB
VAR_INPUT
    AmmoniaValve : BOOL; // Control ammonia flow to reactor
    CO2Valve : BOOL;     // Control CO₂ flow to reactor
    PressureSensor : REAL; // Measure pressure in reactor
    TemperatureSensor : REAL; // Measure temperature in reactor
    StartReaction : BOOL; // Start reaction
    StopReaction : BOOL; // Stop reaction
END_VAR

VAR_OUTPUT
    AmmoniaValve_Output : BOOL; // Control ammonia valve
    CO2Valve_Output : BOOL;    // Control CO₂ valve
    ReactionRunning : BOOL;    // Flag indicating whether reaction is running
END_VAR

VAR
    ReactionComplete : BOOL := FALSE; // Flag indicating whether reaction is complete
    ReactionTime : TIME; // Time since reaction started
    ReactionTimer : TON; // Timer to control reaction duration
END_VAR

// Initialize outputs
AmmoniaValve_Output := FALSE;
CO2Valve_Output := FALSE;
ReactionRunning := FALSE;

// Initialize timer
ReactionTimer(IN := StartReaction, PT := T#10m);

// Main logic
IF StartReaction THEN
    // Start timer and set outputs
    ReactionTimer(IN := TRUE);
    AmmoniaValve_Output := TRUE;
    CO2Valve_Output := TRUE;
    ReactionRunning := TRUE;

    // Reset timer when reaction is complete
    ReactionComplete := TRUE;
    ReactionTimer(IN := FALSE);
END_IF;

// Check if reaction is complete
IF ReactionTimer.Q AND NOT ReactionRunning THEN
    ReactionComplete := TRUE;
END_IF;
