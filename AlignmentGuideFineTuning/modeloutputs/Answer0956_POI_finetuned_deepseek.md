### Intent:
The task is to develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text for full-cycle polyethylene production, covering material preparation through packaging with modular function blocks, sequencing logic, and safety constraints for PLC deployment.

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
The task is to develop an ISA-88-compliant batch control program in IEC 61131-3 Structured Text for full-cycle polyethylene production, covering material preparation through packaging with modular function blocks, sequencing logic, and safety constraints for PLC deployment.
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
(* IEC 61131-3 Structured Text program for ISA-88-compliant polyethylene batch control *)
(* Version: 1.0, Date: 2025-05-01 *)

PROGRAM PolyethyleneBatchControl
VAR
    (* Inputs *)
    StartBatch : BOOL;                  (* Start batch control *)
    BatchID : INT;                      (* Batch identifier *)
    MaterialBatchID : INT;              (* Material batch identifier *)
    ReactionTime : TIME;                (* Reaction time in hours *)
    CoolingTime : TIME;                 (* Cooling time in hours *)
    DryingTime : TIME;                  (* Drying time in hours *)
    PelletizingTime : TIME;              (* Pelletizing time in hours *)
    QualityControlID : INT;             (* Quality control identifier *)
    PackagingID : INT;                  (* Packaging identifier *)
    StorageID : INT;                    (* Storage identifier *)
    MaterialBatchStatus : BOOL;         (* TRUE if material batch is ready *)
    ReactionStatus : BOOL;              (* TRUE if reaction is complete *)
    CoolingStatus : BOOL;               (* TRUE if cooling is complete *)
    DryingStatus : BOOL;                (* TRUE if drying is complete *)
    PelletizingStatus : BOOL;            (* TRUE if pelletizing is complete *)
    QualityControlStatus : BOOL;        (* TRUE if quality control is complete *)
    PackagingStatus : BOOL;             (* TRUE if packaging is complete *)
    StorageStatus : BOOL;               (* TRUE if storage is complete *)
    
    (* Outputs *)
    MaterialBatchReady : BOOL;           (* TRUE if material batch is ready *)
    ReactionComplete : BOOL;             (* TRUE if reaction is complete *)
    CoolingComplete : BOOL;              (* TRUE if cooling is complete *)
    DryingComplete : BOOL;               (* TRUE if drying is complete *)
    PelletizingComplete : BOOL;          (* TRUE if pelletizing is complete *)
    QualityControlComplete : BOOL;       (* TRUE if quality control is complete *)
    PackagingComplete : BOOL;            (* TRUE if packaging is complete *)
    StorageComplete : BOOL;              (* TRUE if storage is complete *)
    
    (* Internal Variables *)
    BatchStartTime : TIME;                (* Batch start time *)
    BatchEndTime : TIME;                  (* Batch end time *)
    MaterialBatchStartTime
