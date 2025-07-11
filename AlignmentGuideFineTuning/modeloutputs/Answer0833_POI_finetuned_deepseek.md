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
FUNCTION_BLOCK CANOpen_COBID_Manager
VAR_INPUT
    Enable : BOOL; // Enable COBID registration/deregistration
    COBID_ID : INT; // COBID ID to register/deregister
    Error : BOOL; // Error flag
END_VAR

VAR_OUTPUT
    COBID_Registered : BOOL; // TRUE if COBID is registered
    COBID_Deregistered : BOOL; // TRUE if COBID is deregistered
    Error_Occurred : BOOL; // TRUE if an error occurred
    Error_Code : INT; // Error code (0 = no error, 1 = invalid COBID, 2 = network error)
END_VAR

VAR
    COBID_Table : ARRAY[1..100] OF INT; // COBID table
    COBID_Index : INT; // Current COBID index
    COBID_Index_Max : INT; // Maximum COBID index
    COBID_Index_Min : INT; // Minimum COBID index
    COBID_Registered_Index : INT; // Index of registered COBID
    COBID_Deregistered_Index : INT; // Index of deregistered COBID
    COBID_Registered_Count : INT; // Number of registered COBIDs
    COBID_Deregistered_Count : INT; // Number of deregistered COBIDs
    COBID_Registered_Lock : BOOL; // Lock for registering COBIDs
    COBID_Deregistered_Lock : BOOL; // Lock for deregistering COBIDs
    COBID_Table_Lock : BOOL; // Lock for accessing COBID table
END_VAR

METHOD Execute : BOOL
BEGIN
    IF NOT Enable THEN
        COBID_Registered := FALSE;
        COBID_Deregistered := FALSE;
        Error_Occurred := FALSE;
        Error_Code := 0;
        RETURN;
    END_IF;

    // Check input values
    IF NOT Enable OR NOT COBID_ID.ALL THEN
        Error_Occurred := TRUE;
        Error_Code := 1;
        RETURN;
    END_IF;

    // Lock the COBID table
    CO
