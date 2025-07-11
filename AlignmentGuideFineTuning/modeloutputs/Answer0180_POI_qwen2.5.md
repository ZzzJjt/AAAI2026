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
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented for maintainability.

⸻

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Sorting algorithms are fundamental in data processing, but implementing them in PLCs can be challenging due to limited resources and the need for efficiency. A heapsort algorithm is a comparison-based sorting algorithm that is efficient for large datasets. However, creating a reusable, configurable, and safe heapsort function block for PLCs requires careful consideration of execution control, error handling, and output flags.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that implements a configurable heapsort algorithm for integer arrays (1–100 elements). The function block should:
	•	Allow users to configure the array size, input array, and output array
	•	Include execution control signals for start, stop, and reset
	•	Handle errors and provide output flags for success, failure, and array size limits
	•	Ensure the algorithm is iterative and safe for PLC execution

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Start : BOOL
	•	Stop : BOOL
	•	Reset : BOOL
	•	ArraySize : UINT
	•	InputArray : ARRAY[1..100] OF INT
	•	OutputArray : ARRAY[1..100] OF INT
	2.	Use internal variables to:
	•	Store the array size and input/output arrays
	•	Track the sorting progress
	•	Handle errors and provide output flags
	3.	Implement the heapsort algorithm iteratively, ensuring it is safe for PLC execution
	4.	Ensure the function block is scan-cycle safe, reusable, and well-commented for maintainability.

⸻

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Implementing a self-contained function block in IEC 61131-3 Structured Text for a timer requires careful consideration of the timer's functionality, including configurable duration, start/stop control, and timeout handling. A timer that lacks these features can limit flexibility and reusability in PLC systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that acts as a flexible
