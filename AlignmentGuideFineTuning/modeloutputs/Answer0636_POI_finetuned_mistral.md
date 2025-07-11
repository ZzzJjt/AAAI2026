### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant IEC 61131-3 Structured Text program to automate the batch production of polyethylene, covering raw material preparation through packaging, with modular function blocks for each phase, safety interlocks, and precise sequencing to ensure operational efficiency and scalability.

### Prompt:
**Batch Polyethylene:**

Develop a self-contained program in IEC 61131-3 Structured Text to implement batch control for a polyethylene production process. The program should cover the full production cycle, including the following steps: raw material preparation, polymerization, quenching, drying, pelletizing, quality control, and packaging and storage. Ensure that each step is clearly defined and appropriately sequenced with transitions, and provide detailed comments explaining the logic and control conditions for each phase. Discuss the challenges of integrating batch control into a PLC environment, including timing, resource allocation, and synchronization across multiple production units.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a batch process control engineer responsible for implementing full-cycle polyethylene production in IEC 61131-3 Structured Text, following ISA-88 standards.

🟩 I (Input) – Information Provided

You are developing a batch automation program for a polyethylene production process. The process includes the following stages:
	•	Raw material preparation
	•	Polymerization
	•	Quenching
	•	Drying
	•	Pelletizing
	•	Quality control
	•	Packaging and storage

Each phase must be clearly defined, sequenced, and transitioned appropriately using timers, control conditions, and modular logic. The system must also handle synchronization, resource allocation, and timing constraints in a PLC environment.

🟧 S (Steps) – Implementation Steps
	1.	Break the process down into ISA-88-compliant phases and operations, mapping each physical step to a structured procedural model.
	2.	Implement each phase in IEC 61131-3 Structured Text, using modular function blocks and reusable methods for operations such as dosing, heating, or agitation.
	3.	Use timers, interlocks, and sensor feedback to manage transitions between phases and ensure safe, reliable operation.
	4.	Add inline comments to explain logic, control parameters, and sequencing decisions.
	5.	Address batch control challenges such as timing precision, multi-unit synchronization, and resource arbitration within the logic.

🟦 E (Expectation) – Expected Outcome

Deliver a robust, modular Structured Text program that covers the entire polyethylene batch cycle, fully aligned with ISA-88. The program should ensure accurate execution of each phase, minimize downtime through precise sequencing, and support easy scaling or modification for more complex systems—all while maintaining operational safety and production consistency.

### Generated Code:
**Intent Summary:**  
Develop an ISA-88-compliant IEC 61131-3 Structured Text program to automate the batch production of polyethylene, covering raw material preparation through packaging, with modular function blocks for each phase, safety interlocks, and precise sequencing to ensure operational efficiency and scalability.
**Batch Polyethylene:**

Develop a self-contained program in IEC 61131-3 Structured Text to implement batch control for a polyethylene production process. The program should cover the full production cycle, including the following steps: raw material preparation, polymerization, quenching, drying, pelletizing, quality control, and packaging and storage. Ensure that each step is clearly defined and appropriately sequenced with transitions, and provide detailed comments explaining the logic and control conditions for each phase. Discuss the challenges of integrating batch control into a PLC environment, including timing, resource allocation, and synchronization across multiple production units.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a batch process control engineer responsible for implementing full-cycle polyethylene production in IEC 61131-3 Structured Text, following ISA-88 standards.

🟩 I (Input) – Information Provided

You are developing a batch automation program for a polyethylene production process. The process includes the following stages:
	•	Raw material preparation
	•	Polymerization
	•	Quenching
	•	Drying
	•	Pelletizing
	•	Quality control
	•	Packaging and storage

Each phase must be clearly defined, sequenced, and transitioned appropriately using timers, control conditions, and modular logic. The system must also handle synchronization, resource allocation, and timing constraints in a PLC environment.

🟧 S (Steps) – Implementation Steps
	1.	Break the process down into ISA-88-compliant phases and operations, mapping each physical step to a structured procedural model.
	2.	Implement each phase in IEC 61131-3 Structured Text, using modular function blocks and reusable methods for operations such as dosing, heating, or agitation.
	3.	Use timers, interlocks, and sensor feedback to manage transitions between phases and ensure safe, reliable operation.
	4.	Add inline comments to explain logic, control parameters, and sequencing decisions.
	5.	Address batch control challenges such as timing precision, multi-unit synchronization, and resource arbitration within the logic.

🟦 E (Expectation) – Expected Outcome

Deliver a robust, modular Structured Text program that covers the entire polyethylene batch cycle, fully aligned with ISA-88. The program should ensure accurate execution of each phase, minimize downtime through precise sequencing, and support easy scaling or modification for more complex systems—all while maintaining operational safety and production consistency.
FUNCTION_BLOCK FB_PneumaticValveControl
VAR_INPUT
    Execute : BOOL; // Trigger control cycle
    ValveState : INT := 0; // 0 = Closed, 1 = Open
    PressureSetpoint : REAL := 100.0; // Setpoint in bar
    PressureFeedback : REAL := 0.0; // Measured pressure in bar
    TemperatureSetpoint : REAL := 25.0; // Setpoint in °C
    TemperatureFeedback : REAL := 0.0; // Measured temperature in °C
    EmergencyStop : BOOL := FALSE; // Safety interlock
END_VAR

VAR_OUTPUT
    ValveOpen : BOOL := FALSE; // Output to control valve
    PressureControlSignal : BOOL := FALSE; // Signal to pressure control loop
    TemperatureControlSignal : BOOL := FALSE; // Signal to temperature control loop
    Error : BOOL := FALSE; // Error flag
    ErrorMessage : STRING(255) := ''; // Error message
END_VAR

VAR
    // Control parameters
    PressureControlPID : TON; // PID controller for pressure control
    TemperatureControlPID : TON; // PID controller for temperature control
    
    // Control states
    ControlState : INT := 0; // 0 = Idle, 1 = Pressure Control, 2 = Temperature Control
    PressureControlActive : BOOL := FALSE;
    TemperatureControlActive : BOOL := FALSE;
    
    // Control limits
    MinPressure : REAL := 80.0; // Minimum pressure in bar
    MaxPressure : REAL := 120.0; // Maximum pressure in bar
    MinTemperature : REAL := 20.0; // Minimum temperature in °C
    MaxTemperature : REAL := 30.0; // Maximum temperature in °C
END_VAR

// Reset outputs and error flags
ValveOpen := FALSE;
PressureControlSignal := FALSE;
TemperatureControlSignal := FALSE;
Error := FALSE;
ErrorMessage := '';

// Initialize PID controllers
