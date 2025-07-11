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

This example shows how to structure the binary search logic within a function block, ensuring proper handling of search boundaries and providing clear outputs for further processing in the control program.

⸻

Incorporate this function block into your automation logic to enable fast, efficient, and reliable data retrieval from sorted integer arrays, improving overall system responsiveness and performance.  

**T-A-G:**

🟥 T (Task) – What You Need to Do

	•	Create a self-contained function block in IEC 61131-3 Structured Text
	•	Implement a binary search algorithm for an array of 100 integers
	•	Include input validation and efficient handling of search boundaries
	•	Output the index of the found value or -1 if not found
	•	Provide a boolean flag to indicate whether the search was successful

⸻

🟩 A (Action) – How to Do It

	•	Define the function block with inputs: an array of 100 integers, a target value, and an enable flag
	•	Use two integer variables, Low and High, to represent the search boundaries
	•	Implement a WHILE loop that runs as long as the search boundaries are valid and the target has not been found
	•	Compute the Mid index using (Low + High) / 2
	•	Perform a comparison between the target value and the value at the Mid index
	•	Adjust the search boundaries based on the comparison result
	•	Once the target is found, store the index in an output variable and set the boolean flag to TRUE
	•	Handle the case where the target is not found by setting the index to -1 and the boolean flag to FALSE
	•	Ensure efficient handling of search boundaries and edge cases (e.g., empty range, out-of-bounds indices)

⸻

🟨 R (Result) – What You Should Have

	•	A self-contained function block that performs a binary search on an array of 100 integers
	•	Proper input validation and handling of search boundaries
	•	Accurate outputs for the index of the found value or -1 if not found
	•	A boolean flag to indicate whether the search was successful
	•	Optimized scan time for real-time PLC applications
	•	Modularity and reusability for integration into larger control systems

⸻

🟦 E (Example) – How It Works in Practice

	•
