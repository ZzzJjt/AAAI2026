### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block that wraps a C-based OPC UA subscription manager (using Open62541) to dynamically establish and monitor subscriptions with configurable intervals, priority, and timeout, while providing real-time status flags and error handling for PLC integration.  

*(Focus: C/ST integration, OPC UA subscription management, and industrial communication robustness.)*

### Prompt:
**OPC UA Subscription Creation Using Open62541 and IEC 61131-3 Structured Text:**

Develop a C function block for OPC UA subscription creation using the Open62541 library, which will be wrapped in IEC 61131-3 structured text code. The function block receives a Connection Handle as a DWORD and has the following inputs: an executed flag (BOOL), a priority (BYTE), and a timeout (TIME). As outputs, it provides three status flags (Done, Busy, Error) along with two DWORD outputs (ErrorID, SubscriptionHdl). The function block also includes an IN/OUT variable PublishingInterval (type TIME), which allows dynamic adjustment of the subscription interval.

In your explanation, describe how this C function block can be wrapped inside IEC 61131-3 structured text code, highlighting the integration steps and providing an example of how to call the function block within an ST program. Discuss error handling, subscription management, and real-time communication with OPC UA servers.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a C-based OPC UA subscription function block using the open62541 library and integrate it into an IEC 61131-3 Structured Text function block for use in a PLC.

⸻

🟩 A (Action) – How to Do It

Implement the subscription logic in C, including setting the publishing interval, priority, and managing the connection session using a ConnectionHdl (DWORD). The C function must return status and a SubscriptionHdl. Then wrap this logic in a Structured Text (ST) function block with the following interface:

Inputs:
	•	Execute (BOOL) – Starts the subscription creation
	•	ConnectionHdl (DWORD) – OPC UA session handle
	•	Priority (BYTE) – Defines subscription priority
	•	Timeout (TIME) – Maximum wait time
	•	PublishingInterval (IN/OUT, TIME) – Defines or updates the subscription rate

Outputs:
	•	Done (BOOL) – TRUE when the subscription is successfully created
	•	Busy (BOOL) – TRUE while the process is ongoing
	•	Error (BOOL) – TRUE if a failure occurs
	•	ErrorID (DWORD) – Returns diagnostic error code
	•	SubscriptionHdl (DWORD) – Outputs the subscription handle

In the ST logic, use rising-edge detection on Execute, manage output flags accordingly, and allow real-time updates to the PublishingInterval.

⸻

🟦 G (Goal) – What You Want to Achieve

Provide a reliable and reusable function block that allows PLC programs to dynamically create and manage OPC UA subscriptions from Structured Text, with full visibility into execution status and error codes. This enables real-time data updates, adaptive communication handling, and streamlined integration with external OPC UA servers in industrial control systems.

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block that wraps a C-based OPC UA subscription manager (using Open62541) to dynamically establish and monitor subscriptions with configurable intervals, priority, and timeout, while providing real-time status flags and error handling for PLC integration.  

*(Focus: C/ST integration, OPC UA subscription management, and industrial communication robustness.)*
**OPC UA Subscription Creation Using Open62541 and IEC 61131-3 Structured Text:**

Develop a C function block for OPC UA subscription creation using the Open62541 library, which will be wrapped in IEC 61131-3 structured text code. The function block receives a Connection Handle as a DWORD and has the following inputs: an executed flag (BOOL), a priority (BYTE), and a timeout (TIME). As outputs, it provides three status flags (Done, Busy, Error) along with two DWORD outputs (ErrorID, SubscriptionHdl). The function block also includes an IN/OUT variable PublishingInterval (type TIME), which allows dynamic adjustment of the subscription interval.

In your explanation, describe how this C function block can be wrapped inside IEC 61131-3 structured text code, highlighting the integration steps and providing an example of how to call the function block within an ST program. Discuss error handling, subscription management, and real-time communication with OPC UA servers.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a C-based OPC UA subscription function block using the open62541 library and integrate it into an IEC 61131-3 Structured Text function block for use in a PLC.

⸻

🟩 A (Action) – How to Do It

Implement the subscription logic in C, including setting the publishing interval, priority, and managing the connection session using a ConnectionHdl (DWORD). The C function must return status and a SubscriptionHdl. Then wrap this logic in a Structured Text (ST) function block with the following interface:

Inputs:
	•	Execute (BOOL) – Starts the subscription creation
	•	ConnectionHdl (DWORD) – OPC UA session handle
	•	Priority (BYTE) – Defines subscription priority
	•	Timeout (TIME) – Maximum wait time
	•	PublishingInterval (IN/OUT, TIME) – Defines or updates the subscription rate

Outputs:
	•	Done (BOOL) – TRUE when the subscription is successfully created
	•	Busy (BOOL) – TRUE while the process is ongoing
	•	Error (BOOL) – TRUE if a failure occurs
	•	ErrorID (DWORD) – Returns diagnostic error code
	•	SubscriptionHdl (DWORD) – Outputs the subscription handle

In the ST logic, use rising-edge detection on Execute, manage output flags accordingly, and allow real-time updates to the PublishingInterval.

⸻

🟦 G (Goal) – What You Want to Achieve

Provide a reliable and reusable function block that allows PLC programs to dynamically create and manage OPC UA subscriptions from Structured Text, with full visibility into execution status and error codes. This enables real-time data updates, adaptive communication handling, and streamlined integration with external OPC UA servers in industrial control systems.
FUNCTION_BLOCK FB_OPCUA_SUBSCRIBE
VAR_INPUT
    Execute : BOOL;                   // Rising edge triggers subscription
    ConnectionHdl : DWORD;            // OPC UA session handle
    Priority : BYTE;                  // Subscription priority (0-255)
    PublishingInterval : TIME;         // Subscription update interval
    MaxRetries : INT := 3;            // Maximum retry attempts for connection
    RetryInterval : TIME := T#1s;     // Retry interval
END_VAR

VAR_OUTPUT
    Done : BOOL;                      // TRUE when subscription is successful
    Busy : BOOL;                      // TRUE while operation is in progress
    Error : BOOL;                     // TRUE if an error occurs
    ErrorID : DWORD;                  // Error code
    SubscriptionHdl : DWORD;          // Output subscription handle
END_VAR

VAR
    // Internal state variables
    State : INT := 0;                 // 0=Idle, 1=Connecting, 2=Subscribing, 3=Done, 4=Error
    LastExecute : BOOL;              // Previous state of Execute
    RetryCount : INT := 0;           // Retry counter
    SubscriptionCreated : BOOL;      // Internal flag for subscription creation
    SubscriptionHandle : DWORD;      // Internal subscription handle
    LastConnectionHdl : DWORD;       // Previous session handle
    LastPriority : BYTE;             // Previous priority
    LastPublishingInterval : TIME;   // Previous publishing interval
    LastMaxRetries : INT;            // Previous max retries
    LastRetryInterval : TIME;        // Previous retry interval
    LastErrorID : DWORD;             // Previous error code
    LastSubscriptionHdl : DWORD;     // Previous subscription handle
    LastDone : BOOL;                 // Previous Done flag
    LastBusy : BOOL;                 // Previous Busy flag
    LastError : BOOL;                // Previous Error flag
    LastState : INT;                 // Previous state
    LastRetryTimer : TON;            // Retry timer
    LastConnectionTimer : TON;
