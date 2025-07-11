### Intent:
**Intent Summary:**  
Create a Structured Text program that maintains a 2:1 flow ratio between two reactants (A and B) with safety checks, emergency stop handling, and alarm management for an industrial mixing process.

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
**Intent Summary:**  
Create a Structured Text program that maintains a 2:1 flow ratio between two reactants (A and B) with safety checks, emergency stop handling, and alarm management for an industrial mixing process.
**Programming Reference:**
Compile a comprehensive list of all valid keywords used in the IEC 61131-3 Structured Text programming language, ensuring that it covers both standard control flow structures and data types. Include examples of usage for key functions where applicable.

**T-A-G:**

🟥 T (Task)

Create a programming reference for the IEC 61131-3 Structured Text (ST) language by compiling a complete list of valid keywords.

🟩 A (Action)

Gather and categorize all official keywords specified in the IEC 61131-3 standard, including control flow structures (such as IF, CASE, FOR), standard functions (TON, CTU, ABS), and data types (INT, REAL, BOOL). Include concise usage examples or code snippets to illustrate how key functions and structures are typically used in automation programming.

🟦 G (Goal)

Deliver a well-organized, easy-to-use reference guide that supports engineers and developers in writing correct, efficient, and standards-compliant Structured Text code for industrial control systems.
(* Program: Ratio Control for Reactant Mixing *)
(* Version: 1.0, Date: 2025-05-21 *)
(* Maintains 2:1 flow ratio between reactants A and B *)
(* Uses flow measurements, safety checks, and emergency stop *)
(* Written to IEC 61131-3 Structured Text standards *)

PROGRAM RatioControl
VAR
    (* Inputs *)
    FlowA_PV : REAL;                  (* Measured flow rate of reactant A, L/min *)
    FlowB_PV : REAL;                  (* Measured flow rate of reactant B, L/min *)
    EmergencyStop : BOOL;             (* TRUE if emergency stop activated *)
    
    (* Outputs *)
    FlowA_SP : REAL;                  (* Setpoint for reactant A flow, L/min *)
    FlowB_SP : REAL;                  (* Setpoint for reactant B flow, L/min *)
    AlarmA : BOOL;                    (* TRUE if A flow out of range *)
    AlarmB : BOOL;                    (* TRUE if B flow out of range *)
    Error : BOOL;                     (* TRUE if system error *)
    
    (* Internal Variables *)
    RatioSetpoint : REAL := 2.0;      (* Desired flow ratio A:B *)
    FlowA_Error : BOOL := FALSE;      (* TRUE if A flow invalid *)
    FlowB_Error : BOOL := FALSE;      (* TRUE if B flow invalid *)
    FlowA_Valid : BOOL := FALSE;      (* TRUE if A flow valid *)
    FlowB_Valid : BOOL := FALSE;      (* TRUE if B flow valid *)
    FlowA_Ratio : REAL;               (* Ratio of A:B flow *)
    FlowB_Ratio : REAL;               (* Ratio of B:A flow *)
    FlowA_Adjustment : REAL;          (* Adjustment to A flow to maintain ratio *)
    FlowB_Adjustment : REAL;          (* Adjustment to B flow to maintain ratio *)
    FlowA_Max : REAL := 100.0;        (* Max flow rate
