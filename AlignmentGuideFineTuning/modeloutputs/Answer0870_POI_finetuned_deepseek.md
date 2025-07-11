### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for cubic spline interpolation that smoothly fits data points, handles real-time constraints efficiently, and is suitable for motion control or sensor smoothing applications.  

*(Focus: Modularity, smooth curve fitting, and PLC-compatible implementation.)*

### Prompt:
**Spline Interpolation:**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute spline interpolation over a set of data points. Ensure that the function block is modular and efficient, with comments explaining the steps involved in constructing and evaluating the spline. Address potential computational challenges, such as memory usage and processing time, and discuss the advantages of spline interpolation in comparison to linear methods, particularly in applications where smooth curve fitting is essential.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained and reusable IEC 61131-3 Structured Text function block that performs spline interpolation on a set of known data points. This function should return a smooth, curve-fitted value for any specified input within the defined range.

⸻

🟩 A (Action) – How to Do It
	1.	Define a function block called SplineInterpolator with:
	•	Inputs:
	•	X : ARRAY[1..N] OF REAL – known x-values
	•	Y : ARRAY[1..N] OF REAL – corresponding y-values
	•	TargetX : REAL – the x-value at which to interpolate
	•	Output:
	•	InterpolatedY : REAL – the result of spline interpolation
	2.	Implement logic to perform cubic spline interpolation:
	•	Identify the correct interval for TargetX between X[i] and X[i+1]
	•	Use precomputed spline coefficients (A[i], B[i], C[i], D[i]) to evaluate:
InterpolatedY = A[i] + B[i](x - X[i]) + C[i](x - X[i])^2 + D[i](x - X[i])^3
	3.	Ensure the implementation is modular:
	•	Coefficients may be computed externally and passed in or initialized once
	•	Runtime logic is optimized for real-time scan cycles
	•	Add comments explaining the math and implementation decisions
	4.	Address challenges:
	•	Handle boundary conditions and extrapolation safely
	•	Use efficient logic for indexing and evaluating the correct segment
	•	Maintain precision without excessive memory or processing overhead

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a robust and efficient interpolation function block that:
	•	Outputs a smooth curve through all given data points
	•	Is ideal for applications such as:
	•	Motion trajectory planning
	•	Sensor data smoothing
	•	Profile-driven process control
	•	Operates predictably and safely within PLC real-time constraints
	•	Is reusable and adaptable to different array sizes and system needs

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block for cubic spline interpolation that smoothly fits data points, handles real-time constraints efficiently, and is suitable for motion control or sensor smoothing applications.  

*(Focus: Modularity, smooth curve fitting, and PLC-compatible implementation.)*
**Spline Interpolation:**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute spline interpolation over a set of data points. Ensure that the function block is modular and efficient, with comments explaining the steps involved in constructing and evaluating the spline. Address potential computational challenges, such as memory usage and processing time, and discuss the advantages of spline interpolation in comparison to linear methods, particularly in applications where smooth curve fitting is essential.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Create a self-contained and reusable IEC 61131-3 Structured Text function block that performs spline interpolation on a set of known data points. This function should return a smooth, curve-fitted value for any specified input within the defined range.

⸻

🟩 A (Action) – How to Do It
	1.	Define a function block called SplineInterpolator with:
	•	Inputs:
	•	X : ARRAY[1..N] OF REAL – known x-values
	•	Y : ARRAY[1..N] OF REAL – corresponding y-values
	•	TargetX : REAL – the x-value at which to interpolate
	•	Output:
	•	InterpolatedY : REAL – the result of spline interpolation
	2.	Implement logic to perform cubic spline interpolation:
	•	Identify the correct interval for TargetX between X[i] and X[i+1]
	•	Use precomputed spline coefficients (A[i], B[i], C[i], D[i]) to evaluate:
InterpolatedY = A[i] + B[i](x - X[i]) + C[i](x - X[i])^2 + D[i](x - X[i])^3
	3.	Ensure the implementation is modular:
	•	Coefficients may be computed externally and passed in or initialized once
	•	Runtime logic is optimized for real-time scan cycles
	•	Add comments explaining the math and implementation decisions
	4.	Address challenges:
	•	Handle boundary conditions and extrapolation safely
	•	Use efficient logic for indexing and evaluating the correct segment
	•	Maintain precision without excessive memory or processing overhead

⸻

🟦 G (Goal) – What You Want to Achieve

Deliver a robust and efficient interpolation function block that:
	•	Outputs a smooth curve through all given data points
	•	Is ideal for applications such as:
	•	Motion trajectory planning
	•	Sensor data smoothing
	•	Profile-driven process control
	•	Operates predictably and safely within PLC real-time constraints
	•	Is reusable and adaptable to different array sizes and system needs
FUNCTION_BLOCK SplineInterpolator
VAR_INPUT
    X : ARRAY[1..N] OF REAL; // Known x-values
    Y : ARRAY[1..N] OF REAL; // Corresponding y-values
    TargetX : REAL; // X-value to interpolate
END_VAR

VAR_OUTPUT
    InterpolatedY : REAL; // Result of spline interpolation
END_VAR

VAR
    i : INT; // Loop index
    A : ARRAY[1..N] OF REAL; // Precomputed spline coefficients
    B : ARRAY[1..N] OF REAL;
    C : ARRAY[1..N] OF REAL;
    D : ARRAY[1..N] OF REAL;
END_VAR

// Initialize coefficients
FOR i := 1 TO N DO
    A[i] := Y[i];
    B[i] := Y[i] - Y[i-1];
    C[i] := (Y[i] - Y[i-1]) * (Y[i] - Y[i-1]);
    D[i] := (Y[i] - Y[i-1]) * (Y[i] - Y[i-1]) * (Y[i] - Y[i-1]);
END_FOR

// Compute spline coefficients for target x
FOR i := 1 TO N DO
    IF X >= X[i] AND X <= X[i+1] THEN
        A[i] := A[i];
        B[i] := B[i];
        C[i] := C[i];
        D[i] := D[i];
    ELSE
        A[i] := 0.0;
        B[i] := 0.0;
        C[i] := 0.0;
        D[i] := 0.0;
    END_IF;
END_FOR

// Evaluate spline at target x
IF X >= X[1] AND X <= X[N] THEN
    InterpolatedY := A[1] + B[1](TargetX - X[1]) + C[1](TargetX - X[1])^2 + D[1](TargetX - X[1])^3;
ELSE
    Interpolated
