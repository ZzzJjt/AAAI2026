### Intent:
**Intent Summary:**  
Develop an OPC UA subscription function block in IEC 61131-3 Structured Text to create, manage, and monitor real-time data subscriptions with configurable priority and interval, while handling errors and connection states.  

*(Focus: OPC UA subscription lifecycle, error handling, and real-time monitoring for industrial control systems.)*

### Prompt:
**Ethernet PowerLink Diagnostics Using IEC 61131-3 Structured Text:**

Develop a function block in structured text (ST) based on IEC 61131 standards to retrieve Ethernet PowerLink diagnostic information from a control node device via a PowerLink managing node (MN). The function block should collect and display key diagnostic data such as communication status, error codes, and node health. The program must ensure that the diagnostic information is accurately processed and relayed to the controller for further analysis. Discuss how the function block interacts with the PowerLink network, handles error detection, and provides real-time diagnostics for maintaining network integrity.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop an IEC 61131-3 Structured Text (ST) function block to retrieve and process diagnostic information from Ethernet PowerLink control nodes via a Managing Node (MN).

🟩 A (Action) – How to Do It

Implement logic to cyclically collect key diagnostic data such as communication status, error codes, and node health. The function block should interact with the MN to access diagnostic registers, process and validate the received data, detect errors, and forward structured output to the controller. Include logic for fault handling and ensure that the data is refreshed in real time for monitoring and logging purposes.

🟦 G (Goal) – What You Want to Achieve

Provide a reliable and reusable diagnostic tool that enables real-time visibility into the condition of PowerLink nodes, improves troubleshooting efficiency, and supports the long-term stability and maintainability of the communication network.

### Generated Code:
**Intent Summary:**  
Develop an OPC UA subscription function block in IEC 61131-3 Structured Text to create, manage, and monitor real-time data subscriptions with configurable priority and interval, while handling errors and connection states.  

*(Focus: OPC UA subscription lifecycle, error handling, and real-time monitoring for industrial control systems.)*
**Ethernet PowerLink Diagnostics Using IEC 61131-3 Structured Text:**

Develop a function block in structured text (ST) based on IEC 61131 standards to retrieve Ethernet PowerLink diagnostic information from a control node device via a PowerLink managing node (MN). The function block should collect and display key diagnostic data such as communication status, error codes, and node health. The program must ensure that the diagnostic information is accurately processed and relayed to the controller for further analysis. Discuss how the function block interacts with the PowerLink network, handles error detection, and provides real-time diagnostics for maintaining network integrity.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop an IEC 61131-3 Structured Text (ST) function block to retrieve and process diagnostic information from Ethernet PowerLink control nodes via a Managing Node (MN).

🟩 A (Action) – How to Do It

Implement logic to cyclically collect key diagnostic data such as communication status, error codes, and node health. The function block should interact with the MN to access diagnostic registers, process and validate the received data, detect errors, and forward structured output to the controller. Include logic for fault handling and ensure that the data is refreshed in real time for monitoring and logging purposes.

🟦 G (Goal) – What You Want to Achieve

Provide a reliable and reusable diagnostic tool that enables real-time visibility into the condition of PowerLink nodes, improves troubleshooting efficiency, and supports the long-term stability and maintainability of the communication network.
(* IEC 61131-3 Structured Text Function Block for OPC UA Subscription Management *)
(* Purpose: Creates, manages, and monitors real-time OPC UA subscriptions *)

FUNCTION_BLOCK OPCUA_SubscriptionManager
VAR_INPUT
    Execute : BOOL;                  (* Trigger subscription creation/update *)
    SubscriptionID : STRING[20];     (* Unique subscription identifier *)
    Priority : INT;                  (* Subscription priority (1-10) *)
    Interval : TIME;                 (* Subscription interval in seconds *)
    ConnectionState : BOOL;          (* TRUE if connection is active *)
    Error : BOOL;                    (* TRUE if error occurred *)
END_VAR

VAR_OUTPUT
    SubscriptionCreated : BOOL;      (* TRUE if subscription is created successfully *)
    SubscriptionUpdated : BOOL;      (* TRUE if subscription is updated successfully *)
    SubscriptionError : BOOL;       (* TRUE if error occurred during subscription *)
    SubscriptionErrorID : INT;      (* Error code (0=NoError, 1=InvalidSubscriptionID, 2=InvalidPriority, 3=InvalidInterval, 4=InvalidConnectionState, 5=InvalidError) *)
    SubscriptionErrorText : STRING[255]; (* Detailed error message *)
END_VAR

VAR
    Subscriptions : ARRAY[1..10] OF OPCUA_Subscription; (* Array of subscriptions *)
    CurrentSubscription : OPCUA_Subscription; (* Current subscription *)
    CurrentSubscriptionIndex : INT; (* Current subscription index *)
    SubscriptionIndex : INT; (* Subscription index for error handling *)
    SubscriptionIDExists : BOOL; (* TRUE if subscription exists *)
    SubscriptionErrorID : INT; (* Error code *)
    SubscriptionErrorText : STRING[255]; (* Error message *)
    SubscriptionError : BOOL; (* TRUE if error occurred *)
    SubscriptionCreated : BOOL; (* TRUE if subscription is created successfully *)
    SubscriptionUpdated : BOOL; (* TRUE if subscription is updated successfully *)
    SubscriptionErrorText : STRING[255]; (* Error message *)
END_VAR

(* Initialize variables *)
SubscriptionIndex := 0;
SubscriptionErrorID := 0;
SubscriptionErrorText := '';
SubscriptionError := FALSE;
SubscriptionCreated := FALSE;
SubscriptionUpdated := FALSE;

(* Execute subscription management *)
IF Execute THEN
    (* Check if subscription exists *)
