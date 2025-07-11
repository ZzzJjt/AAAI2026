### Intent:
**Intent Summary:**  
Develop a cause-and-effect matrix for chemical reactor interlocks, mapping sensor-triggered abnormal conditions (e.g., high pressure) to actuator responses (e.g., valve closure), and generate explanatory documentation to validate safety logic and compliance.  

*(For code generation: Focus on translating the matrix into PLC logic (e.g., IF-THEN rules) and alarm/actuator control logic.)*

### Prompt:
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**B-A-B:**

🟥 B (Before) – The Challenge

In chemical reactor systems, safety depends on timely and accurate responses to abnormal conditions such as overpressure, overheating, or high liquid levels. Without a structured representation of interlock logic, it becomes difficult to validate how each sensor-triggered event leads to a protective action. This increases the risk of unhandled faults, operational downtime, or equipment damage.

⸻

🟩 A (After) – The Ideal Outcome

Develop a cause and effect matrix for the interlock logic of a chemical reactor. Each row in the matrix represents a specific cause—typically an abnormal sensor value like high pressure, low level, or high temperature. Each column represents an effect—an actuator-based response such as closing a feed valve, stopping a recirculation pump, or triggering a high-priority alarm.

Once the matrix is built, accompany it with a detailed explanation of how each interlock action contributes to process safety. Clarify how the design prevents hazardous outcomes, maintains stable operation, and protects both personnel and equipment during process upsets.

⸻

🟧 B (Bridge) – The Implementation Strategy

Start by identifying all critical failure scenarios based on sensor readings. Define the corresponding protective actions using actuators and alarms. Construct the matrix by linking each cause to its necessary effects. Use this structured mapping to:

	•	Verify full safety coverage for every major process hazard
	•	Identify overlapping or redundant interlocks for optimization
	•	Support compliance with safety standards and facilitate HAZOP reviews
	•	Communicate interlock logic clearly across engineering, operations, and safety teams

The final matrix will serve as a foundational tool for both system design and ongoing risk management in reactor control.

### Generated Code:
**Intent Summary:**  
Develop a cause-and-effect matrix for chemical reactor interlocks, mapping sensor-triggered abnormal conditions (e.g., high pressure) to actuator responses (e.g., valve closure), and generate explanatory documentation to validate safety logic and compliance.  

*(For code generation: Focus on translating the matrix into PLC logic (e.g., IF-THEN rules) and alarm/actuator control logic.)*
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**B-A-B:**

🟥 B (Before) – The Challenge

In chemical reactor systems, safety depends on timely and accurate responses to abnormal conditions such as overpressure, overheating, or high liquid levels. Without a structured representation of interlock logic, it becomes difficult to validate how each sensor-triggered event leads to a protective action. This increases the risk of unhandled faults, operational downtime, or equipment damage.

⸻

🟩 A (After) – The Ideal Outcome

Develop a cause and effect matrix for the interlock logic of a chemical reactor. Each row in the matrix represents a specific cause—typically an abnormal sensor value like high pressure, low level, or high temperature. Each column represents an effect—an actuator-based response such as closing a feed valve, stopping a recirculation pump, or triggering a high-priority alarm.

Once the matrix is built, accompany it with a detailed explanation of how each interlock action contributes to process safety. Clarify how the design prevents hazardous outcomes, maintains stable operation, and protects both personnel and equipment during process upsets.

⸻

🟧 B (Bridge) – The Implementation Strategy

Start by identifying all critical failure scenarios based on sensor readings. Define the corresponding protective actions using actuators and alarms. Construct the matrix by linking each cause to its necessary effects. Use this structured mapping to:

	•	Verify full safety coverage for every major process hazard
	•	Identify overlapping or redundant interlocks for optimization
	•	Support compliance with safety standards and facilitate HAZOP reviews
	•	Communicate interlock logic clearly across engineering, operations, and safety teams

The final matrix will serve as a foundational tool for both system design and ongoing risk management in reactor control.
FUNCTION_BLOCK FB_ReactorInterlocks
VAR_INPUT
    Execute : BOOL; // Trigger interlock evaluation on rising edge
    PressureSensor : REAL; // Reactor pressure (bar)
    TemperatureSensor : REAL; // Reactor temperature (°C)
    LevelSensor : REAL; // Reactor level (%)
    EmergencyStop : BOOL; // Manual emergency stop
END_VAR

VAR_OUTPUT
    FeedValveClosed : BOOL; // Feed valve closed
    RecirculationPumpStopped : BOOL; // Recirculation pump stopped
    AlarmActive : BOOL; // High-priority alarm active
    Shutdown : BOOL; // Reactor shutdown initiated
END_VAR

VAR
    // Interlock logic matrix
    PressureHigh : BOOL;
    TemperatureHigh : BOOL;
    LevelHigh : BOOL;
    EmergencyStopActive : BOOL;

    // Interlock actions
    FeedValveClosed_TempHigh : BOOL;
    RecirculationPumpStopped_LevelHigh : BOOL;
    AlarmActive_PressureHigh : BOOL;
    Shutdown_EmergencyStop : BOOL;

    // State variables
    PrevExecute : BOOL;
END_VAR

// Reset outputs on rising edge of Execute
IF Execute THEN
    FeedValveClosed := FALSE;
    RecirculationPumpStopped := FALSE;
    AlarmActive := FALSE;
    Shutdown := FALSE;
END_IF

// Store previous state of Execute for rising edge detection
PrevExecute := Execute;

// Evaluate interlocks based on sensor inputs and emergency stop
PressureHigh := PressureSensor > 15.0; // Set threshold (e.g., 15 bar)
TemperatureHigh := TemperatureSensor > 120.0; // Set threshold (e.g., 120°C)
LevelHigh := LevelSensor > 95.0; // Set threshold (e.g., 95%)
EmergencyStopActive := EmergencyStop;

// Apply interlock logic using matrix
FeedValveCl
