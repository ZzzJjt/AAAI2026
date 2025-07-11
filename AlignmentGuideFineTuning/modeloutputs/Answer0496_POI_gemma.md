### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to efficiently compute the mean and sample standard deviation of a 100-integer array on a PLC, ensuring real-time performance, overflow handling, and clear documentation for process monitoring or quality control applications.  

*(Focus: Statistical calculation, PLC constraints, modularity, and real-time suitability.)*

### Prompt:
**Mean and StdDev:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute both the mean and standard deviation of an input array consisting of 100 integers. Ensure that the function block is modular and includes detailed comments explaining the steps of calculating both statistical measures. Address potential issues related to overflow or precision when handling large datasets, and provide insights into the function block’s applicability within real-time control systems.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer tasked with developing a reusable and efficient function block in IEC 61131-3 Structured Text to compute statistical metrics directly on a programmable logic controller.

⸻

🟩 I (Input) – What You’re Given

You are provided with:
	•	A 100-element integer input array:
InputArray: ARRAY[1..100] OF INT
	•	The requirement to compute:
	•	The mean (arithmetic average)
	•	The sample standard deviation
	•	Constraints such as:
	•	Limited processing power and memory on PLCs
	•	The need for real-time execution within a control scan cycle
	•	Potential for overflow or precision loss during integer summation and squared operations

⸻

🟧 S (Steps) – What You Need to Do
	1.	Create a function block named MeanStdDevCalculator with appropriate inputs and outputs:
 VAR_INPUT
    InputArray : ARRAY[1..100] OF INT;
  END_VAR
  VAR_OUTPUT
    Mean : REAL;
    StdDev : REAL;
  END_VAR
  2.	Implement logic for the mean:
	•	Accumulate the sum using a loop with a REAL accumulator to avoid overflow
	•	Divide by 100.0 to obtain the mean
	3.	Implement logic for the standard deviation:
	•	Loop again through the array
	•	Subtract the mean from each element, square the result, and accumulate
	•	Divide by 99.0 (N - 1) and apply the square root function to get the standard deviation
	4.	Use inline comments to explain each part of the process:
	•	Why REAL is used for intermediate variables
	•	Why the divisor is 99.0 (for sample standard deviation)
	•	Error checking strategies (optional)
	5.	Optimize for real-time use:
	•	Use fixed-size loops for deterministic timing
	•	Avoid dynamic memory or recursive calls
	•	Test on target PLC hardware to ensure execution fits within scan time

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a fully operational, modular function block that:
	•	Accurately calculates the mean and standard deviation of a 100-element integer array
	•	Executes efficiently and predictably within a real-time PLC scan cycle
	•	Is applicable to:
	•	Process monitoring
	•	Sensor signal diagnostics
	•	Quality control and statistical alarms
	•	Is reusable and maintainable, with well-commented logic and clear structure

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block to efficiently compute the mean and sample standard deviation of a 100-integer array on a PLC, ensuring real-time performance, overflow handling, and clear documentation for process monitoring or quality control applications.  

*(Focus: Statistical calculation, PLC constraints, modularity, and real-time suitability.)*
**Mean and StdDev:**

Create a self-contained function block in IEC 61131-3 Structured Text to compute both the mean and standard deviation of an input array consisting of 100 integers. Ensure that the function block is modular and includes detailed comments explaining the steps of calculating both statistical measures. Address potential issues related to overflow or precision when handling large datasets, and provide insights into the function block’s applicability within real-time control systems.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or automation engineer tasked with developing a reusable and efficient function block in IEC 61131-3 Structured Text to compute statistical metrics directly on a programmable logic controller.

⸻

🟩 I (Input) – What You’re Given

You are provided with:
	•	A 100-element integer input array:
InputArray: ARRAY[1..100] OF INT
	•	The requirement to compute:
	•	The mean (arithmetic average)
	•	The sample standard deviation
	•	Constraints such as:
	•	Limited processing power and memory on PLCs
	•	The need for real-time execution within a control scan cycle
	•	Potential for overflow or precision loss during integer summation and squared operations

⸻

🟧 S (Steps) – What You Need to Do
	1.	Create a function block named MeanStdDevCalculator with appropriate inputs and outputs:
 VAR_INPUT
    InputArray : ARRAY[1..100] OF INT;
  END_VAR
  VAR_OUTPUT
    Mean : REAL;
    StdDev : REAL;
  END_VAR
  2.	Implement logic for the mean:
	•	Accumulate the sum using a loop with a REAL accumulator to avoid overflow
	•	Divide by 100.0 to obtain the mean
	3.	Implement logic for the standard deviation:
	•	Loop again through the array
	•	Subtract the mean from each element, square the result, and accumulate
	•	Divide by 99.0 (N - 1) and apply the square root function to get the standard deviation
	4.	Use inline comments to explain each part of the process:
	•	Why REAL is used for intermediate variables
	•	Why the divisor is 99.0 (for sample standard deviation)
	•	Error checking strategies (optional)
	5.	Optimize for real-time use:
	•	Use fixed-size loops for deterministic timing
	•	Avoid dynamic memory or recursive calls
	•	Test on target PLC hardware to ensure execution fits within scan time

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a fully operational, modular function block that:
	•	Accurately calculates the mean and standard deviation of a 100-element integer array
	•	Executes efficiently and predictably within a real-time PLC scan cycle
	•	Is applicable to:
	•	Process monitoring
	•	Sensor signal diagnostics
	•	Quality control and statistical alarms
	•	Is reusable and maintainable, with well-commented logic and clear structure

**Deliverables:**

1.	A fully operational function block in IEC 61131-3 Structured Text that computes the mean and standard deviation of a 100-element integer array.
2.	A detailed explanation of the steps taken to implement the function block, including any optimizations or error handling strategies.
3.	A description of the function block’s applicability within real-time control systems, including any potential issues or constraints.
4.	A demonstration of the function block’s performance on a PLC, including timing and memory usage.
5.	A discussion of the function block’s reusability and maintainability, including any comments or documentation provided.

**Evaluation Criteria:**

1.	Accuracy: The function block should accurately calculate the mean and standard deviation of a 100-element integer array.
2.	Efficiency: The function block should execute efficiently and predictably within a real-time PLC scan cycle.
3.	Modularity: The function block should be modular and well-structured, with clear comments and documentation.
4.	Real-time suitability: The function block should be applicable to real-time control systems, with any potential issues or constraints clearly explained.
5.	Documentation: The function block should be accompanied by a detailed explanation of the steps taken to implement it, including any optimizations or error handling strategies.

**Resources:**

1.	IEC 61131-3 Standard: https://www.iec.ch/standards/standard/view/?number=61131-3
2.	PLC Programming Guide: https://www.plctalk.net/downloads/PLC_Programming_Guide.pdf
3.	Mean and Standard Deviation Calculation: https://www.mathsisfun.com/data/mean-standard-deviation.html
4.	Real-time Programming: https://www.controleng.com/articles/real-time-programming-for-plc-applications/
5.	PLC Performance: https://www.plctalk.net/downloads/PLC_Performance_Guide.pdf

**References:**

1.	IEC 61131-3 Standard: https://www.iec.ch/standards/standard/view/?number=61131-3
2.	PLC Programming Guide: https://www.plctalk.net/downloads/PLC_Programming_Guide.
