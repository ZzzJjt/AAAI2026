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
FUNCTION_BLOCK FB_BatchPolyethylene
VAR_INPUT
    StartBatch : BOOL; // Trigger batch start
    StopBatch : BOOL;   // Stop batch
    BatchID : INT;      // Batch identifier
    BatchStatus : BOOL; // Batch status (0=Idle, 1=Running, 2=Complete)
    BatchProgress : INT; // Progress (0-100%)
    BatchQuality : BOOL; // Quality flag (0=Fail, 1=Pass)
    BatchWeight : REAL;  // Batch weight (kg)
    BatchTemperature : REAL; // Batch temperature (°C)
    BatchPressure : REAL; // Batch pressure (bar)
    BatchDryingTime : TIME; // Drying time (hours)
    BatchDryingTemp : REAL; // Drying temperature (°C)
    BatchDryingPressure : REAL; // Drying pressure (bar)
    BatchDryingTimeRemaining : TIME; // Remaining drying time
    BatchDryingTempRemaining : REAL; // Remaining drying temperature
    BatchDryingPressureRemaining : REAL; // Remaining drying pressure
    BatchDryingStatus : BOOL; // Drying status (0=Idle, 1=Running, 2=Complete)
    BatchDryingQuality : BOOL; // Drying quality flag (0=Fail, 1=Pass)
    BatchDryingWeight : REAL; // Drying weight (kg)
    BatchDryingWeightRemaining : REAL; // Remaining drying weight
    BatchDryingWeightRemainingValid : BOOL; // Weight validation flag
    BatchDryingWeightTolerance : REAL; // Weight tolerance (±1%)
    BatchDryingWeightToleranceValid : BOOL; // Weight tolerance validation flag
    BatchDryingWeightToleranceMax : REAL; // Max weight tolerance (±1%)
    BatchDryingWeightToleranceMaxValid : BOOL; // Max weight tolerance validation flag
    BatchDryingWeightToleranceMin : REAL; // Min weight tolerance (±1%)
    BatchDryingWeightToleranceMinValid : BOOL; // Min weight tolerance validation flag
    BatchDryingWeightToleranceMinMax : REAL; // Min/Max weight tolerance (±1%)
    BatchDryingWeightToleranceMinMaxValid : BOOL; // Min/Max weight tolerance validation flag
    BatchDryingWeightToleranceAlarm : BOOL; // Weight
