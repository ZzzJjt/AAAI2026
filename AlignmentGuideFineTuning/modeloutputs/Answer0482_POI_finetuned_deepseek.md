### Intent:
**Intent Summary:**  
Design a safety interlock system for a subsea wellhead that monitors pressure, temperature, and flow, triggers shutdown actions (e.g., closing the master valve) during hazardous conditions (high pressure, low flow, high temperature), logs events, and allows manual reset only when safe.  

*(Focus: Safety logic, sensor validation, fail-safe actions, and audit trails for compliance.)*

### Prompt:
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a process safety or control systems engineer designing interlock logic for a chemical reactor to ensure safe and reliable operation during abnormal process conditions.

⸻

🟩 I (Input) – What You’re Given

You need to develop a cause and effect matrix where:

	•	Each row represents a specific cause, such as abnormal sensor readings (e.g., high pressure, low level, high temperature).
	•	Each column represents an effect, such as shutting valves, stopping pumps, or triggering alarms.
 
The matrix must link causes to protective actions that are executed through actuators or control logic.

You are also required to explain how the matrix contributes to overall system safety and equipment protection.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify critical causes: List process deviations and sensor-based alarms that require protective action (e.g., “Reactor Pressure > High Limit”).
	2.	Define safety actions: List available interlock responses (e.g., close feed valve, isolate cooling, trigger alarm).
	3.	Create the matrix: Mark where each cause triggers one or more specific actions in the corresponding cells.
	4.	Write an explanation describing:
 
	•	How the matrix logic works
	•	How it supports rapid response to unsafe conditions
	•	How each action mitigates specific risks
	•	The importance of completeness and clarity in interlock design

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a well-structured interlock matrix that gives a clear overview of how the chemical reactor will respond to unsafe operating conditions. The matrix will ensure comprehensive safety coverage, reduce ambiguity, and serve as a key tool in both operational decision-making and safety compliance efforts.

### Generated Code:
**Intent Summary:**  
Design a safety interlock system for a subsea wellhead that monitors pressure, temperature, and flow, triggers shutdown actions (e.g., closing the master valve) during hazardous conditions (high pressure, low flow, high temperature), logs events, and allows manual reset only when safe.  

*(Focus: Safety logic, sensor validation, fail-safe actions, and audit trails for compliance.)*
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**R-I-S-E:**

🟥 R (Role) – Your Role

Act as a process safety or control systems engineer designing interlock logic for a chemical reactor to ensure safe and reliable operation during abnormal process conditions.

⸻

🟩 I (Input) – What You’re Given

You need to develop a cause and effect matrix where:

	•	Each row represents a specific cause, such as abnormal sensor readings (e.g., high pressure, low level, high temperature).
	•	Each column represents an effect, such as shutting valves, stopping pumps, or triggering alarms.
 
The matrix must link causes to protective actions that are executed through actuators or control logic.

You are also required to explain how the matrix contributes to overall system safety and equipment protection.

⸻

🟧 S (Steps) – What You Need to Do
	1.	Identify critical causes: List process deviations and sensor-based alarms that require protective action (e.g., “Reactor Pressure > High Limit”).
	2.	Define safety actions: List available interlock responses (e.g., close feed valve, isolate cooling, trigger alarm).
	3.	Create the matrix: Mark where each cause triggers one or more specific actions in the corresponding cells.
	4.	Write an explanation describing:
 
	•	How the matrix logic works
	•	How it supports rapid response to unsafe conditions
	•	How each action mitigates specific risks
	•	The importance of completeness and clarity in interlock design

⸻

🟦 E (Expectation) – What Success Looks Like

You produce a well-structured interlock matrix that gives a clear overview of how the chemical reactor will respond to unsafe operating conditions. The matrix will ensure comprehensive safety coverage, reduce ambiguity, and serve as a key tool in both operational decision-making and safety compliance efforts.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_NUM_OF_EVENTS 100
#define MAX_NUM_OF_EVENTS_LOG 1000

// Event types
enum EventType {
    HIGH_PRESSURE,
    LOW_FLOW,
    HIGH_TEMPERATURE,
    MANUAL_RESET,
    MAX_NUM_OF_EVENTS
};

// Event struct
typedef struct {
    enum EventType type;
    int pressure;
    int flow;
    int temperature;
    int timestamp;
} Event;

// Event log
Event events[MAX_NUM_OF_EVENTS_LOG];
int event_count = 0;

// Manual reset flag
bool manual_reset = false;

// Main function
void main() {
    // Initialize event log
    for (int i = 0; i < MAX_NUM_OF_EVENTS_LOG; i++) {
        events[i].type = 0;
        events[i].pressure = 0;
        events[i].flow = 0;
        events[i].temperature = 0;
        events[i].timestamp = 0;
    }

    // Example event
    events[event_count].type = HIGH_PRESSURE;
    events[event_count].pressure = 150000;
    events[event_count].flow = 0;
    events[event_count].temperature = 0;
    events[event_count].timestamp = 1625000000;
    event_count++;

    // Manual reset
    if (manual_reset) {
        manual_reset = false;
        event_count = 0;
    }
}

// Manual reset function
void manualReset() {
    manual_reset = true;
}

// Get current event count
int getEventCount() {
    return event_count;
}

// Get current event by index
Event getEvent(int index) {
    if (index < 0 || index >= event_count) {
        return {0, 0,
