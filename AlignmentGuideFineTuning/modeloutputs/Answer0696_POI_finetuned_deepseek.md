### Intent:
**Intent Summary:**  
Create an IEC 61131-3 Sequential Function Chart (SFC) to control a single intersection traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using mutually exclusive outputs and cyclic operation.  

*(Focus: PLC logic for timed traffic light sequencing with looped states.)*

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
Create an IEC 61131-3 Sequential Function Chart (SFC) to control a single intersection traffic light system with timed states (Green: 5s, Yellow: 2s, Red: 5s) using mutually exclusive outputs and cyclic operation.  

*(Focus: PLC logic for timed traffic light sequencing with looped states.)*
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
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_NAME_LEN 20
#define MAX_TAG_LEN 10
#define MAX_UNIT_LEN 10
#define MAX_RANGE_LEN 10
#define MAX_SETPOINT_LEN 10
#define MAX_PID_REF_LEN 10

typedef struct {
    char name[MAX_NAME_LEN];
    char tag[MAX_TAG_LEN];
    char analogDigital;
    char unit[MAX_UNIT_LEN];
    char range[MAX_RANGE_LEN];
    char setpoint[MAX_SETPOINT_LEN];
    char pidRef[MAX_PID_REF_LEN];
} Signal;

typedef struct {
    Signal signals[10];
} FeedwaterControlIOList;

void read_signal_data(FeedwaterControlIOList *io_list) {
    FILE *fp = fopen("feedwater_control_io.txt", "r");
    if (fp == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

    char line[100];
    while (fgets(line, sizeof(line), fp)) {
        char *token = strtok(line, " ");
        if (token == NULL) {
            printf("Invalid line format\n");
            exit(1);
        }

        char name[MAX_NAME_LEN];
        strncpy(name, token, MAX_NAME_LEN - 1);
        name[MAX_NAME_LEN - 1] = '\0';

        char tag[MAX_TAG_LEN];
        strncpy(tag, strtok(NULL, " "), MAX_TAG_LEN - 1);
        tag[MAX_TAG_LEN - 1] = '\0';

        char analogDigital;
        analogDigital = (token[0] == 'A') ? true : false;

        char unit[MAX_UNIT_LEN];
        strncpy(unit, strtok(NULL
