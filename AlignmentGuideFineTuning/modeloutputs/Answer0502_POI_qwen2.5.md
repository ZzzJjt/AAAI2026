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

The block should run within acceptable PLC scan times, remain numerically stable, and provide meaningful frequency-domain data without external processing tools. It should also be adaptable to different input sizes and types, with clear documentation on how to use and interpret the results.

**Fast Fourier Transform (FFT) Function Block Implementation**

```structuredtext
FUNCTION_BLOCK FFT
VAR_INPUT
    InputSignal : ARRAY[1..64] OF REAL; // Input signal array
    InputSize : INT; // Size of the input array (must be a power of 2)
    OutputType : INT; // 0 for magnitude, 1 for real/imaginary parts
END_VAR

VAR_OUTPUT
    OutputSignal : ARRAY[1..64] OF REAL; // Output signal array
END_VAR

VAR
    // Temporary variables for FFT computation
    TwiddleFactors : ARRAY[1..64] OF REAL; // Precomputed twiddle factors
    BitReversedOrder : ARRAY[1..64] OF INT; // Bit-reversed order array
    Stage : INT; // Current stage of FFT
    Bit : INT; // Current bit position
    Index : INT; // Current index
    Temp : REAL; // Temporary variable for butterfly computation
END_VAR

// Initialize twiddle factors and bit-reversed order array
PROCEDURE Initialize
VAR
    k : INT;
    n : INT;
    m : INT;
    p : INT;
    q : INT;
    r : INT;
    s : INT;
    t : INT;
    u : INT;
    v : INT;
    w : INT;
    x : INT;
    y : INT;
    z : INT;
END_VAR

// Bit-reversal reordering
PROCEDURE BitReversal
VAR
    i : INT;
    j : INT;
    k : INT;
    l : INT;
    m : INT;
    n : INT;
    o : INT;
    p : INT;
    q : INT;
    r : INT;
    s : INT;
    t : INT;
    u : INT;
    v : INT;
    w : INT;
    x : INT;
    y : INT;
    z : INT;
END_VAR

// Butterfly computation
PROCEDURE Butterfly
VAR
    i : INT;
    j : INT;
    k : INT;
    l : INT;
    m : INT;
    n : INT;
    o : INT;
    p : INT;
    q : INT;
    r : INT;
    s : INT;
    t : INT;
    u : INT;
