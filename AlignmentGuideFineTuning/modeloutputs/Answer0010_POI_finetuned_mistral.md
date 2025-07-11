### Intent:
**Intent Summary:**  
Develop a model predictive control (MPC) system in C++ to optimize HVAC operations by dynamically adjusting heating, cooling, and humidity control based on real-time indoor conditions, weather forecasts, and occupancy patterns, while minimizing energy usage.  

*(Focus: MPC algorithm for HVAC control, energy efficiency, and comfort optimization.)*

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**B-A-B:**

🟥 B（Before）

In steel manufacturing, maintaining consistent product quality is challenging due to variability in factors like tensile strength, thickness, and surface finish. Without proper monitoring, these variations can lead to increased waste, product defects, and customer dissatisfaction.

🟩 A（After）

Develop a statistical process control (SPC) system using Python that monitors key quality metrics in real time, detects out-of-control conditions using control charts and statistical rules, and suggests corrective actions to maintain consistent, high-quality steel products with minimal waste.

🟧 B（Bridge）

Write Python code to simulate the steel manufacturing process and implement SPC tools such as X̄ and R charts, control limits, and trend analysis. Include logic for triggering alarms when variations exceed control thresholds, and suggest data-driven adjustments. Demonstrate how this system helps operators maintain quality and reduce process variability during production.

### Generated Code:
**Intent Summary:**  
Develop a model predictive control (MPC) system in C++ to optimize HVAC operations by dynamically adjusting heating, cooling, and humidity control based on real-time indoor conditions, weather forecasts, and occupancy patterns, while minimizing energy usage.  

*(Focus: MPC algorithm for HVAC control, energy efficiency, and comfort optimization.)*
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**B-A-B:**

🟥 B（Before）

In steel manufacturing, maintaining consistent product quality is challenging due to variability in factors like tensile strength, thickness, and surface finish. Without proper monitoring, these variations can lead to increased waste, product defects, and customer dissatisfaction.

🟩 A（After）

Develop a statistical process control (SPC) system using Python that monitors key quality metrics in real time, detects out-of-control conditions using control charts and statistical rules, and suggests corrective actions to maintain consistent, high-quality steel products with minimal waste.

🟧 B（Bridge）

Write Python code to simulate the steel manufacturing process and implement SPC tools such as X̄ and R charts, control limits, and trend analysis. Include logic for triggering alarms when variations exceed control thresholds, and suggest data-driven adjustments. Demonstrate how this system helps operators maintain quality and reduce process variability during production.
FUNCTION_BLOCK FB_MPC_HVAC_Control
VAR_INPUT
    // Inputs from indoor sensors
    Temp_Indoor : REAL; // Indoor temperature (°C)
    Humidity_Indoor : REAL; // Indoor humidity (%)
    Occupancy : BOOL; // Occupancy status

    // Inputs from weather forecast
    Temp_Forecast : REAL; // Predicted outdoor temperature (°C)
    Humidity_Forecast : REAL; // Predicted outdoor humidity (%)

    // Inputs from HVAC system
    Heater_Status : BOOL; // Heater status
    Cooler_Status : BOOL; // Cooler status
    Humidifier_Status : BOOL; // Humidifier status

    // Control parameters
    Delta_T : REAL := 1.0; // Desired temperature change (°C)
    Delta_H : REAL := 0.05; // Desired humidity change (%)
    Control_Horizon : INT := 120; // Prediction horizon (minutes)
    Simulation_Step : INT := 1; // Simulation step size (minutes)

    // Setpoint for indoor temperature and humidity
    Temp_Setpoint : REAL := 22.0; // Desired indoor temperature (°C)
    Humidity_Setpoint : REAL := 50.0; // Desired indoor humidity (%)

    // Control limits for SPC
    Temp_Upper_Limit : REAL := 25.0; // Upper control limit for temperature
    Temp_Lower_Limit : REAL := 20.0; // Lower control limit for temperature
    Humidity_Upper_Limit : REAL := 60.0; // Upper control limit for humidity
    Humidity_Lower_Limit : REAL := 40.0; // Lower control limit for humidity
END_VAR

VAR_OUTPUT
    // Outputs to HVAC system
    Heater_Setpoint : REAL; // Heater setpoint (°C)
    Cooler_Setpoint : REAL; // Cooler setpoint (°C)
    Humidifier_Setpoint : REAL;
