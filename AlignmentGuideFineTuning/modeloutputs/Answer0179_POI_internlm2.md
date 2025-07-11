### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to compare two REAL values with configurable decimal precision, handling floating-point inaccuracies and providing comparison outputs (Equal/Greater/Less) with error checking.  

*(Focus: Precision-based floating-point comparison for reliable industrial logic, avoiding direct equality checks.)*

### Prompt:
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In many industrial control systems, comparing floating-point values (REAL types) directly can lead to unreliable results due to rounding errors and floating-point representation limits. Without a method to compare numbers with a specified decimal precision, engineers may encounter false mismatches or unstable logic in process comparisons, alarming, or control switching logic.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that compares two REAL inputs up to n decimal places. The function block should:
	•	Accept a user-defined precision level (n)
	•	Normalize or round both input values to that precision before comparison
	•	Provide output flags such as Equal, Greater, and Less
	•	Handle floating-point inaccuracies and include error checks (e.g., invalid precision or input range)

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Input1 : REAL, Input2 : REAL
	•	Precision : INT (number of decimal places to compare)
	•	Enable : BOOL
	2.	Internally calculate a scaling factor based on precision:
\text{Scale} := 10^\text{Precision}
Then compare ROUND(Input1 * Scale) vs ROUND(Input2 * Scale)
	3.	Provide outputs:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (e.g., if Precision < 0 or inputs are invalid)
	4.	Include inline comments and safeguards to ensure scan-cycle-safe operation and clarity

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to compare two REAL values with configurable decimal precision, handling floating-point inaccuracies and providing comparison outputs (Equal/Greater/Less) with error checking.  

*(Focus: Precision-based floating-point comparison for reliable industrial logic, avoiding direct equality checks.)*
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In many industrial control systems, comparing floating-point values (REAL types) directly can lead to unreliable results due to rounding errors and floating-point representation limits. Without a method to compare numbers with a specified decimal precision, engineers may encounter false mismatches or unstable logic in process comparisons, alarming, or control switching logic.

⸻

🟩 A (After) – The Desired Outcome

Develop a self-contained function block in IEC 61131-3 Structured Text that compares two REAL inputs up to n decimal places. The function block should:
	•	Accept a user-defined precision level (n)
	•	Normalize or round both input values to that precision before comparison
	•	Provide output flags such as Equal, Greater, and Less
	•	Handle floating-point inaccuracies and include error checks (e.g., invalid precision or input range)

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the function block with inputs:
	•	Input1 : REAL, Input2 : REAL
	•	Precision : INT (number of decimal places to compare)
	•	Enable : BOOL
	2.	Internally calculate a scaling factor based on precision:
\text{Scale} := 10^\text{Precision}
Then compare ROUND(Input1 * Scale) vs ROUND(Input2 * Scale)
	3.	Provide outputs:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (e.g., if Precision < 0 or inputs are invalid)
	4.	Include inline comments and safeguards to ensure scan-cycle-safe operation and clarity of code.

**Example Usage:**

```ST
VAR
  Input1 : REAL := 3.14159;
  Input2 : REAL := 3.14;
  Precision : INT := 4;
  Equal : BOOL;
  Greater : BOOL;
  Less : BOOL;
  Error : BOOL;
  
BEGIN
  Equal := RealComparator(Input1, Input2, Precision, Enable);
  Greater := RealComparator(Input1, Input2, Precision, Enable);
  Less := RealComparator(Input1, Input2, Precision, Enable);
  Error := RealComparator(Input1, Input2, Precision, Enable);
END
```

**Additional Considerations:**

1.	**Error Handling:** The function block should include error checking for invalid precision values (e.g., Precision < 0) and out-of-range input values. In the case of an error, the function block should set the Error output to TRUE and return a default value (e.g., FALSE for comparison outputs) to prevent unstable logic.
2.	**Scalability:** The function block should be designed to handle a wide range of precision levels (e.g., 0 to 20 decimal places) without performance degradation or memory issues.
3.	**Scan-Cycle Safety:** The function block should be designed to ensure safe operation during scan cycles, avoiding race conditions or data corruption.
4.	**Documentation:** The function block should include inline comments and a detailed description of its inputs, outputs, and behavior to facilitate understanding and maintenance by other engineers.
5.	**Testing:** The function block should be thoroughly tested with a variety of input values, precision levels, and edge cases to ensure reliable and accurate operation in different scenarios.
6.	**Compatibility:** The function block should be compatible with different IEC 61131-3 programming languages (e.g., ST, FBD, SFC) and be easily adaptable to different PLC or HMI platforms.
7.	**Modularity:** The function block should be designed to be easily reusable in different projects, reducing development time and effort.
8.	**Performance:** The function block should be optimized for performance, minimizing scan cycle time and memory usage.
9.	**Maintainability:** The function block should be designed with maintainability in mind, using clear variable names, modular code structure, and inline comments to facilitate future modifications or enhancements.

**Example Output:**

```ST
VAR
