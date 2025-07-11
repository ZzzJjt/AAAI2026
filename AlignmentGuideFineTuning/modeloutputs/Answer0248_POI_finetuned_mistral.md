### Intent:
**Intent Summary:**  
Develop safety interlocks for a subsea wellhead system that automatically triggers shutdowns when pressure, temperature, or flow rates exceed safe limits, with manual reset functionality.  

*(Focus: Automated safety shutdowns with process monitoring and fail-safe reset logic.)*

### Prompt:
**Interlock Prilling Station:**

Develop a complete list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should cover critical safety and operational aspects to ensure the safe and efficient operation of the prilling process. Discuss the importance of implementing these interlocks in ammonium nitrate production for both safety and compliance with regulatory standards.

**C-A-R-E:**

🟥 C (Context) – The Background

Ammonium nitrate prilling stations involve the transformation of molten ammonium nitrate into solid prills using a controlled environment involving high temperatures, melt handling, and air cooling. Due to the explosive nature of ammonium nitrate and strict safety regulations, any failure in process control or equipment must be rapidly detected and mitigated. This requires a well-structured interlock system that ensures both personnel safety and regulatory compliance.

⸻

🟩 A (Action) – The Implementation Task

Develop a comprehensive list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should address both safety-critical and process-critical events. For each interlock, define the triggering condition and associated automated response. Interlocks should include:
	•	Overtemperature Interlock – Shut down the prill tower if temperatures exceed operational limits
	•	High Pressure Interlock – Open relief paths or shut down pumps
	•	Low Cooling Air Flow Interlock – Halt melt feed if airflow is insufficient
	•	High Product Level Interlock – Stop production if prill accumulation exceeds safe levels
	•	Pump or Feeder Failure Interlock – Shut down prilling head if melt flow is lost
	•	Scrubber Failure Interlock – Stop emissions source if scrubber malfunctions
	•	Emergency Stop Interlock – Manual shutdown of entire system during critical events
	•	Inerting Gas Loss Interlock – Stop all processes relying on inert gas for explosion prevention

Each interlock should be built using fail-safe logic, integrated into the control system, and capable of being latched until reset conditions are verified.

⸻

🟨 R (Result) – The Expected Outcome

This interlock system ensures that any unsafe or abnormal condition leads to a predictable and safe system response, avoiding equipment damage, fire, explosion, or regulatory violations. It provides an automated safety net that reduces reliance on human intervention and enhances operator confidence in process safety systems.

⸻

🟦 E (Example) – A Practical Use Case

If the cooling air fan fails, the system automatically halts melt feed and disables the prilling head to prevent overheating and uncontrolled prill formation. Simultaneously, an alarm notifies the operator, and the system remains shut down until airflow is restored and manually verified. Similarly, if pressure in the melt system exceeds 12 bar, a high-pressure interlock opens a relief valve and shuts down the pump, preventing rupture or downstream damage.

### Generated Code:
**Intent Summary:**  
Develop safety interlocks for a subsea wellhead system that automatically triggers shutdowns when pressure, temperature, or flow rates exceed safe limits, with manual reset functionality.  

*(Focus: Automated safety shutdowns with process monitoring and fail-safe reset logic.)*
**Interlock Prilling Station:**

Develop a complete list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should cover critical safety and operational aspects to ensure the safe and efficient operation of the prilling process. Discuss the importance of implementing these interlocks in ammonium nitrate production for both safety and compliance with regulatory standards.

**C-A-R-E:**

🟥 C (Context) – The Background

Ammonium nitrate prilling stations involve the transformation of molten ammonium nitrate into solid prills using a controlled environment involving high temperatures, melt handling, and air cooling. Due to the explosive nature of ammonium nitrate and strict safety regulations, any failure in process control or equipment must be rapidly detected and mitigated. This requires a well-structured interlock system that ensures both personnel safety and regulatory compliance.

⸻

🟩 A (Action) – The Implementation Task

Develop a comprehensive list of interlocks required for a prilling station handling ammonium nitrates. The interlocks should address both safety-critical and process-critical events. For each interlock, define the triggering condition and associated automated response. Interlocks should include:
	•	Overtemperature Interlock – Shut down the prill tower if temperatures exceed operational limits
	•	High Pressure Interlock – Open relief paths or shut down pumps
	•	Low Cooling Air Flow Interlock – Halt melt feed if airflow is insufficient
	•	High Product Level Interlock – Stop production if prill accumulation exceeds safe levels
	•	Pump or Feeder Failure Interlock – Shut down prilling head if melt flow is lost
	•	Scrubber Failure Interlock – Stop emissions source if scrubber malfunctions
	•	Emergency Stop Interlock – Manual shutdown of entire system during critical events
	•	Inerting Gas Loss Interlock – Stop all processes relying on inert gas for explosion prevention

Each interlock should be built using fail-safe logic, integrated into the control system, and capable of being latched until reset conditions are verified.

⸻

🟨 R (Result) – The Expected Outcome

This interlock system ensures that any unsafe or abnormal condition leads to a predictable and safe system response, avoiding equipment damage, fire, explosion, or regulatory violations. It provides an automated safety net that reduces reliance on human intervention and enhances operator confidence in process safety systems.

⸻

🟦 E (Example) – A Practical Use Case

If the cooling air fan fails, the system automatically halts melt feed and disables the prilling head to prevent overheating and uncontrolled prill formation. Simultaneously, an alarm notifies the operator, and the system remains shut down until airflow is restored and manually verified. Similarly, if pressure in the melt system exceeds 12 bar, a high-pressure interlock opens a relief valve and shuts down the pump, preventing rupture or downstream damage.
FUNCTION_BLOCK FB_SubseaWellheadShutdown
VAR_INPUT
    Execute : BOOL; // Trigger shutdown on rising edge
    Pressure_PV : REAL; // Measured wellhead pressure (bar)
    Temp_PV : REAL; // Measured wellhead temperature (°C)
    Flow_PV : REAL; // Measured flow rate (m³/h)
END_VAR

VAR_OUTPUT
    Shutdown : BOOL; // TRUE when shutdown is triggered
    Reset : BOOL; // TRUE when manual reset is required
    Error : BOOL; // TRUE if shutdown cannot be executed
    ErrorMessage : STRING(255); // Detailed error message
END_VAR

VAR
    Pressure_High_Limit : REAL := 150.0; // High pressure limit (bar)
    Temp_High_Limit : REAL := 120.0; // High temperature limit (°C)
    Flow_High_Limit : REAL := 1000.0; // High flow rate limit (m³/h)
    Shutdown_Executed : BOOL := FALSE; // Flag to track shutdown execution
    Reset_Required : BOOL := FALSE; // Flag to track manual reset
    Error_Occurred : BOOL := FALSE; // Flag to track error conditions
END_VAR

// Main logic block
IF Execute THEN
    // Check for high pressure, temperature, or flow conditions
    IF Pressure_PV > Pressure_High_Limit OR Temp_PV > Temp_High_Limit OR Flow_PV > Flow_High_Limit THEN
        // Trigger shutdown and set error flag
        Shutdown := TRUE;
        Error_Occurred := TRUE;
        ErrorMessage := 'Pressure, temperature, or flow exceeded safe limits';
    ELSE
        // No safety conditions triggered, reset outputs
        Shutdown := FALSE;
        Reset_Required := FALSE;
        Error_Occurred := FALSE;
        ErrorMessage := '';
    END_IF;
ELSE
    // No shutdown requested, reset outputs
    Shutdown := FALSE;
    Reset_Required := FALSE;
    Error_Occurred
