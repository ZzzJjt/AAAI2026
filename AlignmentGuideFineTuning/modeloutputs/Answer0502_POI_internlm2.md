### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to compute the Fast Fourier Transform (FFT) of a fixed-size real-valued input array, optimized for real-time PLC execution with clear documentation on algorithmic steps and performance limitations.  

*(Focus: Efficient PLC implementation of FFT for industrial signal analysis.)*

### Prompt:
**Fast Fourier Transform:**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute the Fast Fourier Transform (FFT) of a given input array. Ensure that the implementation is efficient and includes detailed comments explaining the algorithmic steps involved in computing the FFT. Discuss any limitations in terms of computational complexity and real-time performance, as well as considerations for handling input size constraints typically found in industrial control systems.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or control systems engineer responsible for implementing a Fast Fourier Transform (FFT) algorithm using IEC 61131-3 Structured Text on a real-time industrial controller for signal analysis.

⸻

🟩 I (Input) – What You’re Given

You are tasked with creating a self-contained function block that:
	•	Accepts a REAL input array (e.g., InputSignal: ARRAY[1..64] OF REAL)
	•	Computes the FFT of the input using an efficient algorithm such as radix-2 Cooley-Tukey
	•	Returns either a magnitude spectrum or real/imaginary parts
	•	Is optimized for performance and real-time execution
	•	Includes clear inline comments that explain the major algorithmic steps
	•	Addresses PLC limitations such as memory, scan time, and fixed input size

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block interface:
	•	Input: real-valued array (fixed size, e.g., 64 points)
	•	Output: either amplitude array or real/imaginary arrays
	2.	Implement FFT logic using:
	•	Bit-reversal reordering
	•	Butterfly computation with twiddle factors
	•	Looping constructs that avoid recursion or dynamic memory usage
	3.	Optimize for PLC performance by:
	•	Using only power-of-two input sizes
	•	Precomputing or approximating sine/cosine values if needed
	•	Limiting execution time to fit within typical scan cycles
	4.	Comment thoroughly, explaining:
	•	Purpose of each calculation step
	•	How twiddle factors are computed and applied
	•	How to interpret the resulting frequency bins
	5.	Document known limitations, such as:
	•	Fixed input length
	•	Absence of floating-point complex number support on some PLCs

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a modular, efficient FFT function block that performs spectral analysis in real time, suitable for:
	•	Vibration monitoring
	•	Motor current signature analysis
	•	Predictive maintenance triggers
	•	Harmonic analysis in power systems

The block should run within acceptable PLC scan times, remain numerically stable, and provide meaningful frequency-domain data without external processing tools.

### Generated Code:
**Intent Summary:**  
Create an IEC 61131-3 Structured Text function block to compute the Fast Fourier Transform (FFT) of a fixed-size real-valued input array, optimized for real-time PLC execution with clear documentation on algorithmic steps and performance limitations.  

*(Focus: Efficient PLC implementation of FFT for industrial signal analysis.)*
**Fast Fourier Transform:**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute the Fast Fourier Transform (FFT) of a given input array. Ensure that the implementation is efficient and includes detailed comments explaining the algorithmic steps involved in computing the FFT. Discuss any limitations in terms of computational complexity and real-time performance, as well as considerations for handling input size constraints typically found in industrial control systems.

**R-I-S-E:**

🟥 R (Role) – Your Role

You are a PLC programmer or control systems engineer responsible for implementing a Fast Fourier Transform (FFT) algorithm using IEC 61131-3 Structured Text on a real-time industrial controller for signal analysis.

⸻

🟩 I (Input) – What You’re Given

You are tasked with creating a self-contained function block that:
	•	Accepts a REAL input array (e.g., InputSignal: ARRAY[1..64] OF REAL)
	•	Computes the FFT of the input using an efficient algorithm such as radix-2 Cooley-Tukey
	•	Returns either a magnitude spectrum or real/imaginary parts
	•	Is optimized for performance and real-time execution
	•	Includes clear inline comments that explain the major algorithmic steps
	•	Addresses PLC limitations such as memory, scan time, and fixed input size

⸻

🟧 S (Steps) – What You Need to Do
	1.	Define the function block interface:
	•	Input: real-valued array (fixed size, e.g., 64 points)
	•	Output: either amplitude array or real/imaginary arrays
	2.	Implement FFT logic using:
	•	Bit-reversal reordering
	•	Butterfly computation with twiddle factors
	•	Looping constructs that avoid recursion or dynamic memory usage
	3.	Optimize for PLC performance by:
	•	Using only power-of-two input sizes
	•	Precomputing or approximating sine/cosine values if needed
	•	Limiting execution time to fit within typical scan cycles
	4.	Comment thoroughly, explaining:
	•	Purpose of each calculation step
	•	How twiddle factors are computed and applied
	•	How to interpret the resulting frequency bins
	5.	Document known limitations, such as:
	•	Fixed input length
	•	Absence of floating-point complex number support on some PLCs

⸻

🟦 E (Expectation) – What Success Looks Like

You deliver a modular, efficient FFT function block that performs spectral analysis in real time, suitable for:
	•	Vibration monitoring
	•	Motor current signature analysis
	•	Predictive maintenance triggers
	•	Harmonic analysis in power systems

The block should run within acceptable PLC scan times, remain numerically stable, and provide meaningful frequency-domain data without external processing tools. The comments and documentation should be clear and concise, allowing other engineers to understand and modify the code as needed.

**Additional Considerations:**

1.	**Memory Constraints:** PLCs have limited memory, so ensure that the function block uses minimal memory and does not require dynamic memory allocation.
2.	**Scan Time Constraints:** PLCs have a fixed scan time, typically in the order of milliseconds. Ensure that the FFT computation completes within this time frame.
3.	**Fixed Input Size:** PLCs often have fixed input sizes, such as 64 points. Ensure that the function block can handle such constraints and does not require resizing or dynamic memory allocation.
4.	**Numerical Stability:** Ensure that the FFT computation remains numerically stable, especially when dealing with large input arrays or high frequencies.
5.	**Complex Number Support:** Some PLCs may not support complex number operations directly. Consider alternative approaches to handle real/imaginary parts or use a library that provides complex number support.
6.	**Performance Optimization:** Optimize the FFT algorithm for real-time performance, considering factors such as loop unrolling, precomputing twiddle factors, and minimizing memory access.
7.	**Documentation:** Provide clear and concise documentation that explains the algorithmic steps, twiddle factor computation, and interpretation of the frequency bins. Include any known limitations and recommendations for handling them.
8.	**Testing:** Thoroughly test the function block with various input arrays, including edge cases and real-world scenarios, to ensure its correctness and performance.

**Deliverables:**

1.	**Function Block Code:** A self-contained IEC 61131-3 Structured Text function block that implements the FFT algorithm.
2.	**Documentation:** Detailed comments within the code and a separate document that explains the algorithmic steps, performance considerations, and known limitations.
3.	**Test Cases:** A set of test cases that verify the correctness and performance of the function block under various scenarios.

**Deadline:** 2 weeks from the start of the project.

**Budget:** $500 (USD)

**Additional Resources:**

1.	IEC 61131-3: Structured Text Standard: [https://www.iec.ch/standards/iec_61131-3.htm](https://www.iec.ch/standards/iec_61131-3
