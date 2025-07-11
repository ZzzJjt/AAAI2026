### Intent:
**Intent Summary:**  
Create a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including process flow, instrumentation (e.g., TT101, FIC201), control loops, safety interlocks (e.g., PSH301 → ESD1), and piping, formatted in structured plain-text notation.  

*(Focus: Standardized textual representation of control logic for LNG vaporization, ensuring traceability and automation readiness.)*

### Prompt:
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Designing a NORSOK-compliant System Control Diagram (SCD) for a LNG vaporizer system is essential for ensuring operational safety, process transparency, and automation readiness. In many early-stage projects or documentation scenarios, engineers need a textual representation of the control diagram when graphical tools aren’t available. Without a structured textual format—including piping, instrumentation, and interlocks—it can be difficult to communicate control logic clearly across disciplines or trace compliance with standards.

⸻

🟩 A (After) – The Desired Outcome

Create a NORSOK-style System Control Diagram (SCD) using textual notation for a LNG vaporizer system. This diagram should:
	•	Include major process elements (e.g., LNG feed lines, vaporizers, heaters, gas outlet)
	•	Represent instrumentation and control loops with realistic tag numbers (e.g., TT101, FIC202, PSV301)
	•	Clearly document interlocks (e.g., pressure high-high trip, ESD logic)
	•	Indicate piping flow using arrows (-->) and group control functions logically (e.g., temperature control loop, flow regulation, safety shutdowns)

The result will be a functional, plain-text SCD layout that can support control system development and safety verification.

⸻

🟧 B (Bridge) – How to Get There
	1.	Define process flow from LNG inlet → vaporizer → pressure regulation → gas outlet.
	2.	Assign and place instrumentation:
	•	Temperature loop: TT101 → TIC101 → Heater Control Valve (TCV101)
	•	Flow loop: FT201 → FIC201 → FCV201
	•	Safety: PSH301 (Pressure Switch High) → ESD1
	3.	Use NORSOK-style loop and tag conventions (e.g., P&ID cross-references like U-610, L-120).
	4.	Format in readable text with logical grouping and indentation. Example:

 LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer
                                       |
                                       --> TT101 --> TIC101 --> TCV101
                                               |
                                               --> PSH301 --> ESD1

### Generated Code:
**Intent Summary:**  
Create a NORSOK-compliant textual System Control Diagram (SCD) for an LNG vaporizer system, including process flow, instrumentation (e.g., TT101, FIC201), control loops, safety interlocks (e.g., PSH301 → ESD1), and piping, formatted in structured plain-text notation.  

*(Focus: Standardized textual representation of control logic for LNG vaporization, ensuring traceability and automation readiness.)*
**SCD LNG Vaporizer:**

Create a NORSOK system control diagram (SCD) in textual notation for a LNG Vaporizer System. Include instrumentation, control loops, and interlocks. Provide concrete tag numbers and piping.


**B-A-B:**

🟥 B (Before) – The Problem or Challenge

Designing a NORSOK-compliant System Control Diagram (SCD) for a LNG vaporizer system is essential for ensuring operational safety, process transparency, and automation readiness. In many early-stage projects or documentation scenarios, engineers need a textual representation of the control diagram when graphical tools aren’t available. Without a structured textual format—including piping, instrumentation, and interlocks—it can be difficult to communicate control logic clearly across disciplines or trace compliance with standards.

⸻

🟩 A (After) – The Desired Outcome

Create a NORSOK-style System Control Diagram (SCD) using textual notation for a LNG vaporizer system. This diagram should:
	•	Include major process elements (e.g., LNG feed lines, vaporizers, heaters, gas outlet)
	•	Represent instrumentation and control loops with realistic tag numbers (e.g., TT101, FIC202, PSV301)
	•	Clearly document interlocks (e.g., pressure high-high trip, ESD logic)
	•	Indicate piping flow using arrows (-->) and group control functions logically (e.g., temperature control loop, flow regulation, safety shutdowns)

The result will be a functional, plain-text SCD layout that can support control system development and safety verification.

⸻

🟧 B (Bridge) – How to Get There
	1.	Define process flow from LNG inlet → vaporizer → pressure regulation → gas outlet.
	2.	Assign and place instrumentation:
	•	Temperature loop: TT101 → TIC101 → Heater Control Valve (TCV101)
	•	Flow loop: FT201 → FIC201 → FCV201
	•	Safety: PSH301 (Pressure Switch High) → ESD1
	3.	Use NORSOK-style loop and tag conventions (e.g., P&ID cross-references like U-610, L-120).
	4.	Format in readable text with logical grouping and indentation. Example:

 LNG Inlet --> FT201 --> FIC201 --> FCV201 --> Vaporizer
                                       |
                                       --> TT101 --> TIC101 --> TCV101
                                               |
                                               --> PSH301 --> ESD1

This format is easy to read, maintain, and integrate into control system design tools.
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

// Function to calculate the distance between two points
double calculateDistance(double x1, double y1, double x2, double y2) {
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

// Function to calculate the shortest path between two points
vector<int> shortestPath(vector<vector<int>> grid, int x1, int y1, int x2, int y2) {
    int n = grid.size();
    vector<vector<int>> dist(n, vector<int>(n, -1));
    dist[x1][y1] = 0;
    queue<pair<int, int>> q;
    q.push({x1, y1});

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        if (x == x2 && y == y2) {
            return {x2, y2};
        }

        if (x < n && y < n && dist[x][y] != -1) {
            continue;
        }

        dist[x][y] = dist[x][y] == -1 ? 0 : dist[x][y];
        q.push({x, y});

        if (x > 0) {
            if (dist[x-1][y] == -1 || dist[x][y] + 1 < dist[x-1][y]) {
                dist[x-1][y] = dist[x][y] + 1;
                q.push({x-1, y});
            }
        }

        if (y > 0) {
            if (dist[x][y-1] == -1 || dist[x][y] + 1 < dist[x][y-1]) {
                dist[x][y-1] = dist[x][y] +
