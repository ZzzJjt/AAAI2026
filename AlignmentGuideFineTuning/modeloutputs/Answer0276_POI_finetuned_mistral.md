### Intent:
Create a reusable IEC 61131-3 Structured Text function block that calculates the mean and sample standard deviation of a 100-integer array with overflow protection, real-time diagnostics, and clear documentation for industrial automation applications.

### Prompt:
**Mean and StdDev:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute both the mean and standard deviation of an input array consisting of 100 integers. Ensure that the function block is modular and includes detailed comments explaining the steps of calculating both statistical measures. Address potential issues related to overflow or precision when handling large datasets, and provide insights into the function block’s applicability within real-time control systems.

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial automation, it’s often necessary to compute statistical measures such as mean and standard deviation in real time—for example, to monitor process variability, detect sensor anomalies, or evaluate product consistency. However, PLCs programmed with IEC 61131-3 Structured Text don’t provide built-in statistical libraries, and real-time execution requires efficient, deterministic, and resource-aware implementations.

⸻

🟩 A (Action) – The Implementation Task

Create a self-contained function block in IEC 61131-3 Structured Text, named MeanStdDevCalculator, that:
	•	Accepts an input array:
InputArray: ARRAY[1..100] OF INT
	•	Computes and outputs:
	•	Mean: REAL – the average of the 100 integers
	•	StdDev: REAL – the sample standard deviation
	•	Implements the following logic:
	1.	Sum all array elements and divide by 100 for the mean
	2.	For each element, calculate the squared difference from the mean
	3.	Sum the squared differences, divide by 99 (N−1), then compute the square root
	•	Uses REAL types for internal calculations to avoid overflow or precision loss
	•	Includes clear inline comments that:
	•	Explain each step
	•	Warn about potential risks (e.g., integer overflow or underflow)
	•	Clarify why N−1 is used for the standard deviation

⸻

🟨 R (Result) – The Expected Outcome

The resulting function block:
	•	Accurately computes both statistical metrics in a single scan cycle
	•	Is modular and reusable, supporting applications like:
	•	Process stability monitoring
	•	Sensor signal quality checks
	•	Statistical control charting in real time
	•	Is lightweight and efficient enough for real-time control environments
	•	Supports diagnostic output or fail-safes in case of extreme or invalid input values

⸻

🟦 E (Example) – A Practical Use Case

In a packaging line, a PLC collects 100 recent weight measurements from a load cell. These are passed into MeanStdDevCalculator. The function block computes the average weight and standard deviation, which are then used to:
	•	Automatically adjust filler calibration if the mean drifts
	•	Trigger an alarm if standard deviation exceeds a quality threshold

Code snippet example:
FOR i := 1 TO 100 DO
    Sum := Sum + InputArray[i];
END_FOR;
Mean := Sum / 100.0;

FOR i := 1 TO 100 DO
    Temp := InputArray[i] - Mean;
    SumSquaredDiff := SumSquaredDiff + Temp * Temp;
END_FOR;
StdDev := SQRT(SumSquaredDiff / 99.0);

### Generated Code:
Create a reusable IEC 61131-3 Structured Text function block that calculates the mean and sample standard deviation of a 100-integer array with overflow protection, real-time diagnostics, and clear documentation for industrial automation applications.
**Mean and StdDev:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute both the mean and standard deviation of an input array consisting of 100 integers. Ensure that the function block is modular and includes detailed comments explaining the steps of calculating both statistical measures. Address potential issues related to overflow or precision when handling large datasets, and provide insights into the function block’s applicability within real-time control systems.

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial automation, it’s often necessary to compute statistical measures such as mean and standard deviation in real time—for example, to monitor process variability, detect sensor anomalies, or evaluate product consistency. However, PLCs programmed with IEC 61131-3 Structured Text don’t provide built-in statistical libraries, and real-time execution requires efficient, deterministic, and resource-aware implementations.

⸻

🟩 A (Action) – The Implementation Task

