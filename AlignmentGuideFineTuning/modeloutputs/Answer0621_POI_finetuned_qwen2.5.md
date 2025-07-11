### Intent:
**Intent Summary:**  
Design a structured start-up and shutdown sequence in IEC 61131-3 Structured Text for a 3D pouch making machine, ensuring synchronized activation/deactivation of heating/cooling stations, cutters, and feeders with precise winding tension control to maintain product quality and machine safety.

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
Design a structured start-up and shutdown sequence in IEC 61131-3 Structured Text for a 3D pouch making machine, ensuring synchronized activation/deactivation of heating/cooling stations, cutters, and feeders with precise winding tension control to maintain product quality and machine safety.
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

Produce a well-documented IEC 61131-3 Structured Text program that executes the start-up and shutdown sequences safely and efficiently. The code should reflect real industrial conditions and maintain high reliability, product consistency, and machine longevity, with clear logic and robust handling of timing, synchronization, and tension control. Discuss the importance of winding tension in maintaining machine efficiency and product quality, ensuring that the program accounts for thermal dynamics, cutter coordination, and feeder tension management.

**T-A-G:**

⸻

🟥 T (Task) – What You Need to Do

Design a start-up and shutdown sequence in IEC 61131-3 Structured Text for a 3D pouch making machine with 8 heating stations, 8 cooling stations, one horizontal cutter, one vertical cutter, and two feeder units responsible for raw material feeding. Winding tension management is critical throughout the process.

🟩 A (Action) – How to Do It

	1.	Create a detailed start-up sequence:
	•	Sequentially turn on the heating and cooling stations, ensuring proper temperature control.
	•	Implement logic to regulate feeder units to maintain optimal tension in the raw material.
	•	Synchronize the cutters with the material flow to prevent damage or misalignment.
	2.	Develop a shutdown sequence:
	•	Safely de-activate the cutters and feeder units in the correct order.
	•	Allow the cooling stations to cool down properly before being shut off.
	•	Release the winding tension gradually to prevent material damage or misalignment.
	3.	Include typical parameter values, timers, and conditions for each stage of the start-up and shutdown procedures.

🟧 G (Goal) – What You’re Aiming For

	•	A well-structured start-up and shutdown sequence in IEC 61131-3 Structured Text that ensures proper synchronization, tension control, and safety for the 3D pouch making machine.
	•	Accurate parameter values, timers, and conditions to ensure smooth operation and prevent damage to the machine or product quality.
	•	A discussion on the importance of winding tension in maintaining machine efficiency and product consistency.

⸻

**T-A-G:**

⸻

🟥 T (Task) – What You Need to Do

Design a start-up and shutdown sequence in IEC 61131-3 Structured Text for a 3D pouch making machine with 8 heating stations, 8 cooling stations, one horizontal cutter, one vertical cutter, and two feeder units responsible for raw material feeding. Winding tension management is critical throughout the process.

🟩 A (Action) – How to Do It

	1.	Create a detailed start-up sequence:
	•	Sequentially turn on the heating and cooling stations, ensuring
