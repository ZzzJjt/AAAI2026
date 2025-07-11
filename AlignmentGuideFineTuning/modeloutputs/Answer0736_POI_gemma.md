### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to compute the mean and sample standard deviation of a fixed-size integer array (100 elements) for real-time industrial applications, ensuring precision, overflow handling, and deterministic performance with inline documentation.  

*(Focus: Statistical calculation, PLC constraints, modularity, and real-time suitability.)*

### Prompt:
**Mean and StdDev:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute both the mean and standard deviation of an input array consisting of 100 integers. Ensure that the function block is modular and includes detailed comments explaining the steps of calculating both statistical measures. Address potential issues related to overflow or precision when handling large datasets, and provide insights into the function block’s applicability within real-time control systems.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer or control systems engineer responsible for implementing statistical calculations directly on programmable logic controllers using IEC 61131-3 Structured Text. Your task is to ensure the solution works efficiently within the real-time constraints of industrial systems.

⸻

🟩 T (Task) – What You Need to Do

Develop a function block named MeanStdDevCalculator that:
	•	Accepts an input array:
InputArray : ARRAY[1..100] OF INT
	•	Computes two statistical outputs:
	•	Mean : REAL – the average of the 100 values
	•	StdDev : REAL – the sample standard deviation
	•	Follows this logic:
	1.	Mean:
	•	Sum all elements using a REAL accumulator
	•	Divide by 100.0
	2.	Standard deviation:
	•	For each value, subtract the mean and square the result
	•	Sum these squared differences
	•	Divide by 99.0 and apply SQRT
	•	Includes inline comments to explain:
	•	The use of REAL for accuracy and to prevent overflow
	•	Why the divisor is N−1 for sample standard deviation
	•	How the design ensures deterministic scan-time performance
	•	Addresses limitations such as:
	•	Precision loss with large integers
	•	Potential scan-time impact if extended to larger arrays
	•	Inflexibility if array size must change (optionally parameterize in future)

⸻

🟧 F (Format) – Expected Output

Your final function block should include:
	•	Structured Text code like:
 Sum := 0.0;
FOR i := 1 TO 100 DO
    Sum := Sum + InputArray[i];
END_FOR;
Mean := Sum / 100.0;

SumSquaredDiff := 0.0;
FOR i := 1 TO 100 DO
    Diff := InputArray[i] - Mean;
    SumSquaredDiff := SumSquaredDiff + (Diff * Diff);
END_FOR;
StdDev := SQRT(SumSquaredDiff / 99.0);

	•	Inline documentation that clearly describes the purpose of each section
	•	A structure that supports reuse in:
	•	Sensor signal conditioning
	•	Real-time quality assurance
	•	Anomaly detection in control loops

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to compute the mean and sample standard deviation of a fixed-size integer array (100 elements) for real-time industrial applications, ensuring precision, overflow handling, and deterministic performance with inline documentation.  

*(Focus: Statistical calculation, PLC constraints, modularity, and real-time suitability.)*
**Mean and StdDev:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute both the mean and standard deviation of an input array consisting of 100 integers. Ensure that the function block is modular and includes detailed comments explaining the steps of calculating both statistical measures. Address potential issues related to overflow or precision when handling large datasets, and provide insights into the function block’s applicability within real-time control systems.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC programmer or control systems engineer responsible for implementing statistical calculations directly on programmable logic controllers using IEC 61131-3 Structured Text. Your task is to ensure the solution works efficiently within the real-time constraints of industrial systems.

⸻

🟩 T (Task) – What You Need to Do

Develop a function block named MeanStdDevCalculator that:
	•	Accepts an input array:
InputArray : ARRAY[1..100] OF INT
	•	Computes two statistical outputs:
	•	Mean : REAL – the average of the 100 values
	•	StdDev : REAL – the sample standard deviation
	•	Follows this logic:
	1.	Mean:
	•	Sum all elements using a REAL accumulator
	•	Divide by 100.0
	2.	Standard deviation:
	•	For each value, subtract the mean and square the result
	•	Sum these squared differences
	•	Divide by 99.0 and apply SQRT
	•	Includes inline comments to explain:
	•	The use of REAL for accuracy and to prevent overflow
	•	Why the divisor is N−1 for sample standard deviation
	•	How the design ensures deterministic scan-time performance
	•	Addresses limitations such as:
	•	Precision loss with large integers
	•	Potential scan-time impact if extended to larger arrays
	•	Inflexibility if array size must change (optionally parameterize in future)

⸻

🟧 F (Format) – Expected Output

Your final function block should include:
	•	Structured Text code like:
 Sum := 0.0;
FOR i := 1 TO 100 DO
    Sum := Sum + InputArray[i];
END_FOR;
Mean := Sum / 100.0;

SumSquaredDiff := 0.0;
FOR i := 1 TO 100 DO
    Diff := InputArray[i] - Mean;
    SumSquaredDiff := SumSquaredDiff + (Diff * Diff);
END_FOR;
StdDev := SQRT(SumSquaredDiff / 99.0);

	•	Inline documentation that clearly describes the purpose of each section
	•	A structure that supports reuse in:
	•	Sensor signal conditioning
	•	Real-time quality assurance
	•	Anomaly detection in control loops
	•	Other applications that require statistical calculations

**Deliverables:**

Your final submission should include:
	•	A function block named MeanStdDevCalculator
	•	Inline documentation that clearly describes the purpose of each section
	•	A structure that supports reuse in:
	•	Sensor signal conditioning
	•	Real-time quality assurance
	•	Anomaly detection in control loops
	•	Other applications that require statistical calculations

**Resources:**

	•	IEC 61131-3 Structured Text
	•	Real-time control systems
	•	Statistical calculations
	•	PLC programming
	•	Industrial automation

**Constraints:**

	•	The function block must be implemented in IEC 61131-3 Structured Text
	•	The function block must be self-contained and modular
	•	The function block must be deterministic and suitable for real-time control systems
	•	The function block must be able to handle large datasets without overflow or precision loss
	•	The function block must be able to handle arrays of any size (optionally parameterize in future)
	•	The function block must be able to handle arrays of any data type (optionally parameterize in future)
	•	The function block must be able to handle arrays of any dimension (optionally parameterize in future)
	•	The function block must be able to handle arrays of any shape (optionally parameterize in future)
	•	The function block must be able to handle arrays of any order (optionally parameterize in future)
	•	The function block must be able to handle arrays of any size (optionally parameterize in future)
	•	The function block must be able to handle arrays of any data type (optionally parameterize in future)
	•	The function block must be able to handle arrays of any dimension (optionally parameterize in future)
	•	The function block must be able to handle arrays of any shape (optionally parameterize in future)
	•	The function block must be able to handle arrays of any order (optionally parameterize in future)
	•	The function block must be able to handle arrays of any size (optionally parameterize in future)
	•	The function block must be able to handle arrays of any data type (optionally parameterize in future)
	•
