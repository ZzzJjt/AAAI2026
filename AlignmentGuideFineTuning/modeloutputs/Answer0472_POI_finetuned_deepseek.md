### Intent:
**Intent Summary:**  
Design a turbine safety interlock system that triggers protective actions (e.g., shutdowns, valve closures, alarms) based on real-time sensor inputs (temperature, pressure, speed, etc.) to prevent equipment damage and hazardous conditions.  

*(Focus: Cause-effect logic for fail-safe responses to abnormal turbine operating conditions.)*

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
Design a turbine safety interlock system that triggers protective actions (e.g., shutdowns, valve closures, alarms) based on real-time sensor inputs (temperature, pressure, speed, etc.) to prevent equipment damage and hazardous conditions.  

*(Focus: Cause-effect logic for fail-safe responses to abnormal turbine operating conditions.)*
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
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <map>

using namespace std;

// Define the turbine's operating conditions
enum class TURBINE_STATE {
    IDLE,
    START_UP,
    OPERATIONAL,
    SHUTDOWN,
    EMERGENCY_SHUTDOWN
};

// Define the turbine's sensor inputs
enum class SENSOR_STATE {
    NORMAL,
    HIGH_TEMPERATURE,
    LOW_PRESSURE,
    HIGH_SPEED,
    LOW_LEVEL,
    HIGH_PRESSURE,
    HIGH_TEMPERATURE_AND_LOW_PRESSURE,
    HIGH_TEMPERATURE_AND_LOW_LEVEL,
    HIGH_TEMPERATURE_AND_HIGH_PRESSURE,
    HIGH_TEMPERATURE_AND_LOW_LEVEL_AND_HIGH_PRESSURE
};

// Define the turbine's actuator outputs
enum class ACTUATOR_STATE {
    CLOSED,
    OPEN,
    ALARM_TRIGGERED
};

// Define the turbine's interlock logic
enum class INTERLOCK_STATE {
    OK,
    WARNING,
    SHUTDOWN
};

// Define the turbine's interlock matrix
map<SENSOR_STATE, vector<ACTUATOR_STATE>> interlockMatrix;

// Initialize the interlock matrix
void initializeInterlockMatrix() {
    interlockMatrix[SENSOR_STATE::NORMAL] = {ACTUATOR_STATE::CLOSED, ACTUATOR_STATE::CLOSED, ACTUATOR_STATE::CLOSED};
    interlockMatrix[SENSOR_STATE::HIGH_TEMPERATURE] = {ACTUATOR_STATE::CLOSED, ACTUATOR_STATE::ALARM_TRIGGERED, ACTUATOR_STATE::CLOSED};
    interlockMatrix[SENSOR_STATE::LOW_PRESSURE] = {ACTUATOR_STATE::CLOSED, ACTUATOR_STATE::CLOSED, ACTUATOR_STATE::CLOSED};
    interlockMatrix[SENSOR_STATE::HIGH_SPEED] = {ACTUATOR
