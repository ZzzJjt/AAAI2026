### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for an iterative heapsort algorithm that sorts integer arrays (1–100 elements) with configurable size, execution control, and error handling for industrial PLC applications.  

*(Focus: Configurable sorting, iterative design for PLCs, and safety/output flags.)*

### Prompt:
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Timers are essential in industrial automation for sequencing operations, delays, and safety checks. However, relying on fixed or external timers can limit flexibility and reusability. A timer that lacks configurable duration, start/stop control, or timeout indication can lead to rigid control logic and poor maintainability in PLC systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that acts as a flexible timer. The function block should:
	•	Allow users to configure the time duration
	•	Support Start and Stop signals for runtime control
	•	Track elapsed time and indicate when the timer has timed out
	•	Provide output flags for Running, Done, and optionally RemainingTime

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	2.	Use internal variables to:
	•	Store StartTime and ElapsedTime
	•	Reset when Stop = TRUE
	•	Accumulate time only when Start = TRUE and Stop = FALSE
	3.	Provide outputs:
	•	Running : BOOL – active while the timer is counting
	•	Done : BOOL – TRUE when elapsed time ≥ preset time
	•	RemainingTime : TIME – optional, shows remaining time until done
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block for an iterative heapsort algorithm that sorts integer arrays (1–100 elements) with configurable size, execution control, and error handling for industrial PLC applications.  

*(Focus: Configurable sorting, iterative design for PLCs, and safety/output flags.)*
**Timer:**
Implement a self-contained function block in IEC 61131-3 structured text to create a timer. Include configurable time duration, start/stop controls, and timeout handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Timers are essential in industrial automation for sequencing operations, delays, and safety checks. However, relying on fixed or external timers can limit flexibility and reusability. A timer that lacks configurable duration, start/stop control, or timeout indication can lead to rigid control logic and poor maintainability in PLC systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that acts as a flexible timer. The function block should:
	•	Allow users to configure the time duration
	•	Support Start and Stop signals for runtime control
	•	Track elapsed time and indicate when the timer has timed out
	•	Provide output flags for Running, Done, and optionally RemainingTime

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	PresetTime : TIME
	2.	Use internal variables to:
	•	Store StartTime and ElapsedTime
	•	Reset when Stop = TRUE
	•	Accumulate time only when Start = TRUE and Stop = FALSE
	3.	Provide outputs:
	•	Running : BOOL – active while the timer is counting
	•	Done : BOOL – TRUE when elapsed time ≥ preset time
	•	RemainingTime : TIME – optional, shows remaining time until done
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Sorting algorithms are essential in industrial automation for organizing data, optimizing processes, and improving performance. However, relying on built-in sorting functions or external libraries can limit flexibility and reusability. A sorting algorithm that lacks configurable size, execution control, or error handling can lead to rigid control logic and poor maintainability in PLC systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that acts as a sorting algorithm. The function block should:
	•	Allow users to configure the array size
	•	Support Start and Stop signals for runtime control
	•	Provide output flags for Running, Done, and optionally Error
	•	Handle errors such as invalid input, out of bounds, and overflow

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	ArraySize : INT
	•	Array : ARRAY[1..ArraySize] OF INT
	2.	Use internal variables to:
	•	Store the array and its size
	•	Reset when Stop = TRUE
	•	Sort the array using an iterative heapsort algorithm
	3.	Provide outputs:
	•	Running : BOOL – active while the algorithm is running
	•	Done : BOOL – TRUE when the algorithm is complete
	•	Error : BOOL – TRUE when an error occurs
	4.	Ensure the algorithm is scan-cycle safe, reusable, and well-commented

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Safety is a critical concern in industrial automation, where a single error can lead to costly downtime, equipment damage, or even injury. However, relying on built-in safety functions or external libraries can limit flexibility and reusability. A safety function that lacks configurable size, execution control, or error handling can lead to rigid control logic and poor maintainability in PLC systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that acts as a safety function. The function block should:
	•	Allow users to configure the array size
	•	Support Start and
