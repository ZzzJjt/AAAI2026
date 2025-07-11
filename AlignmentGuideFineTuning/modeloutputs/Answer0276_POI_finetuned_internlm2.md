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
StdDev := SQRT(SumSquaredDiff / 99.0);  // N-1 for sample standard deviation

**T-A-B:**

🟥 T (Task) – The Task

Create a self-contained function block in IEC 61131-3 Structured Text to compute the mean and standard deviation of an input array of 100 integers. The function block should include detailed comments explaining the steps of calculating both statistical measures, and should address potential issues related to overflow or precision when handling large datasets.

⸻

🟩 A (Action) – The Action

Create a function block named MeanStdDevCalculator that accepts an input array of 100 integers and outputs the mean and standard deviation. The function block should implement the following logic:

1.	Compute the sum of all array elements and divide by 100 to calculate the mean.
2.	For each element in the array, calculate the squared difference from the mean.
3.	Compute the sum of the squared differences, divide by 99 (N-1), and take the square root to calculate the standard deviation.

Use REAL types for internal calculations to avoid overflow or precision loss. Include clear inline comments that explain each step and warn about potential risks, such as integer overflow or underflow. Clarify why N-1 is used for the standard deviation.

⸻

🟨 R (Result) – The Result

The resulting function block should accurately compute both statistical metrics in a single scan cycle. It should be modular and reusable, supporting applications like process stability monitoring, sensor signal quality checks, and statistical control charting in real-time control environments. The function block should be lightweight and efficient enough for real-time control, and should support diagnostic output or fail-safes in case of extreme or invalid input values.

⸻

🟦 E (Example) – An Example

In a packaging line, a PLC collects 100 recent weight measurements from a load cell. These are passed into MeanStdDevCalculator. The function block computes the average weight and standard deviation, which are then used to:

•	Automatically adjust filler calibration if the mean drifts
•	Trigger an alarm if the standard deviation exceeds a quality threshold

**C-A-R-E:**

🟥 C (Context) – The Background

In industrial automation, it’s often necessary to compute statistical measures such as mean and standard deviation in real time—for example, to monitor process variability, detect sensor anomalies, or evaluate product consistency. However,
