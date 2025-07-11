### Intent:
**Intent Summary:**  
Develop a reusable IEC 61131-3 Structured Text function block that wraps a C-based OPC UA subscription manager (using Open62541) to dynamically create and manage subscriptions with configurable intervals, priority, and timeout, while providing real-time status and error feedback for PLC integration.

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
Develop a reusable IEC 61131-3 Structured Text function block that wraps a C-based OPC UA subscription manager (using Open62541) to dynamically create and manage subscriptions with configurable intervals, priority, and timeout, while providing real-time status and error feedback for PLC integration.
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

⸻

🟨 E (Example) – How to Use It

```
DEFINE FUNCTION Block "SubscriptionManager"
	INPUT Execute (BOOL),
		ConnectionHdl (DWORD),
		Priority (BYTE),
		Timeout (TIME),
		PublishingInterval (IN/OUT, TIME)
	OUTPUT Done (BOOL),
		Busy (BOOL),
		Error (BOOL),
		ErrorID (DWORD),
		SubscriptionHdl (DWORD)
END FUNCTION Block

DEFINE FUNCTION Block "SubscriptionManager"
	IF Execute THEN
		IF PublishingInterval.Value = 0 THEN
			PublishingInterval.Value := TIME.DEFAULT
		ENDIF
		IF ConnectionHdl.Value = 0 THEN
			Error := TRUE
			ErrorID := ERROR_INVALID_HANDLE
			RETURN
		ENDIF
		IF Priority.Value = 0 THEN
			Error := TRUE
			ErrorID := ERROR_INVALID_PRIORITY
			RETURN
		ENDIF
		IF Timeout.Value = 0 THEN
			Timeout.Value := TIME.DEFAULT
		ENDIF
		IF PublishingInterval.Value = 0 THEN
			PublishingInterval.Value := TIME.DEFAULT
		ENDIF
		IF Timeout.Value > PublishingInterval.Value THEN
			Error := TRUE
			ErrorID := ERROR_INVALID_TIMEOUT
			RETURN
		ENDIF
		SubscriptionHdl := open62541::createSubscription(ConnectionHdl.Value, Timeout.Value, PublishingInterval.Value)
		IF SubscriptionHdl.Value = 0 THEN
			Error := TRUE
			ErrorID := ERROR_SUBSCRIPTION_CREATION_FAILED
			RETURN
		ENDIF
		Done := TRUE
	ENDIF
	RETURN SubscriptionHdl
END FUNCTION Block
```

In this example, the SubscriptionManager function block is defined with inputs for Execute, ConnectionHdl, Priority, Timeout, and PublishingInterval. The function block returns Done, Busy, Error, ErrorID, and SubscriptionHdl. The ST function block calls the C function to create the subscription, and the C function returns the SubscriptionHdl.

⸻

🟩 A (Action
