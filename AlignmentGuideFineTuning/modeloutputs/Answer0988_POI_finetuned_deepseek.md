### Intent:
**Intent Summary:**  
Generate a structured control narrative for an ammonium nitrate production reactor, detailing critical parameters, instrumentation, operating sequences, and safety interlocks to ensure safe and efficient automated operation.  

*(Focused on PLC/DCS implementation with setpoints, alarms, and procedural logic for reactor control.)*

### Prompt:
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.


**T-A-G:**

🟥 T (Task)

Develop a text-based Process Flow Diagram (PFD) for a penicillin fermentation process, suitable for engineering documentation and control design.

⸻

🟩 A (Action)
	•	List the major unit operations in sequential order, such as:
Water Tank --> Nutrient Mixer --> Sterilizer --> Fermenter --> Separator --> Product Tank
	•	For each unit, add associated instrumentation using standard tag formats (e.g., TT101, pH201, FIC301).
	•	Describe basic control loops, such as:
	•	Temperature control using: TT201 → TIC201 → TCV201
	•	pH adjustment via: pH202 → PIC202 → Base Pump
	•	Format the diagram in clear plain text, using arrows (-->) to indicate material flow and indentations for instrumentation and control strategies.

⸻

🟦 G (Goal)

Produce a clear, structured, and implementation-ready textual PFD that outlines both the process flow and the control philosophy for penicillin fermentation. This format should help cross-disciplinary teams—from process design to automation—understand the flow and control logic without needing graphical tools.

### Generated Code:
**Intent Summary:**  
Generate a structured control narrative for an ammonium nitrate production reactor, detailing critical parameters, instrumentation, operating sequences, and safety interlocks to ensure safe and efficient automated operation.  

*(Focused on PLC/DCS implementation with setpoints, alarms, and procedural logic for reactor control.)*
**PFD Penicillin Fermentation:**

Create a Process Flow Diagram (PFD) in textual notation for a fermentation process to produce penicillin. Include instrumentation and control philosophy.


**T-A-G:**

🟥 T (Task)

Develop a text-based Process Flow Diagram (PFD) for a penicillin fermentation process, suitable for engineering documentation and control design.

⸻

🟩 A (Action)
	•	List the major unit operations in sequential order, such as:
Water Tank --> Nutrient Mixer --> Sterilizer --> Fermenter --> Separator --> Product Tank
	•	For each unit, add associated instrumentation using standard tag formats (e.g., TT101, pH201, FIC301).
	•	Describe basic control loops, such as:
	•	Temperature control using: TT201 → TIC201 → TCV201
	•	pH adjustment via: pH202 → PIC202 → Base Pump
	•	Format the diagram in clear plain text, using arrows (-->) to indicate material flow and indentations for instrumentation and control strategies.

⸻

🟦 G (Goal)

Produce a clear, structured, and implementation-ready textual PFD that outlines both the process flow and the control philosophy for penicillin fermentation. This format should help cross-disciplinary teams—from process design to automation—understand the flow and control logic without needing graphical tools.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

#define MAX_LENGTH 100
#define MAX_NUM 10000

// Function prototypes
void read_input(int *input, int length);
void print_output(int output[], int length);
void sort_array(int *array, int length);
void bubble_sort(int *array, int length);
void insertion_sort(int *array, int length);
void selection_sort(int *array, int length);
void quick_sort(int *array, int left, int right);
void merge_sort(int *array, int left, int right);
void heap_sort(int *array, int length);
void radix_sort(int *array, int length);
void counting_sort(int *array, int length);
void bucket_sort(int *array, int length);
void shell_sort(int *array, int length);
void heapify(int *array, int length, int i, int heap_size);
void heap_build(int *array, int length, int heap_size);
void heap_sort(int *array, int length);
void radix_sort(int *array, int length);
void counting_sort(int *array, int length);
void bucket_sort(int *array, int length);
void shell_sort(int *array, int length);

// Main function
int main() {
    int input[MAX_LENGTH];
    int output[MAX_NUM];
    int length;

    printf("Enter the length of the input array: ");
    scanf("%d", &length);

    printf("Enter the input array: ");
    read_input(input, length);

    printf("Enter the output array: ");
    read_input(output, length);

    printf("Input array: ");
    print_output(input, length);

    printf("\nOutput array: ");
    print_output(output, length);

    return 0;
}

// Helper functions
void read_input(int *input, int length)
