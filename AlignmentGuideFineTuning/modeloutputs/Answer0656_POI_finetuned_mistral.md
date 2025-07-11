### Intent:
**Intent Summary:**  
Implement a heap sort algorithm in IEC 61131-3 Structured Text as a reusable function block for sorting integer arrays on a PLC, with phased execution to ensure real-time safety and deterministic behavior.

### Prompt:
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing a Kalman filter function block in IEC 61131-3 Structured Text for real-time state estimation of an autonomous vehicle’s position and velocity on a PLC.

⸻

🟩 I (Input) – Information Provided

You are tasked with implementing a discrete-time Kalman filter that:
	•	Estimates position and velocity based on noisy position measurements
	•	Accepts configurable parameters including:
	•	Process noise covariance (Q)
	•	Measurement noise covariance (R)
	•	Sample time (DeltaT)
	•	Initial position and velocity
	•	Must be written in Structured Text without matrix libraries
	•	Should be modular and suitable for scan-cycle-based PLC execution

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with inputs:
	•	MeasuredPosition : REAL
	•	Q, R : REAL (noise covariances)
	•	DeltaT : REAL (sample time)
	•	Reset : BOOL
	2.	Internally store:
	•	Estimated position (x_est_pos) and velocity (x_est_vel)
	•	Previous position (x_est_prev)
	•	Error covariance (p)
	•	Kalman gain (k)
	3.	Implement the prediction step:
	•	Predict new position based on current velocity
	•	Update error covariance with Q
	4.	Implement the correction step:
	•	Compute Kalman gain
	•	Update position with measurement
	•	Estimate velocity based on position change
	•	Update error covariance with R
	5.	Add reset logic and initialize all states on Reset = TRUE
	6.	Ensure the block executes within one scan cycle with safe real-time behavior

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a modular, scan-safe Kalman filter function block that provides accurate and noise-tolerant estimates of an autonomous vehicle’s position and velocity. The block should be easily reusable, configurable via Q and R, and ready for integration into industrial motion control systems on PLC hardware.

### Generated Code:
**Intent Summary:**  
Implement a heap sort algorithm in IEC 61131-3 Structured Text as a reusable function block for sorting integer arrays on a PLC, with phased execution to ensure real-time safety and deterministic behavior.
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer developing a Kalman filter function block in IEC 61131-3 Structured Text for real-time state estimation of an autonomous vehicle’s position and velocity on a PLC.

⸻

🟩 I (Input) – Information Provided

You are tasked with implementing a discrete-time Kalman filter that:
	•	Estimates position and velocity based on noisy position measurements
	•	Accepts configurable parameters including:
	•	Process noise covariance (Q)
	•	Measurement noise covariance (R)
	•	Sample time (DeltaT)
	•	Initial position and velocity
	•	Must be written in Structured Text without matrix libraries
	•	Should be modular and suitable for scan-cycle-based PLC execution

⸻

🟧 S (Steps) – Steps to Perform
	1.	Define the function block interface with inputs:
	•	MeasuredPosition : REAL
	•	Q, R : REAL (noise covariances)
	•	DeltaT : REAL (sample time)
	•	Reset : BOOL
	2.	Internally store:
	•	Estimated position (x_est_pos) and velocity (x_est_vel)
	•	Previous position (x_est_prev)
	•	Error covariance (p)
	•	Kalman gain (k)
	3.	Implement the prediction step:
	•	Predict new position based on current velocity
	•	Update error covariance with Q
	4.	Implement the correction step:
	•	Compute Kalman gain
	•	Update position with measurement
	•	Estimate velocity based on position change
	•	Update error covariance with R
	5.	Add reset logic and initialize all states on Reset = TRUE
	6.	Ensure the block executes within one scan cycle with safe real-time behavior

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a modular, scan-safe Kalman filter function block that provides accurate and noise-tolerant estimates of an autonomous vehicle’s position and velocity. The block should be easily reusable, configurable via Q and R, and ready for integration into industrial motion control systems on PLC hardware.
FUNCTION_BLOCK HeapSort
VAR_INPUT
    InputArray : ARRAY[1..100] OF INT; // Input array to be sorted
END_VAR

VAR_OUTPUT
    SortedArray : ARRAY[1..100] OF INT; // Sorted array output
END_VAR

VAR
    HeapSize : INT := 100; // Total number of elements in the heap
    i : INT;
    j : INT;
    Temp : INT;
    Parent : INT;
    Child : INT;
    MaxIndex : INT;
    Swap : BOOL;
    Phase : INT := 0; // Phase control for execution
END_VAR

METHOD Execute;
BEGIN
    CASE Phase OF
        0: // Initialize
            FOR i := 1 TO HeapSize DO
                SortedArray[i] := InputArray[i];
            END_FOR;
            Phase := 1; // Move to build heap phase
        1: // Build Heap
            FOR i := HeapSize / 2 DOWNTO 1 BY -1 DO
                Parent := i;
                Child := 2 * Parent;
                WHILE Child <= HeapSize DO
                    IF Child < HeapSize AND SortedArray[Child] < SortedArray[Child + 1] THEN
                        Child := Child + 1;
                    ELSIF SortedArray[Parent] < SortedArray[Child] THEN
                        Swap := TRUE;
                        Temp := SortedArray[Parent];
                        SortedArray[Parent] := SortedArray[Child];
                        SortedArray[Child] := Temp;
                        Parent := Child;
                        Child := 2 * Parent;
                    ELSE
                        Swap := FALSE;
                        EXIT;
                    END_IF;
                END_WHILE;
                IF NOT Swap THEN
                    EXIT;
                END_IF;
            END_WHILE;
            Phase := 2; // Move to sort phase
        2: // Sort
            FOR i := HeapSize DOWNTO 2 BY -1 DO
                Temp := SortedArray[1];
