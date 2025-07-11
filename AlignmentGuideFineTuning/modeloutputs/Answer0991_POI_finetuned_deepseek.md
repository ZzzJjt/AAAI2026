### Intent:
**Intent Summary:**  
Create an automation-ready control narrative for an LNG vaporizer system (100,000 kg/h capacity) with detailed process flows, instrumentation tags (NORSOK I-005), PID control loops, and safety interlocks to ensure safe, efficient vaporization of LNG to natural gas at specified setpoints (e.g., 10°C outlet, 4.5 bar pressure).  

*(Focus: Code generation for industrial control logic, instrumentation mapping, and interlock implementation.)*

### Prompt:
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**T-A-G:**

🟥 T (Task)

Create a control narrative for an automated beer brewing process, with emphasis on specifying concrete setpoints and detailing the lautering phase (Section 4).

⸻

🟩 A (Action)
	•	Define the brewing process stages, including specific setpoints and control ranges for parameters like temperature, flow rate, and volume.
	•	In Section 4 – Lautering, include:
	•	A list of required equipment: lauter tun, rake motor, sparge system, wort pump
	•	A list of required instrumentation: turbidity meter, flow transmitter, level sensor, temperature probe
	•	A step-by-step procedure for the lautering process, such as:
	1.	Start recirculation of wort
	2.	Monitor turbidity; wait until it drops below 200 NTU
	3.	Begin transferring wort to the kettle
	4.	Add sparge water at 76 °C to maintain lauter tun level between 60–80%
	5.	Stop process based on turbidity or volume criteria
	•	Include interlock logic, such as:
	•	IF Turbidity > Limit THEN open waste valve
	•	IF Level < Minimum THEN stop sparging

⸻

🟦 G (Goal)

Deliver a clear, structured, and automation-ready control narrative that can be used by control engineers, brewers, and programmers to ensure consistency, quality, and operational reliability in the beer brewing process—especially during the critical lautering phase.

### Generated Code:
**Intent Summary:**  
Create an automation-ready control narrative for an LNG vaporizer system (100,000 kg/h capacity) with detailed process flows, instrumentation tags (NORSOK I-005), PID control loops, and safety interlocks to ensure safe, efficient vaporization of LNG to natural gas at specified setpoints (e.g., 10°C outlet, 4.5 bar pressure).  

*(Focus: Code generation for industrial control logic, instrumentation mapping, and interlock implementation.)*
**Control Narrative Beer Brewing:**

Create a control narrative for beer brewing including concrete setpoints and ranges.

Create a detailed explanation of the Lautering process (Section 4). Include the equipment and instrumentation needed. Provide a list of the steps to execute.

**T-A-G:**

🟥 T (Task)

Create a control narrative for an automated beer brewing process, with emphasis on specifying concrete setpoints and detailing the lautering phase (Section 4).

⸻

🟩 A (Action)
	•	Define the brewing process stages, including specific setpoints and control ranges for parameters like temperature, flow rate, and volume.
	•	In Section 4 – Lautering, include:
	•	A list of required equipment: lauter tun, rake motor, sparge system, wort pump
	•	A list of required instrumentation: turbidity meter, flow transmitter, level sensor, temperature probe
	•	A step-by-step procedure for the lautering process, such as:
	1.	Start recirculation of wort
	2.	Monitor turbidity; wait until it drops below 200 NTU
	3.	Begin transferring wort to the kettle
	4.	Add sparge water at 76 °C to maintain lauter tun level between 60–80%
	5.	Stop process based on turbidity or volume criteria
	•	Include interlock logic, such as:
	•	IF Turbidity > Limit THEN open waste valve
	•	IF Level < Minimum THEN stop sparging

⸻

🟦 G (Goal)

Deliver a clear, structured, and automation-ready control narrative that can be used by control engineers, brewers, and programmers to ensure consistency, quality, and operational reliability in the beer brewing process—especially during the critical lautering phase.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

#define MAX_NUM_OF_STATIONS 10
#define MAX_NUM_OF_TRIPS 10
#define MAX_NUM_OF_CARS 10
#define MAX_NUM_OF_TRIP_CARS 10
#define MAX_NUM_OF_TRIP_STATIONS 10

typedef struct {
    int id;
    char name[20];
    int num_of_cars;
    int num_of_trips;
    int num_of_stations;
} Station;

typedef struct {
    int id;
    int station_id;
    int num_of_cars;
    int num_of_trips;
} Trip;

typedef struct {
    int id;
    int trip_id;
    int car_id;
} Car;

Station stations[MAX_NUM_OF_STATIONS];
Trip trips[MAX_NUM_OF_TRIPS];
Car cars[MAX_NUM_OF_CARS];

void initialize_stations() {
    for (int i = 0; i < MAX_NUM_OF_STATIONS; i++) {
        stations[i].id = i;
        strcpy(stations[i].name, "Station " + std::to_string(i));
        stations[i].num_of_cars = 0;
        stations[i].num_of_trips = 0;
    }
}

void initialize_trips() {
    for (int i = 0; i < MAX_NUM_OF_TRIPS; i++) {
        trips[i].id = i;
        trips[i].station_id = -1;
        trips[i].num_of_cars = 0;
    }
}

void initialize_cars() {
    for (int i = 0; i < MAX_NUM_OF_CARS; i++) {
        cars[i].id = i;
        cars[i].trip_id = -1;
    }