Create a self-contained function block in IEC 61131-3 Structured Text, named MeanStdDevCalculator, that:
	•	Accepts an input array:
InputArray: ARRAY[1..100] OF INT
	•	Computes and outputs:
	•	Mean: REAL – the average of the 100 integers
	•	StdDev: REAL – the sample standard deviation
	•	Implements the following logic:
	1.	Sum all array elements and divide by 100 for the mean
	2.	For each element, calculate the squared difference from the mean
	3.	Sum the squared differences, divide by 99 (N−1), then compute the square root
	•	Uses REAL types for internal calculations to avoid overflow or precision loss
	•	Includes clear inline comments that:
	•	Explain each step
	•	Warn about potential risks (e.g., integer overflow or underflow)
	•	Clarify why N−1 is used for the standard deviation

⸻

🟨 R (Result) – The Expected Outcome

The resulting function block:
	•	Accurately computes both statistical metrics in a single scan cycle
	•	Is modular and reusable, supporting applications like:
	•	Process stability monitoring
	•	Sensor signal quality checks
	•	Statistical control charting in real time
	•	Is lightweight and efficient enough for real-time control environments
	•	Supports diagnostic output or fail-safes in case of extreme or invalid input values

⸻

🟦 E (Example) – A Practical Use Case

In a packaging line, a PLC collects 100 recent weight measurements from a load cell. These are passed into MeanStdDevCalculator. The function block computes the average weight and standard deviation, which are then used to:
	•	Automatically adjust filler calibration if the mean drifts
	•	Trigger an alarm if standard deviation exceeds a quality threshold

Code snippet example:
FOR i := 1 TO 100 DO
    Sum := Sum + InputArray[i];
END_FOR;
Mean := Sum / 100.0;

FOR i := 1 TO 100 DO
    Temp := InputArray[i] - Mean;
    SumSquaredDiff := SumSquaredDiff + Temp * Temp;
END_FOR;
StdDev := SQRT(SumSquaredDiff / 99.0);
(* IEC 61131-3 Structured Text: MeanStdDevCalculator Function Block *)
(* Purpose: Computes mean and sample standard deviation of a 100-integer array *)

FUNCTION_BLOCK MeanStdDevCalculator
VAR_INPUT
    InputArray : ARRAY[1..100] OF INT; (* Input array of 100 integers *)
END_VAR

VAR_OUTPUT
    Mean : REAL;                      (* Average of the 100 integers *)
    StdDev : REAL;                    (* Sample standard deviation *)
    ValidOutput : BOOL;               (* TRUE if output is valid *)
    Error : BOOL;                     (* TRUE if invalid input detected *)
    ErrorCode : DWORD;                (* 0: No error, 1: Invalid input *)
END_VAR

VAR
    Sum : REAL;                       (* Sum of array elements *)
    SumSquaredDiff : REAL;            (* Sum of squared differences from mean *)
    Temp : REAL;                      (* Temporary variable for difference *)
    i : INT;                          (* Loop counter *)
    ValidInput : BOOL;                (* Flag for valid input *)
    SumValid : BOOL;                  (* Flag for valid sum *)
    SumSquaredDiffValid : BOOL;       (* Flag for valid SumSquaredDiff *)
    ValidMean : BOOL;                 (* Flag for valid mean *)
    ValidStdDev : BOOL;               (* Flag for valid standard deviation *)
    MaxValue : INT;                   (* Maximum possible value *)
    MinValue : INT;                   (* Minimum possible value *)
    MaxSum : REAL;                    (* Maximum possible sum *)
    MinSum : REAL;                    (* Minimum possible sum *)
    MaxSumSquaredDiff : REAL;         (* Maximum possible SumSquaredDiff *)
    MinSumSquaredDiff : REAL;         (* Minimum possible SumSquaredDiff *)
    MaxMean : REAL;                   (* Maximum possible mean *)
    MinMean : REAL;                   (* Minimum possible mean *)
    MaxStdDev : REAL;                 (* Maximum possible standard deviation
