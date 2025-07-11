### Intent:
**Intent Summary:**  
Develop an extended cause-and-action matrix for a chemical reactor's interlock system, mapping hazardous conditions (e.g., overpressure, sensor faults) to safety actions (e.g., valve closure, emergency cooling) to ensure comprehensive risk mitigation and generate PLC logic for implementation.

### Prompt:
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**B-A-B:**


🟥 B (Before) – The Challenge

In complex chemical processes, safety and reliability depend on effective interlock systems. However, without a structured and visual representation of how specific causes trigger process actions, it becomes difficult to ensure comprehensive coverage of hazardous conditions. This can lead to gaps in protection against critical risks such as overpressure, overheating, or equipment failure.

⸻

🟩 A (After) – The Ideal Outcome

Develop an extended cause and process action matrix tailored to a chemical reactor’s interlocks. Each row in the matrix represents a specific cause, such as a pressure sensor exceeding its upper limit or a temperature falling below a minimum threshold. Each column represents a process safety action, such as closing a feed valve, venting the reactor, or activating emergency cooling.

The matrix clearly maps each hazardous condition to one or more corresponding safety actions. This structure helps engineers visualize the logic behind interlocks, ensure full process coverage, and quickly assess how the system will respond to various failure scenarios.

⸻

🟧 B (Bridge) – The Implementation Strategy

Start by identifying all relevant causes related to reactor operation—such as high/low pressure, high/low temperature, level sensor faults, or flow anomalies. Then, list all available actuator-based safety actions. Populate the matrix by marking which actions should be triggered by each cause.

Once completed, analyze the matrix to:
	•	Validate that each hazardous scenario has at least one safety response
	•	Check for redundancies and opportunities to optimize interlock logic
	•	Ensure responses are appropriate for protecting the reactor, environment, and personnel

This matrix serves as both a design tool and a communication aid for operators, safety engineers, and process control teams.

### Generated Code:
**Intent Summary:**  
Develop an extended cause-and-action matrix for a chemical reactor's interlock system, mapping hazardous conditions (e.g., overpressure, sensor faults) to safety actions (e.g., valve closure, emergency cooling) to ensure comprehensive risk mitigation and generate PLC logic for implementation.
**Extended Cause & Process Action Matrix:**

Develop an extended cause and process action matrix for the interlocks in a chemical reactor. Each row should represent a specific cause (e.g., sensor values exceeding limits), and the column headings should represent safety actions performed using actuators in the system. The matrix should illustrate how different causes trigger specific actions to ensure safe operation.

Discuss how this extended matrix provides a clear mapping between potential hazardous situations and the corresponding safety actions. Emphasize the importance of designing interlocks that ensure safe and stable reactor operation, preventing risks such as overpressure, underheating, and process failures.

**B-A-B:**


🟥 B (Before) – The Challenge

In complex chemical processes, safety and reliability depend on effective interlock systems. However, without a structured and visual representation of how specific causes trigger process actions, it becomes difficult to ensure comprehensive coverage of hazardous conditions. This can lead to gaps in protection against critical risks such as overpressure, overheating, or equipment failure.

⸻

🟩 A (After) – The Ideal Outcome

Develop an extended cause and process action matrix tailored to a chemical reactor’s interlocks. Each row in the matrix represents a specific cause, such as a pressure sensor exceeding its upper limit or a temperature falling below a minimum threshold. Each column represents a process safety action, such as closing a feed valve, venting the reactor, or activating emergency cooling.

The matrix clearly maps each hazardous condition to one or more corresponding safety actions. This structure helps engineers visualize the logic behind interlocks, ensure full process coverage, and quickly assess how the system will respond to various failure scenarios.

⸻

🟧 B (Bridge) – The Implementation Strategy

Start by identifying all relevant causes related to reactor operation—such as high/low pressure, high/low temperature, level sensor faults, or flow anomalies. Then, list all available actuator-based safety actions. Populate the matrix by marking which actions should be triggered by each cause.

Once completed, analyze the matrix to:
	•	Validate that each hazardous scenario has at least one safety response
	•	Check for redundancies and opportunities to optimize interlock logic
	•	Ensure responses are appropriate for protecting the reactor, environment, and personnel

This matrix serves as both a design tool and a communication aid for operators, safety engineers, and process control teams. It helps build a robust, fault-tolerant interlock system that ensures safe and stable reactor operation.
FUNCTION_BLOCK FB_ReactorInterlock
VAR_INPUT
    Execute : BOOL; // Trigger interlock evaluation on rising edge
    PressureSensor : REAL; // Reactor pressure (bar)
    TemperatureSensor : REAL; // Reactor temperature (°C)
    LevelSensor : REAL; // Reactor level (%)
    FlowRateSensor : REAL; // Feed flow rate (L/min)
    SensorFault : BOOL; // Sensor fault flag
    EmergencyStop : BOOL; // Manual emergency stop
    ShutdownRequest : BOOL; // Shutdown request from HMI
    Reset : BOOL; // Reset interlock state
END_VAR

VAR_OUTPUT
    FeedValveClosed : BOOL; // Feed valve closed
    CoolingValveClosed : BOOL; // Cooling valve closed
    VentValveOpen : BOOL; // Vent valve open
    EmergencyStopActive : BOOL; // Emergency stop active
    Shutdown : BOOL; // Reactor in shutdown state
    Alarm : BOOL; // Alarm raised
    Error : BOOL; // Error flag
    ErrorID : DWORD; // Error code
END_VAR

VAR
    // Interlock states
    PressureHigh : BOOL;
    PressureLow : BOOL;
    TemperatureHigh : BOOL;
    TemperatureLow : BOOL;
    LevelHigh : BOOL;
    LevelLow : BOOL;
    FlowRateHigh : BOOL;
    FlowRateLow : BOOL;
    SensorFaultDetected : BOOL;
    EmergencyStopActive_Internal : BOOL;
    ShutdownRequest_Internal : BOOL;
    Reset_Internal : BOOL;

    // Interlock logic
    PressureHigh_Threshold : REAL := 15.0; // bar
    PressureLow_Threshold : REAL := 5.0; // bar
    TemperatureHigh_Threshold : REAL := 150.0; // °C
    TemperatureLow_Threshold : REAL := 8
