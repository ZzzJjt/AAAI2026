### Intent:
**Intent Summary:**  
Create a self-contained, iterative Quicksort function block in IEC 61131-3 Structured Text for PLCs, using stack emulation to avoid recursion while sorting arrays in-place with configurable execution control and state tracking.  

*(Focus: Non-recursive, scan-cycle-safe sorting for industrial automation.)*

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
Create a self-contained, iterative Quicksort function block in IEC 61131-3 Structured Text for PLCs, using stack emulation to avoid recursion while sorting arrays in-place with configurable execution control and state tracking.  

*(Focus: Non-recursive, scan-cycle-safe sorting for industrial automation.)*
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
	4.	Ensure the timer is scan-cycle safe, reusable, and well-commented for easy integration into other control logic.

**Quicksort:**

🟥 B (Before) – The Problem or Challenge

Quicksort is a popular sorting algorithm for its efficiency, but it requires recursion, which can be problematic in PLCs due to their scan-based nature. Implementing a non-recursive Quicksort function block in IEC 61131-3 Structured Text for PLCs is challenging due to the lack of built-in stack support.

⸻

🟩 A (After) – The Desired Outcome

Create a self-contained function block in IEC 61131-3 Structured Text that implements an iterative Quicksort algorithm for sorting arrays in-place. The function block should:
	•	Avoid recursion by using a stack emulation approach
	•	Support configurable execution control, such as batch size and pivot selection strategy
	•	Track the current state of the sorting process
	•	Provide output flags for Sorting, Done, and optionally RemainingElements
	•	Be scan-cycle safe, reusable, and well-commented for easy integration into other control logic

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Array : ARRAY of REAL or INTEGER
	•	BatchSize : NATURAL
	•	PivotSelectionStrategy : ENUM (First, Last, Median)
	2.	Use internal variables to:
	•	Store the current subarray being sorted
	•	Maintain a stack of subarrays to be processed
	•	Track the current state of the sorting process
	3.	Provide outputs:
	•	Sorting : BOOL – active while the sorting is in progress
	•	Done : BOOL – TRUE when the entire array is sorted
	•	RemainingElements : NATURAL – optional, shows the number of remaining elements to be sorted
	4.	Implement the iterative Quicksort algorithm using the stack emulation approach, ensuring it is scan-cycle safe, reusable, and well-commented for easy integration into other control logic.
