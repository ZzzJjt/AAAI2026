### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text to automate the full polyethylene production cycle (raw material preparation to packaging), ensuring modularity, phase sequencing, and synchronization while addressing PLC-specific challenges like timing and resource allocation.  

*(Focus: Batch automation, procedural control, PLC implementation, ISA-88 standards)*

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
Develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text to automate the full polyethylene production cycle (raw material preparation to packaging), ensuring modularity, phase sequencing, and synchronization while addressing PLC-specific challenges like timing and resource allocation.  

*(Focus: Batch automation, procedural control, PLC implementation, ISA-88 standards)*
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
FUNCTION_BLOCK FB_BatchControl
VAR_INPUT
    StartButton : BOOL; // Starts the batch process
    StopButton : BOOL;  // Stops the batch process
    EmergencyStop : BOOL; // Emergency stop signal
    BatchID : INT;       // Batch identifier
    BatchType : INT;     // Batch type (1: PE, 2: PP)
    BatchSize : INT;     // Batch size
    BatchWeight : REAL;  // Batch weight
    BatchTemperature : REAL; // Batch temperature
    BatchPressure : REAL; // Batch pressure
    BatchTime : TIME;    // Batch time
    BatchQuality : BOOL; // Batch quality flag
    BatchStatus : BOOL; // Batch status (1: Active, 0: Stopped)
END_VAR

VAR_OUTPUT
    Phase1_Start : BOOL; // Phase 1 start signal
    Phase1_Stop : BOOL;  // Phase 1 stop signal
    Phase2_Start : BOOL; // Phase 2 start signal
    Phase2_Stop : BOOL;  // Phase 2 stop signal
    Phase3_Start : BOOL; // Phase 3 start signal
    Phase3_Stop : BOOL;  // Phase 3 stop signal
    Phase4_Start : BOOL; // Phase 4 start signal
    Phase4_Stop : BOOL;  // Phase 4 stop signal
    Phase5_Start : BOOL; // Phase 5 start signal
    Phase5_Stop : BOOL;  // Phase 5 stop signal
    Phase6_Start : BOOL; // Phase 6 start signal
    Phase6_Stop : BOOL;  // Phase 6 stop signal
    Phase7_Start : BOOL; // Phase 7 start signal
    Phase7_Stop : BOOL;  // Phase 7 stop signal
    Phase8_Start : BOOL; // Phase 8 start signal
    Phase8_Stop : BOOL;  // Phase 8 stop signal
    Phase9_Start : BOOL; // Phase 9 start signal
    Phase9_Stop : BOOL;  // Phase 9 stop signal
    Phase10_Start : BOOL; // Phase 10 start signal
    Phase10_Stop : BOOL; // Phase 10 stop signal
    Phase11_Start : BOOL; // Phase 11 start signal
    Phase11_Stop :
