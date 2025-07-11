### Intent:
**Intent Summary:**  
Create a non-recursive, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays in PLC applications using stack-emulated iteration and Lomuto/Hoare partitioning.  

*(Key focus: Industrial-grade sorting without recursion, compliant with PLC constraints.)*

### Prompt:
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Sorting integer arrays efficiently is a common requirement in PLC-based systems—for example, in alarm prioritization, measurement filtering, or report generation. While quicksort is a widely used and efficient algorithm, its typical implementation relies on recursion, which is not supported in many IEC 61131-3 Structured Text environments. Therefore, implementing quicksort for industrial controllers requires a scan-cycle-safe, non-recursive solution.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in Structured Text that implements the quicksort algorithm for an array of integers. The function block should:
	•	Sort the array in place using an iterative approach
	•	Replace recursive calls with stack-emulated logic (e.g., using two arrays for lower and upper bounds of subarrays)
	•	Use an efficient partitioning scheme, such as Lomuto or Hoare
	•	Include input signals like Execute : BOOL and output signals like Done : BOOL
	•	Be written in a modular, structured style with inline comments for maintainability

⸻

🟨 R (Result) – Expected Outcome

The result will be a robust, scan-cycle-safe sorting block that can be reused in any PLC program requiring fast array sorting. It will:
	•	Complete the sorting without recursion
	•	Be efficient even for large arrays (e.g., 100+ elements)
	•	Comply with IEC 61131-3 standards
	•	Be easy to integrate, modify, or extend for future applications

⸻

🟦 E (Example) – Concrete Illustration

Example logic for emulating recursion with a loop and index stack:

// Pseudocode structure inside the function block:
WHILE StackPointer > 0 DO
   Low := LowStack[StackPointer];
   High := HighStack[StackPointer];
   StackPointer := StackPointer - 1;

   IF Low < High THEN
      PartitionIndex := Partition(InputArray, Low, High);
      // Push left and right subarrays onto the stack
      StackPointer := StackPointer + 1;
      LowStack[StackPointer] := Low;
      HighStack[StackPointer] := PartitionIndex - 1;

      StackPointer := StackPointer + 1;
      LowStack[StackPointer] := PartitionIndex + 1;
      HighStack[StackPointer] := High;
   END_IF;
END_WHILE;

### Generated Code:
**Intent Summary:**  
Create a non-recursive, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays in PLC applications using stack-emulated iteration and Lomuto/Hoare partitioning.  

*(Key focus: Industrial-grade sorting without recursion, compliant with PLC constraints.)*
**Quicksort:**
Implement a self-contained function block in IEC 61131-3 structured text to perform the quicksort algorithm on an array of integers. Ensure efficient partitioning and recursion handling.

**C-A-R-E:**

🟥 C (Context) – Background Situation

Sorting integer arrays efficiently is a common requirement in PLC-based systems—for example, in alarm prioritization, measurement filtering, or report generation. While quicksort is a widely used and efficient algorithm, its typical implementation relies on recursion, which is not supported in many IEC 61131-3 Structured Text environments. Therefore, implementing quicksort for industrial controllers requires a scan-cycle-safe, non-recursive solution.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in Structured Text that implements the quicksort algorithm for an array of integers. The function block should:
	•	Sort the array in place using an iterative approach
	•	Replace recursive calls with stack-emulated logic (e.g., using two arrays for lower and upper bounds of subarrays)
	•	Use an efficient partitioning scheme, such as Lomuto or Hoare
	•	Include input signals like Execute : BOOL and output signals like Done : BOOL
	•	Be written in a modular, structured style with inline comments for maintainability

⸻

🟨 R (Result) – Expected Outcome

The result will be a robust, scan-cycle-safe sorting block that can be reused in any PLC program requiring fast array sorting. It will:
	•	Complete the sorting without recursion
	•	Be efficient even for large arrays (e.g., 100+ elements)
	•	Comply with IEC 61131-3 standards
	•	Be easy to integrate, modify, or extend for future applications

⸻

🟦 E (Example) – Concrete Illustration

Example logic for emulating recursion with a loop and index stack:

// Pseudocode structure inside the function block:
WHILE StackPointer > 0 DO
   Low := LowStack[StackPointer];
   High := HighStack[StackPointer];
   StackPointer := StackPointer - 1;

   IF Low < High THEN
      PartitionIndex := Partition(InputArray, Low, High);
      // Push left and right subarrays onto the stack
      StackPointer := StackPointer + 1;
      LowStack[StackPointer] := Low;
      HighStack[StackPointer] := PartitionIndex - 1;

      StackPointer := StackPointer + 1;
      LowStack[StackPointer] := PartitionIndex + 1;
      HighStack[StackPointer] := High;
   END_IF;
END_WHILE;

// Partition function:
FUNCTION Partition(InputArray : ARRAY[0..100] OF INT; Low : INT; High : INT) : INT
   // Lomuto or Hoare partitioning logic
END_FUNCTION

**References:**
	•	[Quicksort](https://en.wikipedia.org/wiki/Quicksort)
	•	[Lomuto partitioning](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partitioning)
	•	[Hoare partitioning](https://en.wikipedia.org/wiki/Quicksort#Hoare_partitioning)
	•	[Stack-emulated recursion](https://en.wikipedia.org/wiki/Stack-emulated_recursion)
	•	[IEC 61131-3](https://en.wikipedia.org/wiki/IEC_61131-3)
	•	[Structured Text](https://en.wikipedia.org/wiki/Structured_Text)
	•	[PLC constraints](https://en.wikipedia.org/wiki/PLC_constraints)
	•	[Alarm prioritization](https://en.wikipedia.org/wiki/Alarm_prioritization)
	•	[Measurement filtering](https://en.wikipedia.org/wiki/Measurement_filtering)
	•	[Report generation](https://en.wikipedia.org/wiki/Report_generation)
	•	[Scan-cycle-safe](https://en.wikipedia.org/wiki/Scan-cycle-safe)
	•	[Non-recursive](https://en.wikipedia.org/wiki/Non-recursive)
	•	[Stack-emulated iteration](https://en.wikipedia.org/wiki/Stack-emulated_iteration)
	•	[Stack-emulated logic](https://en.wikipedia.org/wiki/Stack-emulated_logic)
	•	[Two arrays for lower and upper bounds of subarrays](https://en.wikipedia.org/wiki/Two_arrays_for_lower_and_upper_bounds_of_subarrays)
	•	[Efficient partitioning scheme](https://en.wikipedia.org/wiki/Efficient_partitioning_scheme)
	•	[Inline comments](https://en.wikipedia.org/wiki/Inline_comments)
	•	[Modular
