### Intent:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text to automate the full polyethylene production cycle (raw material preparation to packaging), ensuring modularity, safety, and synchronization across process phases.  

*(Focus: Batch automation, PLC implementation, phased control logic, industrial standards.)*

### Prompt:
**Batch Polyethylene:**

Develop a self-contained program in IEC 61131-3 Structured Text to implement batch control for a polyethylene production process. The program should cover the full production cycle, including the following steps: raw material preparation, polymerization, quenching, drying, pelletizing, quality control, and packaging and storage. Ensure that each step is clearly defined and appropriately sequenced with transitions, and provide detailed comments explaining the logic and control conditions for each phase. Discuss the challenges of integrating batch control into a PLC environment, including timing, resource allocation, and synchronization across multiple production units.

**T-A-G:**

🟥 T (Task)

Create a batch automation program for the full-cycle production of polyethylene using IEC 61131-3 Structured Text, following ISA-88 standards.

🟩 A (Action)

Break the process into clearly defined stages:
	•	Raw material preparation
	•	Polymerization
	•	Quenching
	•	Drying
	•	Pelletizing
	•	Quality control
	•	Packaging and storage

Develop a modular Structured Text program that sequences these phases using timers, control conditions, and interlocks. Implement reusable function blocks (e.g., AddMaterial, StartReaction, BeginDrying) for each operation, and include detailed comments to explain transition logic, parameter settings, and safety constraints. Address integration challenges in PLCs, such as resource contention, timing accuracy, and multi-unit synchronization.

🟦 G (Goal)

Deliver a reliable, maintainable, and ISA-88-compliant control solution that ensures safe, efficient, and scalable execution of the polyethylene batch process, ready for industrial deployment and future system expansion.

### Generated Code:
**Intent Summary:**  
Develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text to automate the full polyethylene production cycle (raw material preparation to packaging), ensuring modularity, safety, and synchronization across process phases.  

*(Focus: Batch automation, PLC implementation, phased control logic, industrial standards.)*
**Batch Polyethylene:**

Develop a self-contained program in IEC 61131-3 Structured Text to implement batch control for a polyethylene production process. The program should cover the full production cycle, including the following steps: raw material preparation, polymerization, quenching, drying, pelletizing, quality control, and packaging and storage. Ensure that each step is clearly defined and appropriately sequenced with transitions, and provide detailed comments explaining the logic and control conditions for each phase. Discuss the challenges of integrating batch control into a PLC environment, including timing, resource allocation, and synchronization across multiple production units.

**T-A-G:**

🟥 T (Task)

Create a batch automation program for the full-cycle production of polyethylene using IEC 61131-3 Structured Text, following ISA-88 standards.

🟩 A (Action)

Break the process into clearly defined stages:
	•	Raw material preparation
	•	Polymerization
	•	Quenching
	•	Drying
	•	Pelletizing
	•	Quality control
	•	Packaging and storage

Develop a modular Structured Text program that sequences these phases using timers, control conditions, and interlocks. Implement reusable function blocks (e.g., AddMaterial, StartReaction, BeginDrying) for each operation, and include detailed comments to explain transition logic, parameter settings, and safety constraints. Address integration challenges in PLCs, such as resource contention, timing accuracy, and multi-unit synchronization.

🟦 G (Goal)

Deliver a reliable, maintainable, and ISA-88-compliant control solution that ensures safe, efficient, and scalable execution of the polyethylene batch process, ready for industrial deployment and future system expansion.
(* IEC 61131-3 Structured Text Program: PolyethyleneBatchControl *)
(* Purpose: Implements ISA-88 batch control for polyethylene production *)

PROGRAM PolyethyleneBatchControl
VAR
    (* Inputs *)
    StartBatch : BOOL;                    (* TRUE to start batch process *)
    StopBatch : BOOL;                     (* TRUE to stop batch process *)
    EmergencyStop : BOOL;                 (* TRUE to stop immediately *)
    RawMaterialLevel : REAL;              (* Raw material level sensor *)
    PolymerizationTemp : REAL;             (* Polymerization temperature *)
    QuenchingTemp : REAL;                 (* Quenching temperature *)
    DryingTemp : REAL;                    (* Drying temperature *)
    PelletizingSpeed : REAL;              (* Pelletizing speed *)
    QualityControlResult : BOOL;          (* TRUE if quality check passes *)
    PackagingLineStatus : BOOL;           (* TRUE if packaging line is ready *)
    StorageTankLevel : REAL;              (* Storage tank level sensor *)
    
    (* Outputs *)
    MaterialPumpOn : BOOL;                (* TRUE to run material pump *)
    PolymerizationHeaterOn : BOOL;        (* TRUE to run polymerization heater *)
    QuenchingStationOn : BOOL;            (* TRUE to run quenching station *)
    DryingOvenOn : BOOL;                  (* TRUE to run drying oven *)
    PelletizerOn : BOOL;                  (* TRUE to run pelletizer *)
    QualityControl : BOOL;                (* TRUE to run quality control *)
    PackagingLine : BOOL;                 (* TRUE to run packaging line *)
    StorageTankInletOpen : BOOL;          (* TRUE to open storage tank inlet *)
    Alarm : BOOL;                         (* TRUE if any fault occurs *)
    Error : BOOL;                         (* TRUE if error occurs *)
    
    (* Internal Variables *)
    CurrentStep : INT := 0;               (* Current process step: 0=Idle, 1=RawMaterial, 2=Polymerization, 3=Quenching, 4=Drying, 5=Pel
