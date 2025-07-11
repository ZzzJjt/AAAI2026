### Intent:
**Intent Summary:**  
Develop a cause-and-effect matrix linking hazardous process conditions (e.g., overpressure, sensor failures) to safety actions (e.g., valve closure, alarms) in a chemical reactor, ensuring automated risk mitigation and operational safety.  

*(For code generation: Map process deviations to predefined actuator responses in a safety interlock system.)*

### Prompt:
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a cause and effect matrix for the interlock system of a chemical reactor.

⸻

🟩 A (Action) – How to Do It

Create a matrix where:

	•	Each row represents a specific cause, such as abnormal sensor readings (e.g., high pressure, low level, or high temperature).
	•	Each column represents a specific effect, such as triggering an alarm, stopping a pump, closing a valve, or shutting down a heater.

Populate the matrix to show how each hazardous condition leads to one or more predefined safety actions. After the matrix is completed, write a detailed explanation discussing how each interlock response helps mitigate risk, protect equipment, and maintain reactor stability. Highlight the importance of using this matrix as a clear, traceable tool in safety system design.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a structured, visual tool that links potential process hazards with protective actions. This matrix will enhance operational safety, simplify interlock validation, and serve as a vital reference for engineers, operators, and auditors responsible for the safe functioning of the chemical reactor.

### Generated Code:
**Intent Summary:**  
Develop a cause-and-effect matrix linking hazardous process conditions (e.g., overpressure, sensor failures) to safety actions (e.g., valve closure, alarms) in a chemical reactor, ensuring automated risk mitigation and operational safety.  

*(For code generation: Map process deviations to predefined actuator responses in a safety interlock system.)*
**Interlock Cause & Effect Matrix:**

Develop a cause and effect matrix for the interlocks required in a chemical reactor system. Each row should represent a specific cause linked to sensor values such as pressure, temperature, or level, while each column should represent the corresponding effect related to actuator actions such as closing valves, stopping pumps, or triggering alarms. Once the matrix is complete, write a detailed explanation of how these interlocks ensure the safety and stability of the reactor operation. Discuss how each interlock action prevents hazardous conditions and safeguards the equipment during abnormal process situations.

**T-A-G:**

🟥 T (Task) – What You Need to Do

Develop a cause and effect matrix for the interlock system of a chemical reactor.

⸻

🟩 A (Action) – How to Do It

Create a matrix where:

	•	Each row represents a specific cause, such as abnormal sensor readings (e.g., high pressure, low level, or high temperature).
	•	Each column represents a specific effect, such as triggering an alarm, stopping a pump, closing a valve, or shutting down a heater.

Populate the matrix to show how each hazardous condition leads to one or more predefined safety actions. After the matrix is completed, write a detailed explanation discussing how each interlock response helps mitigate risk, protect equipment, and maintain reactor stability. Highlight the importance of using this matrix as a clear, traceable tool in safety system design.

⸻

🟦 G (Goal) – What You Want to Achieve

Create a structured, visual tool that links potential process hazards with protective actions. This matrix will enhance operational safety, simplify interlock validation, and serve as a vital reference for engineers, operators, and auditors responsible for the safe functioning of the chemical reactor.
### Safety Interlock Logic for Chemical Reactor

#### 1. Overpressure Protection
- **Cause**: Pressure sensor detects a pressure above the maximum safe limit (e.g., 15 bar).
- **Effect**: Close the feed valve (FV-101) to stop the inflow of reactants.

```
IF Pressure > 15.0 THEN
    FeedValve.Close();
END_IF;
```

#### 2. Low-Level Protection
- **Cause**: Level sensor detects a level below the minimum safe limit (e.g., 50%).
- **Effect**: Open the make-up valve (MU-101) to maintain the minimum liquid level.

```
IF Level < 0.5 THEN
    MakeupValve.Open();
END_IF;
```

#### 3. High-Temperature Protection
- **Cause**: Temperature sensor detects a temperature above the maximum safe limit (e.g., 120°C).
- **Effect**: Open the cooling water valve (CW-101) to cool the reactor.

```
IF Temperature > 120.0 THEN
    CoolingWaterValve.Open();
END_IF;
```

#### 4. Sensor Failure Protection
- **Cause**: A sensor fails or becomes unresponsive.
- **Effect**: Trigger an alarm (ALARM-101) and shut down the reactor (REACTOR.Shutdown()).

```
IF SensorFault THEN
    ALARM_101(TRUE);
    REACTOR.Shutdown();
END_IF;
```

#### 5. Manual Shutdown Interlock
- **Cause**: Operator manually triggers a shutdown.
- **Effect**: Shut down the reactor and close all feed and makeup valves.

```
IF ManualShutdown THEN
    REACTOR.Shutdown();
    FeedValve.Close();
    MakeupValve.Close();
END_IF;
```

### Explanation

Each interlock is designed
