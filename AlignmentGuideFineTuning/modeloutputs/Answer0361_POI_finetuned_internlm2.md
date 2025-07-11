### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to perform a binary search on a sorted array of 100 integers, ensuring input validation, efficient boundary handling, and clear outputs (found index or -1).  

*(Focus: Modular, real-time PLC lookup for industrial automation.)*

### Prompt:
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation systems, it’s common to work with arrays of sensor readings, setpoints, or index values. Efficient data retrieval is essential, especially when scanning large arrays. A binary search algorithm is optimal for sorted integer arrays, offering logarithmic-time performance compared to linear search. Implementing such logic in IEC 61131-3 Structured Text allows for modular, real-time lookup operations on PLCs.

⸻

🟩 A (Action) – Task to Perform

Create a self-contained function block in Structured Text to perform a binary search on an array of 100 integers. Your implementation should:
	•	Take as input a sorted array, the target value, and an enable flag
	•	Use Low, High, and Mid pointers to narrow the search space
	•	Validate input conditions such as array bounds and search preconditions
	•	Handle edge cases like an empty range or out-of-bounds indices
	•	Output the index of the found value (or -1 if not found), and a boolean flag indicating success

⸻

🟨 R (Result) – Expected Outcome

The result should be a modular, reliable, and reusable binary search function block that runs efficiently on PLC hardware. It should minimize scan time for data lookups and be easily integrated into structured control applications that require high-speed decision-making or condition detection.

⸻

🟦 E (Example) – Concrete Illustration

Here’s an excerpt of what the Structured Text logic might look like:

IF Enable THEN
   Low := 1;
   High := 100;
   Found := FALSE;

   WHILE (Low <= High) AND NOT Found DO
      Mid := (Low + High) / 2;
      IF SearchArray[Mid] = TargetValue THEN
         Index := Mid;
         Found := TRUE;
      ELSIF SearchArray[Mid] > TargetValue THEN
         High := Mid - 1;
      ELSE
         Low := Mid + 1;
      END_IF;
   END_WHILE;

   IF NOT Found THEN
      Index := -1;
   END_IF;
END_IF;

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to perform a binary search on a sorted array of 100 integers, ensuring input validation, efficient boundary handling, and clear outputs (found index or -1).  

*(Focus: Modular, real-time PLC lookup for industrial automation.)*
**Binary Search:**
Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation systems, it’s common to work with arrays of sensor readings, setpoints, or index values. Efficient data retrieval is essential, especially when scanning large arrays. A binary search algorithm is optimal for sorted integer arrays, offering logarithmic-time performance compared to linear search. Implementing such logic in IEC 61131-3 Structured Text allows for modular, real-time lookup operations on PLCs.

⸻

🟩 A (Action) – Task to Perform

Create a self-contained function block in Structured Text to perform a binary search on an array of 100 integers. Your implementation should:
	•	Take as input a sorted array, the target value, and an enable flag
	•	Use Low, High, and Mid pointers to narrow the search space
	•	Validate input conditions such as array bounds and search preconditions
	•	Handle edge cases like an empty range or out-of-bounds indices
	•	Output the index of the found value (or -1 if not found), and a boolean flag indicating success

⸻

🟨 R (Result) – Expected Outcome

The result should be a modular, reliable, and reusable binary search function block that runs efficiently on PLC hardware. It should minimize scan time for data lookups and be easily integrated into structured control applications that require high-speed decision-making or condition detection.

⸻

🟦 E (Example) – Concrete Illustration

Here’s an excerpt of what the Structured Text logic might look like:

IF Enable THEN
   Low := 1;
   High := 100;
   Found := FALSE;

   WHILE (Low <= High) AND NOT Found DO
      Mid := (Low + High) / 2;
      IF SearchArray[Mid] = TargetValue THEN
         Index := Mid;
         Found := TRUE;
      ELSIF SearchArray[Mid] > TargetValue THEN
         High := Mid - 1;
      ELSE
         Low := Mid + 1;
      END_IF;
   END_WHILE;

   IF NOT Found THEN
      Index := -1;
   END_IF;
END_IF;  

The function block should be self-contained, with clear input and output variables, and handle edge cases like empty arrays or out-of-bounds indices. It should be optimized for real-time performance on PLCs, ensuring fast and reliable data retrieval in industrial automation systems.

⸻

🟪 A (Analysis) – Decomposition into Smaller Steps

To create a binary search function block in IEC 61131-3 Structured Text, follow these steps:

1.	Define the input and output variables, including the sorted array, target value, and enable flag.
2.	Initialize the low and high pointers to the array bounds.
3.	Use a while loop to narrow the search range until the target value is found or the range is exhausted.
4.	Within the loop, calculate the midpoint and compare the target value to the midpoint element.
5.	Update the low and high pointers based on the comparison result.
6.	Check for the target value at the midpoint and set the found index if successful.
7.	Handle edge cases like an empty array or out-of-bounds indices.
8.	Output the found index and a success flag.

⸻

🟫 I (Insight) – Key Point or Concept

Binary search is a highly efficient algorithm for finding a specific value in a sorted array. It works by repeatedly dividing the search interval in half until the target value is found or the remaining interval is empty. This approach offers a logarithmic time complexity, making it ideal for large arrays or real-time data retrieval in industrial automation systems.

⸻

🟪 C (Conclusion) – Final Thoughts

By implementing a self-contained binary search function block in IEC 61131-3 Structured Text, you can create a reusable, efficient, and modular solution for searching sorted arrays of integers. This logic can be easily integrated into industrial automation systems, enabling fast and reliable data retrieval in real-time applications. Remember to handle edge cases and ensure input validation to ensure robust performance in a PLC environment.
**Binary Search:**

Implement a self-contained function block in IEC 61131-3 structured text to perform a binary search on an array of 100 integers. Include input validation and efficient handling of search boundaries.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation systems, it’s common to work with arrays of sensor
