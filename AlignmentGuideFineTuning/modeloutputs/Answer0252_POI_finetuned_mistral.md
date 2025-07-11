### Intent:
**Intent Summary:**  
Create a cause-and-effect matrix for chemical reactor interlocks, mapping sensor deviations (e.g., high pressure) to safety actions (e.g., valve closure, alarms), ensuring automated hazard mitigation and operational safety.  

*(For code generation: Define logic to trigger actuator responses based on sensor thresholds in a reactor control system.)*

### Prompt:
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**C-A-R-E:**

🟥 C (Context) – The Background

Chemical reactors operate under precise conditions, and deviations in parameters like pressure, temperature, or level can lead to dangerous situations. Interlocks serve as automated safety mechanisms that respond to such deviations. However, without a structured overview, it’s difficult to ensure that all abnormal situations are covered and appropriately mitigated.

⸻

🟩 A (Action) – The Implementation Task

Develop a cause and effect matrix specifically for the interlocks in a chemical reactor system. In this matrix:
	•	Each row represents a cause, such as a sensor value exceeding a safety threshold (e.g., high pressure, low level, high temperature).
	•	Each column represents an effect, such as triggering an alarm, closing a feed valve, stopping a circulation pump, or isolating the reactor.
	•	Fill in the matrix to clearly indicate which actions are triggered by which sensor-based events.

After creating the matrix, write a detailed explanation of how the mapped interlocks contribute to safe reactor operation and how each action helps mitigate specific process risks.

⸻

🟨 R (Result) – The Expected Outcome

The result is a clear and actionable interlock overview that helps operators, control engineers, and safety personnel understand exactly how the system responds to abnormal conditions. The matrix ensures all failure modes are covered, reduces ambiguity in alarm and actuator responses, and serves as a key reference for both system validation and regulatory compliance.

⸻

🟦 E (Example) – A Practical Use Case

For instance, if the reactor pressure exceeds its upper limit, the matrix would show effects such as:
	•	Closing the feed valve
	•	Stopping the feed pump
	•	Activating a relief system
	•	Issuing a high-pressure alarm

This mapping ensures that the overpressure condition is promptly detected and addressed through multiple layers of response, maintaining safe reactor conditions and preventing escalation.

### Generated Code:
**Intent Summary:**  
Create a cause-and-effect matrix for chemical reactor interlocks, mapping sensor deviations (e.g., high pressure) to safety actions (e.g., valve closure, alarms), ensuring automated hazard mitigation and operational safety.  

*(For code generation: Define logic to trigger actuator responses based on sensor thresholds in a reactor control system.)*
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**C-A-R-E:**

🟥 C (Context) – The Background

Chemical reactors operate under precise conditions, and deviations in parameters like pressure, temperature, or level can lead to dangerous situations. Interlocks serve as automated safety mechanisms that respond to such deviations. However, without a structured overview, it’s difficult to ensure that all abnormal situations are covered and appropriately mitigated.

⸻

🟩 A (Action) – The Implementation Task

Develop a cause and effect matrix specifically for the interlocks in a chemical reactor system. In this matrix:
	•	Each row represents a cause, such as a sensor value exceeding a safety threshold (e.g., high pressure, low level, high temperature).
	•	Each column represents an effect, such as triggering an alarm, closing a feed valve, stopping a circulation pump, or isolating the reactor.
	•	Fill in the matrix to clearly indicate which actions are triggered by which sensor-based events.

After creating the matrix, write a detailed explanation of how the mapped interlocks contribute to safe reactor operation and how each action helps mitigate specific process risks.

⸻

🟨 R (Result) – The Expected Outcome

The result is a clear and actionable interlock overview that helps operators, control engineers, and safety personnel understand exactly how the system responds to abnormal conditions. The matrix ensures all failure modes are covered, reduces ambiguity in alarm and actuator responses, and serves as a key reference for both system validation and regulatory compliance.

⸻

🟦 E (Example) – A Practical Use Case

For instance, if the reactor pressure exceeds its upper limit, the matrix would show effects such as:
	•	Closing the feed valve
	•	Stopping the feed pump
	•	Activating a relief system
	•	Issuing a high-pressure alarm

This mapping ensures that the overpressure condition is promptly detected and addressed through multiple layers of response, maintaining safe reactor conditions and preventing escalation.
FUNCTION_BLOCK FB_ReactorInterlocks
VAR_INPUT
    PT_101 : REAL; // Pressure sensor reading (bar)
    TT_101 : REAL; // Temperature sensor reading (°C)
    LT_101 : REAL; // Level sensor reading (m)
    LT_102 : REAL; // Level sensor reading (m)
    LT_103 : REAL; // Level sensor reading (m)
    LT_104 : REAL; // Level sensor reading (m)
    LT_105 : REAL; // Level sensor reading (m)
    LT_106 : REAL; // Level sensor reading (m)
    LT_107 : REAL; // Level sensor reading (m)
    LT_108 : REAL; // Level sensor reading (m)
    LT_109 : REAL; // Level sensor reading (m)
    LT_110 : REAL; // Level sensor reading (m)
    LT_111 : REAL; // Level sensor reading (m)
    LT_112 : REAL; // Level sensor reading (m)
    LT_113 : REAL; // Level sensor reading (m)
    LT_114 : REAL; // Level sensor reading (m)
    LT_115 : REAL; // Level sensor reading (m)
    LT_116 : REAL; // Level sensor reading (m)
    LT_117 : REAL; // Level sensor reading (m)
    LT_118 : REAL; // Level sensor reading (m)
    LT_119 : REAL; // Level sensor reading (m)
    LT_120 : REAL; // Level sensor reading (m)
    LT_121 : REAL; // Level sensor reading (m)
    LT_122 : REAL; // Level sensor reading (m)
    LT_123 : REAL; // Level sensor reading (m)
    LT_124 : REAL; // Level sensor reading (m
