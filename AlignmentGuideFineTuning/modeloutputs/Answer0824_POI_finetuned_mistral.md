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
FUNCTION_BLOCK OPCUA_SUBSCRIBE
VAR_INPUT
    Execute : BOOL;                   // Trigger execution on rising edge
    ConnectionHandle : DWORD;         // OPC UA session handle
    SubscriptionId : DWORD;           // Subscription identifier
    Priority : INT;                   // Subscription priority (0-100)
    Timeout : TIME;                   // Subscription timeout (e.g., 100 ms)
    MaxNotifications : INT;           // Maximum notifications per second
    MaxRetainedValues : INT;          // Maximum retained values
    MaxBufferSize : INT;              // Maximum buffer size (bytes)
    MaxKeepAliveInterval : TIME;      // Maximum keep-alive interval
    MaxNotificationLatency : TIME;    // Maximum notification latency
    MaxRetainedLatency : TIME;        // Maximum retained latency
    MaxDiscardedLatency : TIME;       // Maximum discarded latency
    MaxDiscardedRetained : INT;       // Maximum discarded retained values
    MaxDiscardedNotifications : INT;  // Maximum discarded notifications
    MaxBufferRetention : TIME;        // Maximum buffer retention
    MaxBufferDiscardInterval : TIME;  // Maximum buffer discard interval
    MaxBufferDiscardCount : INT;      // Maximum buffer discard count
    MaxBufferDiscardThreshold : INT;  // Maximum buffer discard threshold
    MaxBufferDiscardTimeout : TIME;   // Maximum buffer discard timeout
    MaxBufferDiscardError : INT;      // Maximum buffer discard error
    MaxBufferDiscardWarning : INT;    // Maximum buffer discard warning
    MaxBufferDiscardCritical : INT;   // Maximum buffer discard critical
    MaxBufferDiscardFatal : INT;      // Maximum buffer discard fatal
    MaxBufferDiscardReset : INT;      // Maximum buffer discard reset
    MaxBufferDiscardShutdown : INT;   // Maximum buffer discard shutdown
    MaxBufferDiscardRestart : INT;    // Maximum buffer discard restart
    MaxBufferDiscardRecovery : INT;   // Maximum buffer discard recovery
    MaxBufferDiscardSystem :
