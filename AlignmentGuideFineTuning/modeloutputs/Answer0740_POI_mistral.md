### Intent:
**Intent Summary:**  
Create a Structured Text function block for cubic spline interpolation that efficiently computes smooth values between given data points in real-time PLC applications, with precomputed coefficients and thorough documentation.

### Prompt:
**Spline Interpolation:**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute spline interpolation over a set of data points. Ensure that the function block is modular and efficient, with comments explaining the steps involved in constructing and evaluating the spline. Address potential computational challenges, such as memory usage and processing time, and discuss the advantages of spline interpolation in comparison to linear methods, particularly in applications where smooth curve fitting is essential.

**R-T-F:**

🟥 R (Role) – Your Role

You are a control systems developer or PLC programmer tasked with building a high-precision interpolation utility for real-time control systems using IEC 61131-3 Structured Text. Your role is to create a function block that can perform spline interpolation efficiently and accurately in a resource-constrained PLC environment.

⸻

🟩 T (Task) – What You Need to Do

Develop a modular and efficient function block called SplineInterpolator that:
	•	Performs cubic spline interpolation over a set of known data points
	•	Accepts the following inputs:
	•	X : ARRAY[1..N] OF REAL — known x-values
	•	Y : ARRAY[1..N] OF REAL — known y-values
	•	TargetX : REAL — x-position where the interpolated value is desired
	•	Returns the following output:
	•	InterpolatedY : REAL — the spline-interpolated result at TargetX

You should also:
	•	Implement logic to:
	•	Locate the correct interval [X[i], X[i+1]] for TargetX
	•	Use precomputed spline coefficients (a, b, c, d)
	•	Evaluate the cubic polynomial for that segment
	•	Comment thoroughly to explain:
	•	The mathematical foundation of cubic splines
	•	How runtime evaluation is kept efficient
	•	Any assumptions made (e.g. natural spline, clamped boundaries, etc.)
	•	Address computational considerations:
	•	Minimize memory by storing only necessary coefficients
	•	Avoid real-time coefficient solving—prepare data during initialization

⸻

🟧 F (Format) – Expected Output

Your final function block should consist of:
	•	IEC 61131-3 Structured Text code for real-time evaluation:
 InterpolatedY := A[i] + B[i]*(TargetX - X[i]) + C[i]*(TargetX - X[i])**2 + D[i]*(TargetX - X[i])**3;
 	•	Inline documentation covering:
	•	How and where spline coefficients should be calculated
	•	Strategies for extending or limiting input arrays
	•	Warnings about performance on low-power PLCs
	•	Use cases such as:
	•	Smooth actuator movement
	•	Sensor calibration curves
	•	Profile control in batch processes

### Generated Code:
**Intent Summary:**  
Create a Structured Text function block for cubic spline interpolation that efficiently computes smooth values between given data points in real-time PLC applications, with precomputed coefficients and thorough documentation.
**Spline Interpolation:**

Develop a self-contained function block in IEC 61131-3 Structured Text to compute spline interpolation over a set of data points. Ensure that the function block is modular and efficient, with comments explaining the steps involved in constructing and evaluating the spline. Address potential computational challenges, such as memory usage and processing time, and discuss the advantages of spline interpolation in comparison to linear methods, particularly in applications where smooth curve fitting is essential.

**R-T-F:**

🟥 R (Role) – Your Role

You are a control systems developer or PLC programmer tasked with building a high-precision interpolation utility for real-time control systems using IEC 61131-3 Structured Text. Your role is to create a function block that can perform spline interpolation efficiently and accurately in a resource-constrained PLC environment.

⸻

🟩 T (Task) – What You Need to Do

Develop a modular and efficient function block called SplineInterpolator that:
	•	Performs cubic spline interpolation over a set of known data points
	•	Accepts the following inputs:
	•	X : ARRAY[1..N] OF REAL — known x-values
	•	Y : ARRAY[1..N] OF REAL — known y-values
	•	TargetX : REAL — x-position where the interpolated value is desired
	•	Returns the following output:
	•	InterpolatedY : REAL — the spline-interpolated result at TargetX

You should also:
	•	Implement logic to:
	•	Locate the correct interval [X[i], X[i+1]] for TargetX
	•	Use precomputed spline coefficients (a, b, c, d)
	•	Evaluate the cubic polynomial for that segment
	•	Comment thoroughly to explain:
	•	The mathematical foundation of cubic splines
	•	How runtime evaluation is kept efficient
	•	Any assumptions made (e.g. natural spline, clamped boundaries, etc.)
	•	Address computational considerations:
	•	Minimize memory by storing only necessary coefficients
	•	Avoid real-time coefficient solving—prepare data during initialization

⸻

🟧 F (Format) – Expected Output

Your final function block should consist of:
	•	IEC 61131-3 Structured Text code for real-time evaluation:
 InterpolatedY := A[i] + B[i]*(TargetX - X[i]) + C[i]*(TargetX - X[i])**2 + D[i]*(TargetX - X[i])**3;
 	•	Inline documentation covering:
	•	How and where spline coefficients should be calculated
	•	Strategies for extending or limiting input arrays
	•	Warnings about performance on low-power PLCs
	•	Use cases such as:
	•	Smooth actuator movement
	•	Sensor calibration curves
	•	Profile control in batch processes
	•	A brief comparison of spline interpolation with linear interpolation

⸻

🟦 C (Context) – Important Details

The function block should be designed for use in real-time PLC applications, where memory and processing power are limited. The function block should be able to handle a variable number of data points (N) and should be able to interpolate values smoothly and accurately.

The function block should be designed to work with cubic splines, which are known for their ability to provide smooth interpolation while minimizing oscillations. The spline should be a natural spline, meaning that the first and last derivatives are continuous but the second derivative is not necessarily continuous at the endpoints.

The function block should be able to handle clamped boundary conditions, where the spline is forced to pass through the first and last data points. This can be achieved by setting the first and last spline coefficients (A[0], B[0], C[0], D[0]) and (A[N], B[N], C[N], D[N]) to specific values based on the boundary conditions.

The function block should be designed to minimize memory usage by storing only the necessary coefficients (A, B, C, D) for each segment. The coefficients can be precomputed during initialization and stored in arrays for efficient runtime evaluation.

The function block should be designed to avoid real-time coefficient solving, as this can be computationally expensive and may not be feasible in a real-time PLC environment. Instead, the coefficients should be precomputed during initialization based on the given data points.

The function block should be designed to handle cases where the number of data points (N) is small, as this can lead to poor interpolation results. In such cases, the function block should provide a warning and suggest using a larger number of data points for better results.

The function block should be designed to handle cases where the number of data points (N) is large, as this can lead to increased memory usage and longer processing times. In such cases, the function block should provide a warning and suggest using a smaller number of data points for better performance.

The function block should be designed to handle cases where the input arrays (X and Y) are not sorted, as this can lead to incorrect interpolation results. In such cases, the function block should provide a
