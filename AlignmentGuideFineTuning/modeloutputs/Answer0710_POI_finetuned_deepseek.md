### Intent:
"Implement a Python-based statistical process control system for steel manufacturing that monitors quality metrics, detects anomalies using control charts, triggers alarms, and suggests corrective actions, with simulated process data for demonstration."

### Prompt:
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-T-F:**

🟥 R（Role）

Act as a Python developer focused on industrial quality control and real-time process monitoring.

🟩 T（Task）

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing quality in steel manufacturing. The system should track key metrics such as tensile strength, thickness, and surface finish using control charts, detect out-of-control conditions, trigger alarms, and recommend corrective actions. Additionally, simulate the manufacturing process to demonstrate how SPC improves quality and reduces variability.

🟧 F（Format）

Provide a Python script that includes:
	•	Data simulation for steel manufacturing quality metrics
	•	Real-time SPC tools (e.g., X̄, R, or S charts with control limits)
	•	Detection logic for out-of-control signals and rule violations
	•	Alarm system with corresponding corrective action suggestions
	•	Terminal or log output showing detection results and system responses (plots optional)

### Generated Code:
"Implement a Python-based statistical process control system for steel manufacturing that monitors quality metrics, detects anomalies using control charts, triggers alarms, and suggests corrective actions, with simulated process data for demonstration."
**Statistical Process Control for Steel Manufacturing Using Python:**

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing the quality of steel manufacturing processes. The code should track key quality metrics such as tensile strength, thickness, and surface finish in real-time, using control charts and other SPC tools to detect and respond to process variations. Implement alarms for out-of-control conditions, and suggest corrective actions to minimize defects and ensure product consistency.

Simulate the steel manufacturing process, and demonstrate how SPC can be used to maintain high-quality production standards while minimizing waste and process variability.

**R-T-F:**

🟥 R（Role）

Act as a Python developer focused on industrial quality control and real-time process monitoring.

🟩 T（Task）

Develop Python code to implement a statistical process control (SPC) system for monitoring and optimizing quality in steel manufacturing. The system should track key metrics such as tensile strength, thickness, and surface finish using control charts, detect out-of-control conditions, trigger alarms, and recommend corrective actions. Additionally, simulate the manufacturing process to demonstrate how SPC improves quality and reduces variability.

🟧 F（Format）

Provide a Python script that includes:
	•	Data simulation for steel manufacturing quality metrics
	•	Real-time SPC tools (e.g., X̄, R, or S charts with control limits)
	•	Detection logic for out-of-control signals and rule violations
	•	Alarm system with corresponding corrective action suggestions
	•	Terminal or log output showing detection results and system responses (plots optional)
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

using namespace std;

// Constants
const int MAX_NUM_STEPS = 10000;
const double MIN_STRENGTH = 5000.0;
const double MAX_STRENGTH = 6000.0;
const double MIN_THICKNESS = 0.5;
const double MAX_THICKNESS = 1.0;
const double MIN_SURFACE_FINISH = 0.0;
const double MAX_SURFACE_FINISH = 1.0;
const double MIN_TEMPERATURE = 1500.0;
const double MAX_TEMPERATURE = 1600.0;
const double MIN_PRESSURE = 0.0;
const double MAX_PRESSURE = 0.5;
const double MIN_DENSITY = 0.0;
const double MAX_DENSITY = 0.5;
const double MIN_MATERIAL_TEMPERATURE = 1500.0;
const double MAX_MATERIAL_TEMPERATURE = 1600.0;
const double MIN_MATERIAL_PRESSURE = 0.0;
const double MAX_MATERIAL_PRESSURE = 0.5;
const double MIN_MATERIAL_DENSITY = 0.0;
const double MAX_MATERIAL_DENSITY = 0.5;
const double MIN_MATERIAL_TEMPERATURE_RATIO = 0.0;
const double MAX_MATERIAL_TEMPERATURE_RATIO = 1.0;
const double MIN_MATERIAL_PRESSURE_RATIO = 0.0;
const double MAX_MATERIAL_PRESSURE_RATIO = 1.0;
const double MIN_MATERIAL_DENSITY_RATIO = 0.0;
const double MAX_MATERIAL_DENSITY_RATIO = 1.0;
