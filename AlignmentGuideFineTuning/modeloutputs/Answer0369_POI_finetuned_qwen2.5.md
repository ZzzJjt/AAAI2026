### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL values with configurable decimal precision, including error handling and relational outputs (equal/greater/less), ensuring robustness against floating-point rounding errors in industrial control logic.

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
Create a reusable IEC 61131-3 function block in Structured Text to compare two REAL values with configurable decimal precision, including error handling and relational outputs (equal/greater/less), ensuring robustness against floating-point rounding errors in industrial control logic.
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
	•	Enable : BOOL (optional, for scan-cycle safety)

	Implement a self-contained function block in IEC 61131-3 Structured Text to compare two REAL inputs up to n decimal places, ensuring scan-cycle safety and providing configurable precision for reliable floating-point comparisons in industrial control logic.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained function block in IEC 61131-3 Structured Text to compare two REAL inputs up to n decimal places. Ensure scan-cycle safety and provide configurable precision for reliable floating-point comparisons in industrial control logic.

⸻

🟩 A (Action) – How to Do It

	•	Define the function block with inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT (number of decimal places)
	•	Enable : BOOL (optional, for scan-cycle safety)
	•	Outputs:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (to handle invalid precision values)
	•	Implement the logic inside the function block:
	•	Scale both inputs by 10^Precision
	•	Perform the comparison using the scaled values
	•	Set the output flags based on the comparison result
	•	Add input validation to ensure Precision is a non-negative integer
	•	(Optional) Include scan-cycle safety by setting the output only when Enable is TRUE
	•	Compile and test the function block in a scan-cycle-safe environment
	•	Provide a detailed explanation of the implementation, including the logic behind scaling and precision handling
	•	Include a discussion on the limitations of floating-point arithmetic and the benefits of using this approach in industrial control systems
	•	Explain how this function block can be used in practical applications, such as PID control, sensor thresholding, or alarm logic, where decimal-level precision is critical
	•	Provide a comparison with built-in comparison functions, highlighting the advantages of a self-contained, configurable comparator
	•	Include a scan-cycle-safe example usage in a control program, demonstrating how to integrate the function block into a real-world control scenario
	•	Lastly, compile the function block and ensure it is scan-cycle-safe, with proper handling of input validation and error checking
	•	Provide a detailed explanation of the implementation, including the logic behind scaling and precision handling
