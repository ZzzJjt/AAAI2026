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

**Solution:**

```
// Structured Text

FUNCTION KalmanFilter(
    // Inputs
    MeasuredPosition : REAL,
    Q : REAL,
    R : REAL,
    DeltaT : REAL,
    Reset : BOOL,
    PreviousPosition : REAL,
    EstimatedPosition : REAL,
    EstimatedVelocity : REAL,
    ErrorCovariance : REAL,
    KalmanGain : REAL,
    // Outputs
    UpdatedPosition : REAL,
    UpdatedVelocity : REAL
)

VAR
    PredictedPosition : REAL;
    PredictedVelocity : REAL;
    ErrorCovariancePredict : REAL;
    ErrorCovarianceUpdate : REAL;
    KalmanGainPredict : REAL;
    KalmanGainUpdate : REAL;
    PredictedErrorCovariance : REAL;
    UpdatedErrorCovariance : REAL;
    UpdatedKalmanGain : REAL;

BEGIN
    // Prediction step
    IF Reset = TRUE THEN
        PredictedPosition := MeasuredPosition;
        PredictedVelocity := 0;
    ELSE
        PredictedPosition := EstimatedPosition + PredictedVelocity * DeltaT;
        PredictedVelocity := EstimatedVelocity + (Q / DeltaT) * DeltaT;

    // Update step
    ErrorCovariancePredict := (R + Q) / (1 + KalmanGainPredict * KalmanGainUpdate);
    PredictedErrorCovariance := ErrorCovariance * ErrorCovariancePredict * ErrorCovariancePredict;
    UpdatedErrorCovariance := PredictedErrorCovariance + ErrorCovarianceUpdate;
    UpdatedKalmanGain := ErrorCovariancePredict / UpdatedErrorCovariance;

    // Update position and velocity
    UpdatedPosition := MeasuredPosition + UpdatedKalmanGain * (MeasuredPosition - PredictedPosition);
    UpdatedVelocity := UpdatedVelocity + UpdatedKalmanGain * (MeasuredPosition - PreviousPosition);
    PreviousPosition := MeasuredPosition;

    // Store updated values
    EstimatedPosition := UpdatedPosition;
    EstimatedVelocity := UpdatedVelocity;
    ErrorCovariance := UpdatedErrorCovariance;
    KalmanGain := UpdatedKalmanGain;

    // Return updated values
    RETURN UpdatedPosition, UpdatedVelocity;
END_FUNCTION
```

This function block implements a simple, scalar-based discrete-time Kalman filter
