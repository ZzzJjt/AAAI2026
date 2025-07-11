### Intent:
**Intent Summary:**  
Develop a Python-based statistical process control (SPC) system to monitor steel manufacturing quality metrics (tensile strength, thickness, surface finish) using control charts, detect deviations, trigger alarms, and simulate corrective actions to reduce variability and defects.  

*(Focus: Real-time monitoring, anomaly detection, and process optimization via SPC tools in Python.)*

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-I-S-E:**

🟥 R（Role）

Act as a Python developer with expertise in quality control and industrial process monitoring systems.

🟩 I（Input）

You are tasked with developing a statistical process control (SPC) system for a steel manufacturing process. The system must track key quality metrics such as tensile strength, thickness, and surface finish in real time, detect process deviations using control charts, and trigger alarms with recommended corrective actions. The process is subject to variability and potential quality drift, which must be managed efficiently to ensure consistent output.

🟧 S（Steps）

	1.	Simulate the steel manufacturing process by generating real-time data for tensile strength, thickness, and surface finish.
 
	2.	Implement SPC tools in Python such as X̄ and R charts, control limit calculations, and rule-based detection of out-of-control conditions.
 
	3.	Design a logic system to trigger alarms when deviations are detected, and suggest data-driven corrective actions.
 
	4.	Evaluate system performance by demonstrating how early warnings and interventions reduce process variation and improve consistency.

🟦 E（Expectation）

The Python-based SPC system should enable early detection of quality issues, support timely corrective actions, and lead to reduced defect rates, more consistent product quality, and lower production waste in the steel manufacturing process.

### Generated Code:
**Intent Summary:**  
Develop a Python-based statistical process control (SPC) system to monitor steel manufacturing quality metrics (tensile strength, thickness, surface finish) using control charts, detect deviations, trigger alarms, and simulate corrective actions to reduce variability and defects.  

*(Focus: Real-time monitoring, anomaly detection, and process optimization via SPC tools in Python.)*
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-I-S-E:**

🟥 R（Role）

Act as a Python developer with expertise in quality control and industrial process monitoring systems.

🟩 I（Input）

You are tasked with developing a statistical process control (SPC) system for a steel manufacturing process. The system must track key quality metrics such as tensile strength, thickness, and surface finish in real time, detect process deviations using control charts, and trigger alarms with recommended corrective actions. The process is subject to variability and potential quality drift, which must be managed efficiently to ensure consistent output.

🟧 S（Steps）

	1.	Simulate the steel manufacturing process by generating real-time data for tensile strength, thickness, and surface finish.
 
	2.	Implement SPC tools in Python such as X̄ and R charts, control limit calculations, and rule-based detection of out-of-control conditions.
 
	3.	Design a logic system to trigger alarms when deviations are detected, and suggest data-driven corrective actions.
 
	4.	Evaluate system performance by demonstrating how early warnings and interventions reduce process variation and improve consistency.

🟦 E（Expectation）

The Python-based SPC system should enable early detection of quality issues, support timely corrective actions, and lead to reduced defect rates, more consistent product quality, and lower production waste in the steel manufacturing process.
#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <map>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <chrono>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <cassert>

using namespace std;

// Constants
const int MAX_NUM_STEPS = 1000000;
const double TENSILE_STRENGTH_MIN = 500.0;
const double TENSILE_STRENGTH_MAX = 700.0;
const double THICKNESS_MIN = 0.5;
const double THICKNESS_MAX = 1.0;
const double SURFACE_FINISH_MIN = 0.0;
const double SURFACE_FINISH_MAX = 1.0;
const double CONTROL_LIMIT_MIN = 50.0;
const double CONTROL_LIMIT_MAX = 150.0;
const double ALARM_THRESHOLD = 100.0;
const double ALARM_THRESHOLD_MIN = 0.0;
const double ALARM_THRESHOLD_MAX = 100.0;
const double ALARM_THRESHOLD_MIN_THICKNESS = 0.5;
const double ALARM_THRESHOLD_MAX_THICKNESS = 1.0;
const double ALARM_THRESHOLD_MIN_SURFACE_FINISH = 0.0;
const double ALARM_THRESHOLD_MAX_SURFACE_FINISH = 1.0;
const double ALARM_THRESHOLD_MIN_TENSILE_STRENGTH = 500.0;
const double ALARM_THRESHOLD_MAX_TENSILE_STRENGTH = 700.0;
const double ALARM_THRESHOLD_MIN_CONTROL_LIMIT = 50.0;
const double ALARM_THRESHOLD_MAX_CONTROL_LIMIT = 150.0;
const double ALARM
