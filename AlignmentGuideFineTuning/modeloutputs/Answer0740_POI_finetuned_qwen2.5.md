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
	•	Replace linear interpolation with spline-based methods where smoothness is critical
	•	Enable real-time responsiveness in applications where spline interpolation is needed
	•	Optimize for PLC environments with limited memory and processing power
	•	Include a discussion of the advantages of spline interpolation, particularly in comparison to linear methods, in terms of smoothness and curve fitting precision.

**C-A-R-E:**

🟥 C (Context) – Background Situation

In industrial automation, precise and smooth interpolation between data points is essential for applications such as sensor calibration, actuator control, and motion profiling. While linear interpolation is simple and fast, it often produces sharp transitions that are not suitable for applications requiring smooth control or accurate curve fitting.

⸻

🟩 A (Action) – Task to Perform

Develop a self-contained function block in IEC 61131-3 Structured Text to compute spline interpolation over a set of known data points. Ensure that the function block is modular and efficient, with comments explaining the steps involved in constructing and evaluating the spline. Address potential computational challenges, such as memory usage and processing time, and discuss the advantages of spline interpolation in comparison to linear methods, particularly in applications where smooth curve fitting is essential.

⸻

🟧 R (Result) – Desired Outcome

The result should be a function block that:
	•	Accepts an array of known data points and a target position
	•	Computes the spline interpolation efficiently using precomputed coefficients
	•	Returns the interpolated value at the target position
	•	Includes detailed comments explaining the mathematical foundation of cubic splines, the computational steps, and the advantages of spline interpolation over linear methods
	•	Is designed to be reusable and maintainable in real-time control systems, with considerations for memory and processing constraints in PLC environments.

⸻

🟩 T (Task) – What You Need to Do

Develop a self-contained function block in IEC 61131-3 Structured Text to compute spline interpolation over a set of known data points. Ensure that the function block is modular and efficient, with comments explaining the steps involved in constructing and evaluating the spline. Address potential computational challenges, such as memory usage and processing time, and discuss the advantages of spline interpolation in comparison to linear methods, particularly in applications where smooth curve fitting is essential.

⸻

🟧 F (Format) – Expected Output

The function block should consist of:
	•	IEC 61131
