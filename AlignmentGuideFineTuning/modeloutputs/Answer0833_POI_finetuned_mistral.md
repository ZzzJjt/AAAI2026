### Intent:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block to manage CANOpen COBID registration/deregistration with robust error handling, network checks, and dynamic table management for reliable industrial communication.  

*(Focus: CANOpen COBID control, error handling, real-time registration tracking)*

### Prompt:
**EtherCAT State Machine Control Using IEC 61131-3 Structured Text:**

Develop an IEC 61131-3 structured text (ST) program to sequentially transition through all the states of an EtherCAT slave device using the ESM (EtherCAT State Machine) function block. The program should use descriptive state names (such as INIT, PREOP, SAFEOP, OP, etc.) rather than numerical values, ensuring that state transitions occur only when allowed. A 5-second timer delay should be implemented before each state transition to ensure proper timing and stabilization. Discuss the implementation of the EtherCAT state machine, including logic for handling state transitions, error checking, and ensuring compliance with EtherCAT protocol requirements.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop an IEC 61131-3 Structured Text (ST) program to control the EtherCAT State Machine (ESM) for a slave device.

🟩 A (Action) – How to Do It

Write logic that sequentially transitions the slave through the standard EtherCAT states: INIT, PREOP, SAFEOP, and OP. Use symbolic state names instead of numeric values to improve readability. Implement a 5-second timer delay before each transition to ensure stability, and include condition checks to verify that transitions are valid. Incorporate error-handling routines to detect and respond to failed or illegal transitions.

🟦 G (Goal) – What You Want to Achieve

Ensure reliable, protocol-compliant EtherCAT state control with readable, maintainable code that supports safe transitions, proper timing, and real-time fault handling for industrial communication systems.

### Generated Code:
**Intent Summary:**  
Develop an IEC 61131-3 Structured Text function block to manage CANOpen COBID registration/deregistration with robust error handling, network checks, and dynamic table management for reliable industrial communication.  

*(Focus: CANOpen COBID control, error handling, real-time registration tracking)*
**EtherCAT State Machine Control Using IEC 61131-3 Structured Text:**

Develop an IEC 61131-3 structured text (ST) program to sequentially transition through all the states of an EtherCAT slave device using the ESM (EtherCAT State Machine) function block. The program should use descriptive state names (such as INIT, PREOP, SAFEOP, OP, etc.) rather than numerical values, ensuring that state transitions occur only when allowed. A 5-second timer delay should be implemented before each state transition to ensure proper timing and stabilization. Discuss the implementation of the EtherCAT state machine, including logic for handling state transitions, error checking, and ensuring compliance with EtherCAT protocol requirements.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop an IEC 61131-3 Structured Text (ST) program to control the EtherCAT State Machine (ESM) for a slave device.

🟩 A (Action) – How to Do It

Write logic that sequentially transitions the slave through the standard EtherCAT states: INIT, PREOP, SAFEOP, and OP. Use symbolic state names instead of numeric values to improve readability. Implement a 5-second timer delay before each transition to ensure stability, and include condition checks to verify that transitions are valid. Incorporate error-handling routines to detect and respond to failed or illegal transitions.

🟦 G (Goal) – What You Want to Achieve

Ensure reliable, protocol-compliant EtherCAT state control with readable, maintainable code that supports safe transitions, proper timing, and real-time fault handling for industrial communication systems.
FUNCTION_BLOCK CANOpenCOBIDRegistration
VAR_INPUT
    Execute : BOOL; // Trigger registration on rising edge
    COBID : UINT;   // CANOpen network identifier (0–1023)
    NodeID : UINT;   // CANOpen node identifier (0–127)
    Timeout : TIME;  // Maximum wait time for registration
END_VAR

VAR_OUTPUT
    Done : BOOL;     // TRUE when registration is complete
    Error : BOOL;    // TRUE if an error occurs
    ErrorID : UINT;  // Error code (0 = No error, 1 = Invalid COBID, 2 = Invalid NodeID, 3 = Timeout, 4 = Network error)
    RegistrationStatus : UINT; // 0 = Unregistered, 1 = Registered
END_VAR

VAR
    PrevExecute : BOOL; // For edge detection
    RegistrationAttempted : BOOL; // Tracks if registration is in progress
    RegistrationComplete : BOOL; // Tracks if registration is successful
    NetworkError : BOOL; // Tracks if network error is detected
    RegistrationTimer : TON; // Timer for timeout detection
END_VAR

// Reset outputs on rising edge of Execute
PrevExecute := Execute;
IF Execute AND NOT PrevExecute THEN
    Done := FALSE;
    Error := FALSE;
    ErrorID := 0;
    RegistrationStatus := 0;
    RegistrationAttempted := FALSE;
    RegistrationComplete := FALSE;
    NetworkError := FALSE;
    RegistrationTimer(IN := FALSE); // Reset timer
END_IF;
PrevExecute := Execute;

// Check if Execute is TRUE and registration is not in progress
IF Execute AND NOT RegistrationAttempted THEN
    // Validate COBID and NodeID
    IF COBID > 1023 OR COBID = 0 OR NodeID > 127 OR NodeID = 0 THEN
        Error := TRUE;
        ErrorID := 1; // Invalid COBID or NodeID
        Done := FALSE;
        RegistrationStatus := 0;
        RegistrationComplete := FALSE;
        NetworkError :=
