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
END_WHILE; To create a non-recursive, scan-cycle-safe quicksort function block in IEC 61131-3 Structured Text, we will follow the steps outlined in the C-A-R-E framework. Below is the implementation of the quicksort algorithm using Lomuto partitioning and stack emulation.

```structuredtext
FUNCTION_BLOCK QuickSort
VAR
   InputArray : ARRAY[0..99] OF INT; // Adjust size as needed
   LowStack : ARRAY[0..99] OF INT;
   HighStack : ARRAY[0..99] OF INT;
   StackPointer : INT := 0;
   Execute : BOOL;
   Done : BOOL := FALSE;
   PartitionIndex : INT;
   Low : INT;
   High : INT;
   Pivot : INT;
   i : INT;
   j : INT;
   temp : INT;
END_VAR

PROCEDURE Partition
   VAR
      i : INT := Low;
      j : INT := High + 1;
      Pivot : INT := InputArray[Low];
   END_VAR

   WHILE TRUE DO
      WHILE InputArray[i] < Pivot DO
         i := i + 1;
      END_WHILE;

      WHILE InputArray[j] > Pivot DO
         j := j - 1;
      END_WHILE;

      IF i >= j THEN
         RETURN j;
      ELSE
         temp := InputArray[i];
         InputArray[i] := InputArray[j];
         InputArray[j] := temp;
         i := i + 1;
         j := j - 1;
      END_IF;
   END_WHILE;
END_PROCEDURE

PROCEDURE Sort
   VAR
      Low : INT := 0;
      High : INT := UBound(InputArray);
   END_VAR

   IF Low < High THEN
      PartitionIndex := Partition(Low, High);
      // Push left and right subarrays onto the stack
      StackPointer := StackPointer + 1;
      LowStack[StackPointer] := Low;
      HighStack[StackPointer] := PartitionIndex - 1;

      StackPointer := StackPointer + 1;
      LowStack[StackPointer] := PartitionIndex + 1;
      HighStack[StackPointer] := High;
   END_IF;
END_PROCEDURE

PROCEDURE ExecuteSort
   VAR
      Low : INT;
      High : INT;
   END_VAR

   IF Execute THEN
      IF StackPointer > 0 THEN
         Low := Low
