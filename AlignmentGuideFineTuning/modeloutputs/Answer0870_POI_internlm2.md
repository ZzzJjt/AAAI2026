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
	•	Includes comments and documentation for easy understanding and maintenance

**Spline Interpolation:**

Cubic spline interpolation is a method for approximating a smooth curve through a set of data points. It is particularly useful in applications where a smooth curve is desired, such as motion control or sensor smoothing. The spline is constructed by fitting a cubic polynomial to each segment between consecutive data points, ensuring a smooth transition between them.

The process of constructing a cubic spline involves several steps:

1. **Data Preprocessing:** The given data points (X, Y) are sorted in ascending order of X. This ensures that the spline is monotonically increasing, which is a requirement for the algorithm to work correctly.

2. **Spline Coefficient Calculation:** For each segment between consecutive data points, the cubic spline coefficients (A, B, C, D) are calculated using the following formulas:

   A[i] = Y[i]
   B[i] = 3 * (Y[i+1] - Y[i]) / (X[i+1] - X[i])
   C[i] = 3 * (Y[i] - Y[i+1]) / (X[i] - X[i+1])
   D[i] = Y[i+1] - Y[i] - B[i] * (X[i+1] - X[i]) - C[i] * (X[i] - X[i+1])

   These coefficients are used to evaluate the spline at any x-value within the segment.

3. **Spline Evaluation:** To interpolate a value at a given x-value (TargetX), the function block identifies the correct interval for TargetX between X[i] and X[i+1]. It then uses the precomputed spline coefficients to evaluate the spline at TargetX:

   InterpolatedY = A[i] + B[i](x - X[i]) + C[i](x - X[i])^2 + D[i](x - X[i])^3

   This process is repeated for each segment until the correct interpolated value is found.

4. **Boundary Conditions:** The function block should handle boundary conditions and extrapolation safely. This can be achieved by checking if TargetX is within the range of X[i] and X[i+1]. If it is not, the function block can either return the nearest boundary value or extrapolate the spline beyond the given data points.

5. **Efficiency
