### Intent:
The task is to develop an IEC 61131-3 Structured Text program that controls an EtherCAT slave device's state machine, ensuring sequential transitions (INIT→PREOP→SAFEOP→OP) with 5-second delays, symbolic state names, and protocol-compliant error handling.  

*(Intent: Generate ST code for EtherCAT state machine control with timed transitions and fault detection.)*

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
The task is to develop an IEC 61131-3 Structured Text program that controls an EtherCAT slave device's state machine, ensuring sequential transitions (INIT→PREOP→SAFEOP→OP) with 5-second delays, symbolic state names, and protocol-compliant error handling.  

*(Intent: Generate ST code for EtherCAT state machine control with timed transitions and fault detection.)*
**EtherCAT State Machine Control Using IEC 61131-3 Structured Text:**

Develop an IEC 61131-3 structured text (ST) program to sequentially transition through all the states of an EtherCAT slave device using the ESM (EtherCAT State Machine) function block. The program should use descriptive state names (such as INIT, PREOP, SAFEOP, OP, etc.) rather than numerical values, ensuring that state transitions occur only when allowed. A 5-second timer delay should be implemented before each state transition to ensure proper timing and stabilization. Discuss the implementation of the EtherCAT state machine, including logic for handling state transitions, error checking, and ensuring compliance with EtherCAT protocol requirements.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop an IEC 61131-3 Structured Text (ST) program to control the EtherCAT State Machine (ESM) for a slave device.

🟩 A (Action) – How to Do It

Write logic that sequentially transitions the slave through the standard EtherCAT states: INIT, PREOP, SAFEOP, and OP. Use symbolic state names instead of numeric values to improve readability. Implement a 5-second timer delay before each transition to ensure stability, and include condition checks to verify that transitions are valid. Incorporate error-handling routines to detect and respond to failed or illegal transitions.

🟦 G (Goal) – What You Want to Achieve

Ensure reliable, protocol-compliant EtherCAT state control with readable, maintainable code that supports safe transitions, proper timing, and real-time fault handling for industrial communication systems.
(* IEC 61131-3 Structured Text Program: EtherCATStateMachineControl *)
(* Purpose: Controls EtherCAT slave state machine with symbolic names and timed transitions *)

PROGRAM EtherCATStateMachineControl
VAR
    (* Inputs *)
    Execute : BOOL;                    (* TRUE to execute state machine *)
    Reset : BOOL;                      (* TRUE to reset to INIT state *)
    FaultDetected : BOOL;              (* TRUE if fault detected *)
    
    (* Outputs *)
    CurrentState : STRING[10];         (* Current state name: INIT, PREOP, SAFEOP, OP *)
    TransitionComplete : BOOL;         (* TRUE when transition completes *)
    Fault : BOOL;                      (* TRUE if fault occurs *)
    
    (* Internal Variables *)
    StateMachine : ESM;                 (* EtherCAT State Machine function block *)
    Timer : TON;                       (* 5-second timer for transition delay *)
    StateTimer : TON;                  (* Internal timer for state stabilization *)
    StateTransitionAllowed : BOOL;      (* TRUE if next transition is allowed *)
    ResetState : BOOL;                 (* Reset state to INIT *)
    StateFault : BOOL;                 (* Fault detected during state *)
    TransitionError : BOOL;            (* TRUE if transition fails *)
    
    (* Constants *)
    STATE_INIT : STRING := 'INIT';     (* Initial state *)
    STATE_PREOP : STRING := 'PREOP';   (* Pre-operation state *)
    STATE_SAFEOP : STRING := 'SAFEOP'; (* Safe operation state *)
    STATE_OP : STRING := 'OP';         (* Operation state *)
    STATE_ERROR : STRING := 'ERROR';   (* Error state *)
    TRANSITION_DELAY : TIME := T#5s;   (* 5-second delay between transitions *)
END_VAR

(* Initialize variables *)
StateMachine(STATE).STATE := STATE_INIT;
Timer(IN).T# := TRANSITION_DELAY;
Timer(ET).T# := TRANSITION_DELAY
