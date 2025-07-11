### Intent:
**Intent Summary:**  
Design an IEC 61131-3 Structured Text program to control the automated start-up and shutdown sequences of a 3D pouch making machine, ensuring synchronized activation of heating/cooling stations, tension-regulated feeding, and safe cutter operation while maintaining critical winding tension for product quality.

### Prompt:
**3D Pouch Making Machine:**

Design a detailed start-up and shutdown sequence for a 3D pouch making machine in IEC 61131-3 Structured Text. The machine consists of 8 heating stations, 8 cooling stations, one horizontal cutter, one vertical cutter, and two feeder units responsible for raw material feeding. Winding tension management is critical throughout the process to ensure proper tension in the raw material.

Write a structured start-up sequence that sequentially activates the heating and cooling stations, regulates the feeder units to maintain optimal tension, and ensures proper synchronization between the cutters and material flow. Additionally, create a shutdown sequence that safely deactivates each component in the correct order, ensuring proper cooling and tension release.

Ensure the program includes typical parameter values, timers, and conditions for each stage of the start-up and shutdown procedures, and discuss the importance of winding tension in maintaining machine efficiency and product quality.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial automation engineer specializing in IEC 61131-3 Structured Text programming for complex multi-stage machinery.

🟩 I (Input) – Information Provided

You are tasked with programming a 3D pouch making machine that includes 8 heating stations, 8 cooling stations, one horizontal cutter, one vertical cutter, and two feeder units for raw material. The machine must execute a precise start-up and shutdown sequence, where winding tension management is critical to ensure material stability and product quality. The system must respond to thermal thresholds, synchronization logic, and safe sequencing requirements.

🟧 S (Steps) – Steps to Perform
	1.	Write a start-up sequence in Structured Text that:
	•	Activates heating and cooling stations in proper order.
	•	Waits for heaters to reach set temperatures before proceeding.
	•	Regulates feeder units to maintain optimal winding tension.
	•	Synchronizes cutter operation with material movement.
	2.	Write a shutdown sequence that:
	•	Safely deactivates cutters and feeder units.
	•	Ensures proper cooling time before turning off cooling stations.
	•	Releases winding tension gradually to avoid material snapping or misalignment.
	3.	Include timers, threshold parameters, and safety interlocks for each step, and structure your code with comments for clarity.

🟦 E (Expectation) – Expected Output

Produce a well-documented IEC 61131-3 Structured Text program that executes the start-up and shutdown sequences safely and efficiently. The code should reflect real industrial conditions and maintain high reliability, product consistency, and machine longevity, with clear logic and robust handling of timing, synchronization, and tension control.

### Generated Code:
**Intent Summary:**  
Design an IEC 61131-3 Structured Text program to control the automated start-up and shutdown sequences of a 3D pouch making machine, ensuring synchronized activation of heating/cooling stations, tension-regulated feeding, and safe cutter operation while maintaining critical winding tension for product quality.
**3D Pouch Making Machine:**

Design a detailed start-up and shutdown sequence for a 3D pouch making machine in IEC 61131-3 Structured Text. The machine consists of 8 heating stations, 8 cooling stations, one horizontal cutter, one vertical cutter, and two feeder units responsible for raw material feeding. Winding tension management is critical throughout the process to ensure proper tension in the raw material.

Write a structured start-up sequence that sequentially activates the heating and cooling stations, regulates the feeder units to maintain optimal tension, and ensures proper synchronization between the cutters and material flow. Additionally, create a shutdown sequence that safely deactivates each component in the correct order, ensuring proper cooling and tension release.

Ensure the program includes typical parameter values, timers, and conditions for each stage of the start-up and shutdown procedures, and discuss the importance of winding tension in maintaining machine efficiency and product quality.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as an industrial automation engineer specializing in IEC 61131-3 Structured Text programming for complex multi-stage machinery.

🟩 I (Input) – Information Provided

You are tasked with programming a 3D pouch making machine that includes 8 heating stations, 8 cooling stations, one horizontal cutter, one vertical cutter, and two feeder units for raw material. The machine must execute a precise start-up and shutdown sequence, where winding tension management is critical to ensure material stability and product quality. The system must respond to thermal thresholds, synchronization logic, and safe sequencing requirements.

🟧 S (Steps) – Steps to Perform
	1.	Write a start-up sequence in Structured Text that:
	•	Activates heating and cooling stations in proper order.
	•	Waits for heaters to reach set temperatures before proceeding.
	•	Regulates feeder units to maintain optimal winding tension.
	•	Synchronizes cutter operation with material movement.
	2.	Write a shutdown sequence that:
	•	Safely deactivates cutters and feeder units.
	•	Ensures proper cooling time before turning off cooling stations.
	•	Releases winding tension gradually to avoid material snapping or misalignment.
	3.	Include timers, threshold parameters, and safety interlocks for each step, and structure your code with comments for clarity.

🟦 E (Expectation) – Expected Output

Produce a well-documented IEC 61131-3 Structured Text program that executes the start-up and shutdown sequences safely and efficiently. The code should reflect real industrial conditions and maintain high reliability, product consistency, and machine longevity, with clear logic and robust handling of timing, synchronization, and tension control.
VAR
    // Inputs
    StartButton : BOOL; // Start button input
    StopButton : BOOL;  // Stop button input
    EmergencyStop : BOOL; // Emergency stop input

    // Outputs
    ConveyorMotor : BOOL; // Conveyor motor output
    FeederMotor : BOOL;   // Feeder motor output
    CutterMotor : BOOL;   // Cutter motor output
    Light : BOOL;         // Light output

    // Internal Variables
    Running : BOOL := FALSE; // Machine running state
    Stopping : BOOL := FALSE; // Machine stopping state
    EmergencyStopped : BOOL := FALSE; // Emergency stop state

    // Timers
    TimerStart : TON; // Timer for conveyor start delay
    TimerStop : TON;  // Timer for conveyor stop delay

    // Parameters
    StartDelay : TIME := T#10s; // Conveyor start delay
    StopDelay : TIME := T#5s;   // Conveyor stop delay
END_VAR

// Main Control Logic
IF NOT EmergencyStopped THEN
    // Startup Sequence
    IF StartButton AND NOT Running THEN
        Running := TRUE;
        ConveyorMotor := TRUE;
        FeederMotor := TRUE;
        CutterMotor := TRUE;
        Light := TRUE;
        TimerStart(IN := TRUE, PT := StartDelay);

        // Wait for conveyor to reach speed
        WHILE TimerStart.Q AND Running DO
            // Empty loop to wait for conveyor speed
        END_WHILE;

        // Reset timer and set conveyor as running
        TimerStart(IN := FALSE);
        ConveyorMotor := TRUE;
    END_IF

    // Running Sequence
    IF Running AND NOT StopButton THEN
        // Conveyor and feeder logic
        ConveyorMotor := TRUE;
        FeederMotor := TRUE;
    END_IF

    // Shutdown Sequence
    IF StopButton AND Running THEN
        Running := FALSE;
        ConveyorMotor := FALSE;
