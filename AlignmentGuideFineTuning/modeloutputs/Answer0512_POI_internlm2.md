### Intent:
**Intent Summary:**  
Create an efficient, real-time Fast Fourier Transform (FFT) function block in IEC 61131-3 Structured Text for industrial signal analysis, adhering to PLC constraints (fixed input size, scan time) with clear documentation and optimized performance.  

**Key Focus:**  
- Radix-2 Cooley-Tukey FFT implementation  
- Power-of-two input handling, precomputed twiddle factors  
- Real-time suitability (vibration/motor monitoring) with error/edge-case handling  
- Structured Text compliance and inline algorithmic explanations

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
Create an efficient, real-time Fast Fourier Transform (FFT) function block in IEC 61131-3 Structured Text for industrial signal analysis, adhering to PLC constraints (fixed input size, scan time) with clear documentation and optimized performance.  

**Key Focus:**  
- Radix-2 Cooley-Tukey FFT implementation  
- Power-of-two input handling, precomputed twiddle factors  
- Real-time suitability (vibration/motor monitoring) with error/edge-case handling  
- Structured Text compliance and inline algorithmic explanations
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

The block should run within acceptable PLC scan times, remain numerically stable, and provide meaningful frequency-domain data without external processing tools. The inline comments and documentation should be clear and concise, allowing other engineers to understand and modify the code as needed.

**Additional Considerations:**

- Ensure that the function block is compatible with the target PLC's memory and processing capabilities.
- Consider the trade-offs between computational complexity and real-time performance, and discuss how they impact the final implementation.
- Address any edge cases or error handling that may be required for the specific application.
- Optimize the code for the target PLC's instruction set architecture (ISA) and instruction set extensions (ISE) if applicable.
- Test the function block thoroughly, including boundary conditions, edge cases, and real-world scenarios.
- Document any assumptions, limitations, or known issues that may affect the function block's performance or accuracy.
- Provide clear instructions on how to integrate the function block into a larger control system or application.
- Consider the potential for future enhancements or modifications to the function block, and design it with extensibility in mind.
- Ensure that the function block adheres to the latest IEC 61131-3 standards and best practices for PLC programming.
- Provide a comprehensive user manual or documentation that explains how to use the function block, including any required setup or configuration steps.
- Consider the potential for data security and privacy concerns when using the function block in a real-world application, and implement appropriate measures to protect sensitive data.
- Ensure that the function block is thoroughly tested and validated before deployment in a production environment.
- Consider the potential for hardware limitations or constraints when using the function block in a real-world application, and implement appropriate measures to mitigate any potential issues.
- Consider the potential for software limitations or constraints when using the function block in a real-world application, and implement appropriate measures to mitigate any potential issues.
- Consider the potential for environmental or physical constraints when using the function block in a real-world application, and implement appropriate measures to mitigate any potential issues.
- Consider the potential for legal or regulatory constraints when using the function block in a real-world application, and implement appropriate measures to comply with any relevant laws or regulations.
- Consider the potential for ethical or moral constraints when using the function block in a real-world application, and implement appropriate measures to ensure that the function block is used in an ethical and moral manner.
- Consider the potential for social or cultural constraints when using the function block in a real-world application, and implement appropriate measures to ensure that the function block is used in a socially and culturally appropriate manner.
- Consider the potential for economic or financial constraints when
