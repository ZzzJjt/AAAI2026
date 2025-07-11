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
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented for easy integration into other PLC programs.

**Heapsort:**

🟥 B (Before) – The Problem or Challenge

Sorting algorithms are crucial for organizing data in industrial applications. However, implementing sorting algorithms in PLCs can be challenging due to limited resources, memory constraints, and the need for efficient, reusable, and safe code. A sorting algorithm that lacks configurability, error handling, and efficient execution can lead to inefficient control logic and poor maintainability in PLC systems.

⸻

🟩 A (After) – The Desired Outcome

Develop a reusable function block in IEC 61131-3 Structured Text that implements an iterative heapsort algorithm for integer arrays. The function block should:
	•	Allow users to configure the array size (1–100 elements)
	•	Support input and output of the sorted array
	•	Include error handling for invalid array sizes and unsorted arrays
	•	Provide output flags for Sorting, Done, and optionally Swapped
	•	Optimize for efficient execution and minimal memory usage

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Array : ARRAY[1..100] OF INT
	•	ArraySize : WORD
	2.	Use internal variables to:
	•	Store the sorted array and temporary variables for swapping elements
	•	Track the current index and parent index
	3.	Implement the heapsort algorithm iteratively, with a while loop that continues until the array is sorted:
	•	For each element, compare it with its parent and swap if necessary
	•	Decrement the array size and move the last element to the current index
	•	Repeat the process with the new current index as the parent index
	4.	Provide outputs:
	•	Sorting : BOOL – active while the sorting process is ongoing
	•	Done : BOOL – TRUE when the array is sorted
	•	Swapped : BOOL – optional, shows whether an element was swapped during the current iteration
	5.	Ensure the function block is scan-
