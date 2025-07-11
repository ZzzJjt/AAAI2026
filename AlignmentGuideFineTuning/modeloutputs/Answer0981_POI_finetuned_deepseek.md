### Intent:
**Intent Summary:**  
Create an automated control system for LNG vaporization with instrumentation (flow, temperature, valves) to regulate the process from storage to gas output.  

*(Focused on LNG flow/temperature control with valves and meters, analogous to the beer brewing process's need for setpoints and instrumentation.)*

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
Create an automated control system for LNG vaporization with instrumentation (flow, temperature, valves) to regulate the process from storage to gas output.  

*(Focused on LNG flow/temperature control with valves and meters, analogous to the beer brewing process's need for setpoints and instrumentation.)*
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

#define MAX_LENGTH 100
#define MAX_NUM 1000000

// Function to check if a number is prime
bool is_prime(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

// Function to generate a random number
int generate_random(int min, int max) {
    return rand() % (max - min + 1) + min;
}

// Function to generate a list of prime numbers
void generate_primes(int* primes, int size) {
    primes[0] = 2;
    primes[1] = 3;
    for (int i = 2; i < size; i++) {
        if (is_prime(i)) {
            primes[i] = i;
        }
    }
}

// Function to generate a list of prime numbers up to a given limit
void generate_primes_up_to(int limit, int* primes, int size) {
    for (int i = 0; i < size; i++) {
        primes[i] = 2;
    }
    for (int i = 3; i <= limit; i++) {
        if (is_prime(i)) {
            primes[i] = i;
        }
    }
}

// Function to generate a list of prime numbers up to a given limit
void generate_primes_up_to_limit(int limit, int* primes, int size) {
    for (int i = 0; i < size; i++) {
        primes[i] = 2;
    }
    for (int i = 3; i <= limit; i++) {
        if (is_prime(i)) {
            primes[i] = i;
        }
    }
