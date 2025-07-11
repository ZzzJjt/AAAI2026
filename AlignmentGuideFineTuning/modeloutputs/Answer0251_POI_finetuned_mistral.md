### Intent:
**Intent Summary:**  
Create a cause-and-action matrix for chemical reactor interlocks that maps hazardous conditions (e.g., overpressure, sensor failures) to predefined safety responses (e.g., valve closure, alarms) to ensure systematic risk mitigation and operational safety.  

*(For code generation: Define a lookup table or logic rules linking reactor fault causes to actuator/safety actions.)*

### Prompt:
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**C-A-R-E:**

🟥 C (Context) – The Background

Chemical reactors operate under tightly controlled conditions, and failure to respond effectively to deviations—such as overpressure, underheating, or sensor faults—can lead to safety risks, equipment damage, or process shutdowns. Interlocks are used to mitigate these risks, but without a structured overview of how specific causes trigger safety responses, interlock logic can become difficult to manage or validate.

⸻

🟩 A (Action) – The Implementation Task

Develop an extended cause and process action matrix to document and analyze interlocks in a chemical reactor system. In this matrix:
	•	Rows represent potential hazardous causes (e.g., high pressure, low temperature, level sensor failure)
	•	Columns represent process actions or safety responses (e.g., isolate feed, shut down agitator, activate emergency vent)

Populate the matrix with checkmarks or symbols that show which actions are triggered by which causes. This visual mapping clarifies how interlocks are implemented across the system.

Also, discuss how this matrix supports the engineering process by improving clarity, traceability, and safety assurance in interlock design.

⸻

🟨 R (Result) – The Expected Outcome

The matrix offers a clear and centralized reference that links specific failure conditions to the corresponding safety actions. It enables systematic validation of interlocks, reduces the risk of missing responses to critical events, and enhances cross-functional communication between process engineers, safety experts, and automation teams.

⸻

🟦 E (Example) – A Practical Use Case

For instance, if the reactor pressure exceeds the upper safety limit, the matrix might show that the system will:
	•	Close the feed valve
	•	Activate the relief valve
	•	Stop the heating system

Each of these actions would be marked in the row corresponding to “High Pressure.” If a sensor fault is detected, the matrix might indicate triggering a safe shutdown sequence. This structured representation ensures that no critical scenario goes unaddressed.

### Generated Code:
**Intent Summary:**  
Create a cause-and-action matrix for chemical reactor interlocks that maps hazardous conditions (e.g., overpressure, sensor failures) to predefined safety responses (e.g., valve closure, alarms) to ensure systematic risk mitigation and operational safety.  

*(For code generation: Define a lookup table or logic rules linking reactor fault causes to actuator/safety actions.)*
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**C-A-R-E:**

🟥 C (Context) – The Background

Chemical reactors operate under tightly controlled conditions, and failure to respond effectively to deviations—such as overpressure, underheating, or sensor faults—can lead to safety risks, equipment damage, or process shutdowns. Interlocks are used to mitigate these risks, but without a structured overview of how specific causes trigger safety responses, interlock logic can become difficult to manage or validate.

⸻

🟩 A (Action) – The Implementation Task

Develop an extended cause and process action matrix to document and analyze interlocks in a chemical reactor system. In this matrix:
	•	Rows represent potential hazardous causes (e.g., high pressure, low temperature, level sensor failure)
	•	Columns represent process actions or safety responses (e.g., isolate feed, shut down agitator, activate emergency vent)

Populate the matrix with checkmarks or symbols that show which actions are triggered by which causes. This visual mapping clarifies how interlocks are implemented across the system.

Also, discuss how this matrix supports the engineering process by improving clarity, traceability, and safety assurance in interlock design.

⸻

🟨 R (Result) – The Expected Outcome

The matrix offers a clear and centralized reference that links specific failure conditions to the corresponding safety actions. It enables systematic validation of interlocks, reduces the risk of missing responses to critical events, and enhances cross-functional communication between process engineers, safety experts, and automation teams.

⸻

🟦 E (Example) – A Practical Use Case

For instance, if the reactor pressure exceeds the upper safety limit, the matrix might show that the system will:
	•	Close the feed valve
	•	Activate the relief valve
	•	Stop the heating system

Each of these actions would be marked in the row corresponding to “High Pressure.” If a sensor fault is detected, the matrix might indicate triggering a safe shutdown sequence. This structured representation ensures that no critical scenario goes unaddressed.
FUNCTION_BLOCK FB_ReactorInterlocks
VAR_INPUT
    Execute : BOOL; // Trigger interlock evaluation on rising edge
    PressureSensor : REAL; // Reactor pressure (bar)
    TemperatureSensor : REAL; // Reactor temperature (°C)
    LevelSensor : REAL; // Reactor level (%)
    LevelHighAlarm : BOOL; // High level alarm (%)
    LevelLowAlarm : BOOL; // Low level alarm (%)
    SensorFault : BOOL; // Sensor fault flag
    EmergencyStop : BOOL; // Manual emergency stop
    ShutdownCommand : BOOL; // Shutdown command from PLC
END_VAR

VAR_OUTPUT
    InterlockActive : BOOL; // Flag indicating interlock activation
    Shutdown : BOOL; // Shutdown output to PLC
    Alarm : BOOL; // Alarm output to PLC
    EmergencyStop : BOOL; // Emergency stop output to PLC
    Log : STRING[80]; // Log message for interlock events
END_VAR

VAR
    // Cause-and-action matrix
    CauseMatrix : ARRAY[1..5, 1..4] OF BOOL; // 0 = inactive, 1 = active
    // Cause definitions
    Causes : ARRAY[1..5] OF STRING[20] :=
    ['PressureHigh', 'PressureLow', 'TemperatureHigh', 'TemperatureLow', 'LevelHigh', 'LevelLow', 'SensorFault', 'EmergencyStop', 'ShutdownCommand'];
    // Action definitions
    Actions : ARRAY[1..4] OF STRING[20] :=
    ['IsolateFeed', 'ShutDownAgitator', 'ActivateReliefValve', 'StopHeating'];
    // Interlock thresholds
    PressureHighLimit : REAL := 15.0; // bar
    PressureLowLimit : REAL := 5.0; // bar
    TemperatureHighLimit : REAL := 120.0; // °C
    TemperatureLowLimit : REAL := 80.0; // °C
    LevelHighLimit : RE
