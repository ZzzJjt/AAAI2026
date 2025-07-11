### Intent:
**Intent Summary:**  
Develop a cause-and-effect matrix linking hazardous process conditions (e.g., overpressure, sensor failures) to safety actions (e.g., valve closure, alarms) in a chemical reactor, ensuring automated risk mitigation and operational safety.  

*(For code generation: Map process deviations to predefined actuator responses in a safety interlock system.)*

### Prompt:
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a cause and effect matrix for the interlock system of a chemical reactor.

⸻

🟩 A (Action) – How to Do It

Create a matrix where:

	•	Each row represents a specific cause, such as abnormal sensor readings (e.g., high pressure, low level, or high temperature).
	•	Each column represents a specific effect, such as triggering an alarm, stopping a pump, closing a valve, or shutting down a heater.

Populate the matrix to show how each hazardous condition leads to one or more predefined safety actions. After the matrix is completed, write a detailed explanation discussing how each interlock response helps mitigate risk, protect equipment, and maintain reactor stability. Highlight the importance of using this matrix as a clear, traceable tool in safety system design.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a structured, visual tool that links potential process hazards with protective actions. This matrix will enhance operational safety, simplify interlock validation, and serve as a vital reference for engineers, operators, and auditors responsible for the safe functioning of the chemical reactor.

### Generated Code:
**Intent Summary:**  
Develop a cause-and-effect matrix linking hazardous process conditions (e.g., overpressure, sensor failures) to safety actions (e.g., valve closure, alarms) in a chemical reactor, ensuring automated risk mitigation and operational safety.  

*(For code generation: Map process deviations to predefined actuator responses in a safety interlock system.)*
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a cause and effect matrix for the interlock system of a chemical reactor.

⸻

🟩 A (Action) – How to Do It

Create a matrix where:

	•	Each row represents a specific cause, such as abnormal sensor readings (e.g., high pressure, low level, or high temperature).
	•	Each column represents a specific effect, such as triggering an alarm, stopping a pump, closing a valve, or shutting down a heater.

Populate the matrix to show how each hazardous condition leads to one or more predefined safety actions. After the matrix is completed, write a detailed explanation discussing how each interlock response helps mitigate risk, protect equipment, and maintain reactor stability. Highlight the importance of using this matrix as a clear, traceable tool in safety system design.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a structured, visual tool that links potential process hazards with protective actions. This matrix will enhance operational safety, simplify interlock validation, and serve as a vital reference for engineers, operators, and auditors responsible for the safe functioning of the chemical reactor.
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

// Define the interlock matrix
map<string, map<string, string>> interlock_matrix;

// Define the interlock actions
map<string, string> interlock_actions = {
    {"pressure_high", "close_valve_1"},
    {"pressure_low", "open_valve_2"},
    {"temperature_high", "stop_heater"},
    {"temperature_low", "start_heater"},
    {"level_high", "stop_pump_1"},
    {"level_low", "start_pump_1"},
    {"flow_high", "stop_pump_2"},
    {"flow_low", "start_pump_2"},
    {"pressure_sensor_fault", "trigger_alarm"},
    {"temperature_sensor_fault", "trigger_alarm"},
    {"level_sensor_fault", "trigger_alarm"},
    {"flow_sensor_fault", "trigger_alarm"}
};

// Define the interlock conditions
map<string, string> interlock_conditions = {
    {"pressure_high", "valve_1_closed"},
    {"pressure_low", "valve_2_open"},
    {"temperature_high", "heater_on"},
    {"temperature_low", "heater_off"},
    {"level_high", "pump_1_stopped"},
    {"level_low", "pump_1_started"},
    {"flow_high", "pump_2_stopped"},
    {"flow_low", "pump_2_started"},
    {"pressure_sensor_fault", "alarm_triggered"},
    {"temperature_sensor_fault", "alarm_triggered"},
    {"level_sensor_fault", "alarm_triggered"},
    {"flow_sensor_fault", "alarm_triggered"}
};

// Check if a condition is met
bool check_condition(const string& condition) {
    return interlock_conditions.count(condition) > 0;
}

// Check if an action is triggered
bool check_action(const string& action) {
    return interlock_actions.count(action) > 0;
