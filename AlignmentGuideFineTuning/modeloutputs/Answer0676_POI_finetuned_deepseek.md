### Intent:
**Intent Summary:**  
Generate an I/O list table for feedwater control in a power plant's steam-water cycle, including signal names, tagnumbers, types (A/D), units, ranges, setpoints, and P&ID references, to support PLC/HMI integration and instrumentation documentation.  

*(Focus: Structured data generation for control system engineering.)*

### Prompt:
**IO List Steam Water Cycle:**

Create an I/O list as a table for feedwater control in a steam-water cycle in a power plant. Have as columns names, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer responsible for defining instrumentation and signal documentation for the feedwater control system in a steam-water cycle of a power plant.

⸻

🟩 I (Input) – Information Provided

You are to create an I/O list in table format that includes the following columns for each signal:
	•	Signal Name
	•	Signal Tag Number
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

This list will cover essential elements of the feedwater control loop, such as flow transmitters, drum level indicators, control valves, and pump statuses.

⸻

🟧 S (Steps) – Steps to Perform
	1.	Identify common I/O signals associated with feedwater control, including:
	•	Drum Level Transmitters
	•	Feedwater Flow Transmitters
	•	Control Valve Positions
	•	Pump Start/Stop Signals
	2.	Assign each signal a unique tagnumber and specify whether it is analog or digital.
	3.	Add appropriate engineering units (e.g., %, t/h, bar), define realistic ranges (e.g., 0–100%), and enter typical setpoints.
	4.	Ensure each entry is linked to a P&ID reference for traceability and cross-discipline alignment.
	5.	Format the data into a clean, consistent table that can be imported into design tools, PLC/HMI projects, or engineering reports.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a complete and professionally structured I/O list for the feedwater control section of the steam-water cycle. This list will support:
	•	PLC configuration
	•	Instrumentation specification
	•	HMI integration
	•	Commissioning and validation aligned with P&ID documentation

### Generated Code:
**Intent Summary:**  
Generate an I/O list table for feedwater control in a power plant's steam-water cycle, including signal names, tagnumbers, types (A/D), units, ranges, setpoints, and P&ID references, to support PLC/HMI integration and instrumentation documentation.  

*(Focus: Structured data generation for control system engineering.)*
**IO List Steam Water Cycle:**

Create an I/O list as a table for feedwater control in a steam-water cycle in a power plant. Have as columns names, signal tagnumber, analog/digital, engineering unit, ranges, setpoint, and P&ID reference.

**R-I-S-E:**

🟥 R (Role) – Define Your Role

Act as a control systems engineer responsible for defining instrumentation and signal documentation for the feedwater control system in a steam-water cycle of a power plant.

⸻

🟩 I (Input) – Information Provided

You are to create an I/O list in table format that includes the following columns for each signal:
	•	Signal Name
	•	Signal Tag Number
	•	Analog/Digital
	•	Engineering Unit
	•	Range
	•	Setpoint
	•	P&ID Reference

This list will cover essential elements of the feedwater control loop, such as flow transmitters, drum level indicators, control valves, and pump statuses.

⸻

🟧 S (Steps) – Steps to Perform
	1.	Identify common I/O signals associated with feedwater control, including:
	•	Drum Level Transmitters
	•	Feedwater Flow Transmitters
	•	Control Valve Positions
	•	Pump Start/Stop Signals
	2.	Assign each signal a unique tagnumber and specify whether it is analog or digital.
	3.	Add appropriate engineering units (e.g., %, t/h, bar), define realistic ranges (e.g., 0–100%), and enter typical setpoints.
	4.	Ensure each entry is linked to a P&ID reference for traceability and cross-discipline alignment.
	5.	Format the data into a clean, consistent table that can be imported into design tools, PLC/HMI projects, or engineering reports.

⸻

🟦 E (Expectation) – Expected Outcome

Deliver a complete and professionally structured I/O list for the feedwater control section of the steam-water cycle. This list will support:
	•	PLC configuration
	•	Instrumentation specification
	•	HMI integration
	•	Commissioning and validation aligned with P&ID documentation
	•	Improved communication and traceability across engineering teams
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

// Constants
const int MAX_NUM_ROWS = 100;
const int MAX_NUM_COLS = 100;
const int MAX_NUM_ROWS_PER_PAGE = 10;
const int MAX_NUM_COLS_PER_PAGE = 10;
const int MAX_NUM_PAGES = 10;
const int MAX_NUM_ROWS_PER_PAGE = 10;
const int MAX_NUM_COLS_PER_PAGE = 10;
const int MAX_NUM_PAGES = 10;
const int MAX_NUM_ROWS = 100;
const int MAX_NUM_COLS = 100;
const int MAX_NUM_ROWS_PER_PAGE = 10;
const int MAX_NUM_COLS_PER_PAGE = 10;
const int MAX_NUM_PAGES = 10;
const int MAX_NUM_ROWS_PER_PAGE = 10;
const int MAX_NUM_COLS_PER_PAGE = 10;
const int MAX_NUM_PAGES = 10;
const int MAX_NUM_ROWS_PER_PAGE = 10;
const int MAX_NUM_COLS_PER_PAGE = 10;
const int MAX_NUM_PAGES = 10;
const int MAX_NUM_ROWS_PER_PAGE = 10;
const int MAX_NUM_COLS_PER_PAGE = 10;
const int MAX_NUM_PAGES = 10;
const int MAX_NUM_ROWS_PER_PAGE = 10;
const int MAX_NUM_COLS_PER_PAGE = 10;
const int MAX_NUM_PAGES = 10;
const int MAX_NUM_ROWS_PER_PAGE = 10;
const int MAX_NUM_COLS_
