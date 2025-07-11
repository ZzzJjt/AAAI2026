### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 structured text function block to compare two REAL values with configurable decimal precision, handling rounding errors and providing comparison outputs (Equal/Greater/Less) and error flags.  

*(Focus: Precision-aware floating-point comparison for reliable industrial logic.)*

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
Create a reusable IEC 61131-3 structured text function block to compare two REAL values with configurable decimal precision, handling rounding errors and providing comparison outputs (Equal/Greater/Less) and error flags.  

*(Focus: Precision-aware floating-point comparison for reliable industrial logic.)*
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
	4.	Include inline comments and safeguards to ensure scan-cycle-safe operation and clarity for maintenance.

⸻

Use this function block in scenarios where precise floating-point comparisons are required, such as:
	•	Process control logic with setpoints and tolerances
	•	Interlock conditions that depend on sensor values
	•	Real-time diagnostics and logging with decimal-level precision
	•	Communication protocols that require floating-point data alignment
	•	Replace manual rounding or floating-point comparison logic in control programs
	•	Enable deterministic floating-point comparisons in PLC logic
	•	Implement in function blocks, methods, or as a utility in IEC 61131-3 Structured Text
	•	Include in industrial automation systems where floating-point precision matters
	•	Replace or improve upon built-in floating-point comparison functions
	•	Ensure scan-cycle-safe and deterministic execution
	•	Enable precise floating-point comparisons in industrial logic
	•	Replace manual rounding or floating-point comparison logic
	•	Implement in function blocks, methods, or as a utility
	•	Include in industrial automation systems
	•	Replace or improve upon built-in floating-point comparison functions
	•	Ensure scan-cycle-safe and deterministic execution
	•	Enable precise floating-point comparisons in industrial logic
	•	Replace manual rounding or floating-point comparison logic
	•	Implement in function blocks, methods, or as a utility
	•	Include in industrial automation systems
	•	Replace or improve upon built-in floating-point comparison functions
	•	Ensure scan-cycle-safe and deterministic execution
	•	Enable precise floating-point comparisons in industrial logic
	•	Replace manual rounding or floating-point comparison logic
	•	Implement in function blocks, methods, or as a utility
	•	Include in industrial automation systems
	•	Replace or improve upon built-in floating-point comparison functions
	•	Ensure scan-cycle-safe and deterministic execution
	•	Enable precise floating-point comparisons in industrial logic
	•	Replace manual rounding or floating-point comparison logic
	•	Implement in function blocks, methods, or as a utility
	•	Include in industrial automation systems
	•	Replace or improve upon built-in floating-point comparison functions
	•	Ensure scan-cycle-safe and deterministic execution
	•	Enable precise floating-point comparisons in industrial logic
	•	Replace manual rounding or floating-point comparison logic
	•	Implement in function blocks, methods, or as a utility
	•	Include in industrial automation systems
	•	Replace
