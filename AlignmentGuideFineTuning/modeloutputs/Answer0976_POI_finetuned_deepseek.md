### Intent:
**Intent Summary:**  
Create a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate an autonomous vehicle's position and velocity using noisy sensor data, with configurable noise parameters and scan-cycle-safe execution.  

*(Focus: Discrete-time scalar implementation, modularity, and industrial applicability.)*

### Prompt:
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**T-A-G:**

🟥 T (Task)

Design a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate the position and velocity of an autonomous transport vehicle using noisy sensor input.

⸻

🟩 A (Action)
	•	Implement a discrete-time, 2-state Kalman filter using only scalar arithmetic, avoiding matrix operations or recursion
	•	Accept configurable inputs:
	•	MeasuredPosition : REAL
	•	Q : REAL – process noise covariance
	•	R : REAL – measurement noise covariance
	•	DeltaT : REAL – sample time
	•	Reset : BOOL – to reinitialize state
	•	Internally manage variables for:
	•	Estimated position and velocity
	•	Previous position (for velocity update)
	•	Error covariance and Kalman gain
	•	Perform prediction and update steps each scan cycle
	•	Add clear comments for each stage of the algorithm to support maintainability and clarity

⸻

🟦 G (Goal)

Deliver a modular, scan-cycle-safe function block that produces reliable estimates of position and velocity despite measurement noise. The block should be easy to configure, integrate into motion control logic, and adaptable for various autonomous or mobile platform applications.

### Generated Code:
**Intent Summary:**  
Create a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate an autonomous vehicle's position and velocity using noisy sensor data, with configurable noise parameters and scan-cycle-safe execution.  

*(Focus: Discrete-time scalar implementation, modularity, and industrial applicability.)*
**Kalman Filter:**
Implement a self-contained function block in IEC 61131-3 structured text to create a Kalman filter for estimating the position and velocity of an autonomous transport vehicle. Include configurable parameters for noise covariance and initial conditions.

**T-A-G:**

🟥 T (Task)

Design a self-contained Kalman filter function block in IEC 61131-3 Structured Text to estimate the position and velocity of an autonomous transport vehicle using noisy sensor input.

⸻

🟩 A (Action)
	•	Implement a discrete-time, 2-state Kalman filter using only scalar arithmetic, avoiding matrix operations or recursion
	•	Accept configurable inputs:
	•	MeasuredPosition : REAL
	•	Q : REAL – process noise covariance
	•	R : REAL – measurement noise covariance
	•	DeltaT : REAL – sample time
	•	Reset : BOOL – to reinitialize state
	•	Internally manage variables for:
	•	Estimated position and velocity
	•	Previous position (for velocity update)
	•	Error covariance and Kalman gain
	•	Perform prediction and update steps each scan cycle
	•	Add clear comments for each stage of the algorithm to support maintainability and clarity

⸻

🟦 G (Goal)

Deliver a modular, scan-cycle-safe function block that produces reliable estimates of position and velocity despite measurement noise. The block should be easy to configure, integrate into motion control logic, and adaptable for various autonomous or mobile platform applications.
FUNCTION_BLOCK KalmanFilter
VAR_INPUT
    MeasuredPosition : REAL; // Current position (m)
    Q : REAL; // Process noise covariance (1/s²)
    R : REAL; // Measurement noise covariance (1/m²)
    DeltaT : REAL; // Sample time (s)
    Reset : BOOL; // Reset flag (TRUE to reset state)
END_VAR

VAR_OUTPUT
    EstimatedPosition : REAL; // Estimated position (m)
    EstimatedVelocity : REAL; // Estimated velocity (m/s)
    Covariance : REAL; // Estimated error covariance
    KalmanGain : REAL; // Kalman gain
END_VAR

VAR
    // Internal state variables
    PreviousPosition : REAL; // Previous estimated position
    PreviousVelocity : REAL; // Previous estimated velocity
    PredictedPosition : REAL; // Predicted position
    PredictedVelocity : REAL; // Predicted velocity
    ErrorCovariance : REAL; // Error covariance
    KalmanGain : REAL; // Kalman gain
    PredictionError : REAL; // Prediction error
    MeasurementError : REAL; // Measurement error
    DeltaT : REAL; // Sample time
END_VAR

// Initialize state variables
PreviousPosition := MeasuredPosition;
PreviousVelocity := 0.0;
ErrorCovariance := Q;
KalmanGain := 1.0;

// Prediction step
PredictedPosition := PreviousPosition + PreviousVelocity * DeltaT;
PredictedVelocity := PreviousVelocity;
PredictionError := 0.0;

// Update step
MeasurementError := (MeasuredPosition - PredictedPosition) / DeltaT;
KalmanGain := ErrorCovariance * R;

// Update state variables
EstimatedPosition := PredictedPosition + KalmanGain * MeasurementError;
EstimatedVelocity := (MeasuredPosition - PreviousPosition) / DeltaT;
ErrorCovariance := (1.0 - KalmanGain) * ErrorCovariance;
PreviousPosition := EstimatedPosition;
PreviousVelocity := EstimatedVelocity;

// Reset state on reset
IF Reset THEN
    EstimatedPosition := 0.0;
    EstimatedVelocity := 0.0;
    ErrorCovariance := Q;
    KalmanGain := 1.0;
END_IF;
END_FUNCTION_BLOCK

// Example usage:
// MeasuredPosition
