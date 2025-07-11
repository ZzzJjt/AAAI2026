### Intent:
**Intent Summary:**  
Develop a Python-based statistical process control (SPC) system to monitor and optimize steel manufacturing quality metrics (tensile strength, thickness, surface finish) using real-time control charts, anomaly detection, and corrective actions to reduce variability and defects.  

*(Focus: Steel quality monitoring, real-time SPC, defect minimization via Python automation.)*

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
Develop a Python-based statistical process control (SPC) system to monitor and optimize steel manufacturing quality metrics (tensile strength, thickness, surface finish) using real-time control charts, anomaly detection, and corrective actions to reduce variability and defects.  

*(Focus: Steel quality monitoring, real-time SPC, defect minimization via Python automation.)*
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
const double MIN_THRESHOLD = 0.95;
const double MAX_THRESHOLD = 1.05;
const double MIN_STDEV = 0.01;
const double MAX_STDEV = 0.03;
const double MIN_RATIO = 0.95;
const double MAX_RATIO = 1.05;
const double MIN_VARIANCE = 0.01;
const double MAX_VARIANCE = 0.03;
const double MIN_PEAK_TIME = 10;
const double MAX_PEAK_TIME = 100;
const double MIN_PEAK_HEIGHT = 10;
const double MAX_PEAK_HEIGHT = 100;
const double MIN_PEAK_COUNT = 2;
const double MAX_PEAK_COUNT = 10;
const double MIN_PEAK_DISTANCE = 1;
const double MAX_PEAK_DISTANCE = 10;
const double MIN_PEAK_ANGLE = 0;
const double MAX_PEAK_ANGLE = 360;
const double MIN_PEAK_ANGLE_DIST = 0;
const double MAX_PEAK_ANGLE_DIST = 180;
const double MIN_PEAK_ANGLE_ANGLE = 0;
const double MAX_PEAK_ANGLE_ANGLE = 180;
const double MIN_PEAK_ANGLE_DIST_ANGLE = 0;
const double MAX_PEAK_ANGLE_DIST_ANGLE = 90;
const double MIN_PEAK_ANGLE_ANGLE_DIST = 0;
const double MAX_PEAK_ANGLE_ANGLE_DIST = 45;
const double MIN_PEAK_ANGLE_ANGLE_DIST_ANGLE = 0
