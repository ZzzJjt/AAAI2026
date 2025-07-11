### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text to automate the full polyethylene production cycle (raw material preparation to packaging) with modular logic, phase sequencing, and synchronization, while addressing PLC-specific challenges like timing and resource allocation.

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
Develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text to automate the full polyethylene production cycle (raw material preparation to packaging) with modular logic, phase sequencing, and synchronization, while addressing PLC-specific challenges like timing and resource allocation.
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
    StopButton : BOOL; // Stops the batch process
    EmergencyStop : BOOL; // Emergency stop signal
    BatchID : INT; // Batch identifier
END_VAR

VAR_OUTPUT
    Phase1Running : BOOL; // Phase 1: Raw material preparation
    Phase2Running : BOOL; // Phase 2: Polymerization
    Phase3Running : BOOL; // Phase 3: Quenching
    Phase4Running : BOOL; // Phase 4: Drying
    Phase5Running : BOOL; // Phase 5: Pelletizing
    Phase6Running : BOOL; // Phase 6: Quality control
    Phase7Running : BOOL; // Phase 7: Packaging and storage
    Phase1Done : BOOL; // Phase 1: Raw material preparation complete
    Phase2Done : BOOL; // Phase 2: Polymerization complete
    Phase3Done : BOOL; // Phase 3: Quenching complete
    Phase4Done : BOOL; // Phase 4: Drying complete
    Phase5Done : BOOL; // Phase 5: Pelletizing complete
    Phase6Done : BOOL; // Phase 6: Quality control complete
    Phase7Done : BOOL; // Phase 7: Packaging and storage complete
    Phase1Error : BOOL; // Phase 1: Raw material preparation error
    Phase2Error : BOOL; // Phase 2: Polymerization error
    Phase3Error : BOOL; // Phase 3: Quenching error
    Phase4Error : BOOL; // Phase 4: Drying error
    Phase5Error : BOOL; // Phase 5: Pelletizing error
    Phase6Error : BOOL; // Phase 6: Quality control error
    Phase7Error : BOOL; // Phase 7: Packaging and storage error
    Phase1ErrorDetected : BOOL; // Phase 1: Raw material preparation error detected
    Phase2ErrorDetected : BOOL; // Phase 2: Polymerization error detected
    Phase3ErrorDetected : BOOL; // Phase 3: Quenching error detected
    Phase4ErrorDetected : BOOL; // Phase 4: Drying error detected
    Phase5ErrorDetected : BOOL; // Phase 5: Pelletizing error detected
    Phase6ErrorDetected : BOOL;
