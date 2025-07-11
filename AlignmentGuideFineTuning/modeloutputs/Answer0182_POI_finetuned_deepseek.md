### Intent:
**Intent Summary:**  
Create a detailed control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, and control logic to ensure safe and efficient operation.  

*(For code generation: Focus on translating reactor parameters like temperature, pressure, flow ratios, and pH into programmable control loops with defined setpoints and interlocks.)*

### Prompt:
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In the production of ammonium nitrate, the reactor stage is critical for maintaining safety, product quality, and process efficiency. However, without a clearly defined control narrative—including setpoints, ranges, and instrumentation—operators and control systems risk process instability, inefficient reactions, or unsafe operating conditions. Generic documentation often lacks the precision needed for automation or regulatory compliance.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the ammonium nitrate reactor, including:
	•	Concrete setpoints and control ranges for key parameters such as:
	•	Reaction temperature (e.g., 170–180 °C)
	•	Reactor pressure (e.g., 4.5–5.0 bar)
	•	Ammonia-to-nitric acid ratio
	•	pH control
	•	Identification of critical instrumentation: temperature sensors, pressure transmitters, flow meters, pH analyzers
	•	Description of control logic and interlocks for normal operation and safety shutdowns

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the process overview:
	•	Neutralization of nitric acid with ammonia in a continuous stirred-tank reactor (CSTR)
	2.	List key control loops and their setpoints:
	•	Temperature control loop: TIC-101 setpoint = 175 °C ± 2 °C
	•	Pressure control loop: PIC-102 = 4.8 bar ± 0.2 bar
	•	Flow ratio control: Ammonia:Acid = 1.01:1
	•	pH control loop: target = 6.0–6.5
	3.	Add equipment and instrumentation references (e.g., FIC-103 for ammonia feed, LSH-104 for high-level interlock)
	4.	Detail startup and normal operation sequence, followed by shutdown logic triggered by deviations from pressure, temperature, or flow

### Generated Code:
**Intent Summary:**  
Create a detailed control narrative for an ammonium nitrate reactor, specifying setpoints, instrumentation, and control logic to ensure safe and efficient operation.  

*(For code generation: Focus on translating reactor parameters like temperature, pressure, flow ratios, and pH into programmable control loops with defined setpoints and interlocks.)*
**Control Narrative for Ammonium Nitrate Reactor**

Create a control narrative for a reactor producing ammonium nitrates including concrete setpoints and ranges.

**B-A-B:**

🟥 B (Before) – The Problem or Challenge

In the production of ammonium nitrate, the reactor stage is critical for maintaining safety, product quality, and process efficiency. However, without a clearly defined control narrative—including setpoints, ranges, and instrumentation—operators and control systems risk process instability, inefficient reactions, or unsafe operating conditions. Generic documentation often lacks the precision needed for automation or regulatory compliance.

⸻

🟩 A (After) – The Desired Outcome

Develop a comprehensive control narrative for the ammonium nitrate reactor, including:
	•	Concrete setpoints and control ranges for key parameters such as:
	•	Reaction temperature (e.g., 170–180 °C)
	•	Reactor pressure (e.g., 4.5–5.0 bar)
	•	Ammonia-to-nitric acid ratio
	•	pH control
	•	Identification of critical instrumentation: temperature sensors, pressure transmitters, flow meters, pH analyzers
	•	Description of control logic and interlocks for normal operation and safety shutdowns

⸻

🟧 B (Bridge) – How to Get There
	1.	Define the process overview:
	•	Neutralization of nitric acid with ammonia in a continuous stirred-tank reactor (CSTR)
	2.	List key control loops and their setpoints:
	•	Temperature control loop: TIC-101 setpoint = 175 °C ± 2 °C
	•	Pressure control loop: PIC-102 = 4.8 bar ± 0.2 bar
	•	Flow ratio control: Ammonia:Acid = 1.01:1
	•	pH control loop: target = 6.0–6.5
	3.	Add equipment and instrumentation references (e.g., FIC-103 for ammonia feed, LSH-104 for high-level interlock)
	4.	Detail startup and normal operation sequence, followed by shutdown logic triggered by deviations from pressure, temperature, or flow ratios
	5.	Format the narrative as a structured table or control flow diagram for clarity and ease of integration into automation systems
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <map>

using namespace std;

// Constants
const double PI = 3.14159265358979323846;
const double RADIUS = 1.0;
const double RADIUS_MIN = 0.5;
const double RADIUS_MAX = 2.0;
const double RADIUS_STEP = 0.1;
const double RADIUS_MIN_ANGLE = 0.0;
const double RADIUS_MAX_ANGLE = 2.0 * PI;
const double RADIUS_MIN_ANGLE_STEP = 0.01;
const double RADIUS_MAX_ANGLE_STEP = 0.01;
const double RADIUS_MIN_ANGLE_MIN = RADIUS_MIN;
const double RADIUS_MAX_ANGLE_MAX = RADIUS_MAX;
const double RADIUS_MIN_ANGLE_MAX = RADIUS_MIN;
const double RADIUS_MAX_ANGLE_MIN = RADIUS_MAX;
const double RADIUS_MIN_ANGLE_MIN = RADIUS_MIN;
const double RADIUS_MAX_ANGLE_MAX = RADIUS_MAX;
const double RADIUS_MIN_ANGLE_MAX = RADIUS_MIN;
const double RADIUS_MAX_ANGLE_MIN = RADIUS_MAX;
const double RADIUS_MIN_ANGLE_MIN = RADIUS_MIN;
const double RADIUS_MAX_ANGLE_MAX = RADIUS_MAX;
const double RADIUS_MIN_ANGLE_MAX = RADIUS_MIN;
const double RADIUS_MAX_ANGLE_MIN = RADIUS_MAX;
const double RADIUS_MIN_ANGLE_MIN = RADIUS_MIN;
const double RADIUS_MAX_ANGLE_MAX = RADIUS_MAX;
const double RADIUS_MIN_ANGLE_MAX = RADIUS_MIN;
const double RADIUS_MAX_ANGLE_MIN = RADIUS_MAX;
const double RADIUS_MIN_ANGLE_MIN =
