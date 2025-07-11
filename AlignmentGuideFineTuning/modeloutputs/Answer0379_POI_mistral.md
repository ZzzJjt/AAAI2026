### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL numbers with configurable decimal precision, handling rounding errors and invalid inputs, for reliable industrial control logic.  

*(Focus: Precision-aware floating-point comparison, error handling, modularity for automation systems.)*

### Prompt:
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation, comparing floating-point numbers (REAL values) directly can lead to unpredictable results due to rounding errors and precision limits inherent to binary floating-point representation. This is especially problematic in control logic, threshold detection, or alarm handling where precise decimal-level comparisons are required. A configurable comparator that accounts for decimal precision helps ensure stable and reliable logic decisions.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in IEC 61131-3 Structured Text to compare two REAL inputs with a configurable number of decimal places. The function block should:
	•	Take Input1, Input2 : REAL and Precision : INT as inputs
	•	Round both inputs to the specified precision using a scaling method
	•	Compare the results and set output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Include input validation and an Error : BOOL output in case of invalid precision values
	•	Be written for scan-cycle safety and modular reuse

⸻

🟨 R (Result) – Expected Outcome

The result is a modular, reusable comparator block that accurately determines equality or relational order between two REAL values up to n decimal places, ensuring:
	•	Robust performance under rounding constraints
	•	Clarity in control flow logic
	•	Safe handling of erroneous or extreme inputs
	•	Easy integration into PID tuning, setpoint checks, or quality monitoring systems

⸻

🟦 E (Example) – Concrete Illustration

Example logic (simplified):

Scale := POWER(10, Precision);
Rounded1 := REAL_TO_INT(Input1 * Scale);
Rounded2 := REAL_TO_INT(Input2 * Scale);

Equal := (Rounded1 = Rounded2);
Greater := (Rounded1 > Rounded2);
Less := (Rounded1 < Rounded2);
Error := (Precision < 0);

Inputs:
	•	Input1, Input2 : REAL
	•	Precision : INT
	•	Enable : BOOL

Outputs:
	•	Equal, Greater, Less, Error : BOOL

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL numbers with configurable decimal precision, handling rounding errors and invalid inputs, for reliable industrial control logic.  

*(Focus: Precision-aware floating-point comparison, error handling, modularity for automation systems.)*
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation, comparing floating-point numbers (REAL values) directly can lead to unpredictable results due to rounding errors and precision limits inherent to binary floating-point representation. This is especially problematic in control logic, threshold detection, or alarm handling where precise decimal-level comparisons are required. A configurable comparator that accounts for decimal precision helps ensure stable and reliable logic decisions.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in IEC 61131-3 Structured Text to compare two REAL inputs with a configurable number of decimal places. The function block should:
	•	Take Input1, Input2 : REAL and Precision : INT as inputs
	•	Round both inputs to the specified precision using a scaling method
	•	Compare the results and set output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Include input validation and an Error : BOOL output in case of invalid precision values
	•	Be written for scan-cycle safety and modular reuse

⸻

🟨 R (Result) – Expected Outcome

The result is a modular, reusable comparator block that accurately determines equality or relational order between two REAL values up to n decimal places, ensuring:
	•	Robust performance under rounding constraints
	•	Clarity in control flow logic
	•	Safe handling of erroneous or extreme inputs
	•	Easy integration into PID tuning, setpoint checks, or quality monitoring systems

⸻

🟦 E (Example) – Concrete Illustration

Example logic (simplified):

Scale := POWER(10, Precision);
Rounded1 := REAL_TO_INT(Input1 * Scale);
Rounded2 := REAL_TO_INT(Input2 * Scale);

Equal := (Rounded1 = Rounded2);
Greater := (Rounded1 > Rounded2);
Less := (Rounded1 < Rounded2);
Error := (Precision < 0);

Inputs:
	•	Input1, Input2 : REAL
	•	Precision : INT
	•	Enable : BOOL

Outputs:
	•	Equal, Greater, Less, Error : BOOL

⸻

🟦 T (Test) – Verification Steps

1.	Test the comparator block with various input combinations and precision values to ensure correct output results.
2.	Test edge cases, such as extreme values, rounding errors, and invalid precision inputs, to verify error handling.
3.	Test the block's performance in a real-world control system, such as a PLC, to evaluate its impact on system stability and reliability.
4.	Compare the results with a reference implementation (e.g., using a high-precision programming language) to validate the accuracy of the comparator block.
5.	Evaluate the modularity and ease of integration of the comparator block into different control logic applications.
