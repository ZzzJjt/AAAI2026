### Intent:
**Intent Summary:**  
Create a non-recursive, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays in PLC applications using stack-emulated iteration and Lomuto partitioning.

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
Create a non-recursive, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text to efficiently sort integer arrays in PLC applications using stack-emulated iteration and Lomuto partitioning.
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

// Partition function implementation (e.g., Lomuto partitioning):
FUNCTION Partition : INTEGER;
VAR
   PivotIndex : INTEGER;
   LeftIndex  : INTEGER;
   RightIndex : INTEGER;
BEGIN
   PivotIndex := (Low + High) DIV 2;
   InputArray[PivotIndex] := Swap(InputArray[PivotIndex], InputArray[High]);
   LeftIndex := Low;
   RightIndex := High - 1;

   WHILE TRUE DO
      WHILE InputArray[LeftIndex] < InputArray[High] DO
         LeftIndex := LeftIndex + 1;
      END_WHILE;

      WHILE InputArray[RightIndex] > InputArray[High] DO
         RightIndex := RightIndex - 1;
      END_WHILE;

      IF LeftIndex <= RightIndex THEN
         Swap(InputArray[LeftIndex], InputArray[RightIndex]);
         LeftIndex := LeftIndex + 1;
         RightIndex := RightIndex - 1;
      ELSE
         BREAK;
      END_IF;
   END_WHILE;

   Swap(InputArray[High], InputArray[RightIndex + 1]);
   Partition := RightIndex + 1;
END_FUNCTION;

// Swap function implementation:
FUNCTION Swap : VOID;
VAR
   Temp : INTEGER;
BEGIN
   Temp := InputArray[Low];
   InputArray[Low] := InputArray[High];
   InputArray[High] := Temp;
END_FUNCTION;
