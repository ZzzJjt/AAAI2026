### Intent:
The task is to create a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing process units, instrumentation, flow directions, and control logic (e.g., PID loops) to support automation design and process control implementation.  

**Intent Summary:**  
*Generate a structured textual PFD for penicillin fermentation with units, instrumentation tags, flow paths, and control philosophy (e.g., temperature/pH regulation via PID loops).*

### Prompt:
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process design engineer documenting the penicillin fermentation process using a text-based Process Flow Diagram (PFD) to support automation design and process control implementation.

⸻

🟩 T (Task) – Define the Objective

Create a PFD in textual notation that includes:
	•	The main process units (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Flow direction between units using arrows (-->)
	•	Key instrumentation with specific tag names (e.g., TT101, pH201, LT301)
	•	A concise control philosophy, describing how critical parameters (temperature, pH, agitation) are monitored and controlled—such as using PID loops or manual setpoints

⸻

🟧 F (Format) – Specify the Output Format

Present the information in a structured plain-text format, including:
	•	A flow line for each process stage
	•	A block below each unit showing associated instruments and control loops
	•	Consistent use of indentation, tag naming, and directional symbols
	•	Example control loop logic such as:

 TT201 → TIC201 → Steam Control Valve (TCV201)

### Generated Code:
The task is to create a text-based Process Flow Diagram (PFD) for penicillin fermentation, detailing process units, instrumentation, flow directions, and control logic (e.g., PID loops) to support automation design and process control implementation.  

**Intent Summary:**  
*Generate a structured textual PFD for penicillin fermentation with units, instrumentation tags, flow paths, and control philosophy (e.g., temperature/pH regulation via PID loops).*
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.

**R-T-F:**

🟥 R (Role) – Define Your Role

Act as a process design engineer documenting the penicillin fermentation process using a text-based Process Flow Diagram (PFD) to support automation design and process control implementation.

⸻

🟩 T (Task) – Define the Objective

Create a PFD in textual notation that includes:
	•	The main process units (e.g., water tank, nutrient mixer, sterilizer, fermenter, separator, product tank)
	•	Flow direction between units using arrows (-->)
	•	Key instrumentation with specific tag names (e.g., TT101, pH201, LT301)
	•	A concise control philosophy, describing how critical parameters (temperature, pH, agitation) are monitored and controlled—such as using PID loops or manual setpoints

⸻

🟧 F (Format) – Specify the Output Format

Present the information in a structured plain-text format, including:
	•	A flow line for each process stage
	•	A block below each unit showing associated instruments and control loops
	•	Consistent use of indentation, tag naming, and directional symbols
	•	Example control loop logic such as:

 TT201 → TIC201 → Steam Control Valve (TCV201) → Steam Supply

pH201 → PID201 → pH Controller (PCC201) → pH Control Valve (PVC201) → pH Adjustment

(Optional)

TT201 → TIC201 → TCV201 → Steam Supply

pH201 → PID201 → PVC201 → pH Adjustment

This format allows for easy integration into automation design documents, control system design, and process documentation.
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <map>

using namespace std;

// Define the process units
vector<string> processUnits = {"Water Tank", "Nutrient Mixer", "Sterilizer", "Fermenter", "Separator", "Product Tank"};

// Define the instrumentation tags
map<string, string> instrumentationTags = {
    {"TT101", "Temperature Transmitter"},
    {"TT201", "Temperature Transmitter"},
    {"TT301", "Temperature Transmitter"},
    {"TT401", "Temperature Transmitter"},
    {"TT501", "Temperature Transmitter"},
    {"TT601", "Temperature Transmitter"},
    {"TT701", "Temperature Transmitter"},
    {"TT801", "Temperature Transmitter"},
    {"TT901", "Temperature Transmitter"},
    {"TT102", "Humidity Transmitter"},
    {"TT103", "Humidity Transmitter"},
    {"TT104", "Humidity Transmitter"},
    {"TT105", "Humidity Transmitter"},
    {"TT106", "Humidity Transmitter"},
    {"TT107", "Humidity Transmitter"},
    {"TT108", "Humidity Transmitter"},
    {"TT109", "Humidity Transmitter"},
    {"TT110", "Humidity Transmitter"},
    {"TT111", "Humidity Transmitter"},
    {"TT112", "Humidity Transmitter"},
    {"TT113", "Humidity Trans
