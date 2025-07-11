### Intent:
The intent is to generate a control program for a urea reaction process that manages valve operations and monitors pressure/temperature conditions to ensure a safe and complete chemical reaction.

### Prompt:
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**T-A-G:**

🟥 T (Task)

Create a programming reference for the IEC 61131-3 Structured Text (ST) language by compiling a complete list of valid keywords.

🟩 A (Action)

Gather and categorize all official keywords specified in the IEC 61131-3 standard, including control flow structures (such as IF, CASE, FOR), standard functions (TON, CTU, ABS), and data types (INT, REAL, BOOL). Include concise usage examples or code snippets to illustrate how key functions and structures are typically used in automation programming.

🟦 G (Goal)

Deliver a well-organized, easy-to-use reference guide that supports engineers and developers in writing correct, efficient, and standards-compliant Structured Text code for industrial control systems.

### Generated Code:
The intent is to generate a control program for a urea reaction process that manages valve operations and monitors pressure/temperature conditions to ensure a safe and complete chemical reaction.
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**T-A-G:**

🟥 T (Task)

Create a programming reference for the IEC 61131-3 Structured Text (ST) language by compiling a complete list of valid keywords.

🟩 A (Action)

Gather and categorize all official keywords specified in the IEC 61131-3 standard, including control flow structures (such as IF, CASE, FOR), standard functions (TON, CTU, ABS), and data types (INT, REAL, BOOL). Include concise usage examples or code snippets to illustrate how key functions and structures are typically used in automation programming.

🟦 G (Goal)

Deliver a well-organized, easy-to-use reference guide that supports engineers and developers in writing correct, efficient, and standards-compliant Structured Text code for industrial control systems.
PROGRAM UreaReactionControl
VAR
    // Inputs
    StartReaction : BOOL; // Command to start the reaction
    StopReaction : BOOL;  // Command to stop the reaction
    AmmoniaValveOpen : BOOL; // Status of ammonia valve
    CO2ValveOpen : BOOL; // Status of CO2 valve
    ReactionPressure : REAL; // Measured pressure in the reactor
    ReactionTemperature : REAL; // Measured temperature in the reactor

    // Outputs
    AmmoniaValveCommand : BOOL; // Command to open or close the ammonia valve
    CO2ValveCommand : BOOL; // Command to open or close the CO2 valve
    ReactionComplete : BOOL; // Status indicating if the reaction is complete
    Error : BOOL; // Status indicating if an error occurred

    // Internal Variables
    ReactionRunning : BOOL := FALSE; // Status indicating if the reaction is currently running
    ReactionStarted : BOOL := FALSE; // Status indicating if the reaction has been started
    ReactionCompleteFlag : BOOL := FALSE; // Flag indicating if the reaction is complete
    ReactionTimer : TON; // Timer to monitor the reaction duration
    ReactionTargetPressure : REAL := 120.0; // Target pressure for the reaction (bar)
    ReactionTargetTemperature : REAL := 180.0; // Target temperature for the reaction (°C)
END_VAR

// Initialize the timer with a 10-second timeout
ReactionTimer(IN := FALSE, PT := T#10s);

// Main control logic
IF StartReaction AND NOT ReactionRunning THEN
    // Start the reaction
    ReactionRunning := TRUE;
    ReactionTimer(IN := TRUE);
    AmmoniaValveCommand := TRUE; // Open the ammonia valve
    CO2ValveCommand := TRUE; // Open the CO2 valve
    ReactionCompleteFlag := FALSE;
END_IF

IF StopReaction AND ReactionRunning THEN
    // Stop the reaction
    ReactionRunning := FALSE;
    ReactionTimer(IN := FALSE);
    Ammon
