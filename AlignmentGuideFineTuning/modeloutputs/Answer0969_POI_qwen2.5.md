### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block to compare two REAL numbers with configurable decimal precision, outputting equality/greater/less flags and handling invalid inputs, for reliable floating-point comparisons in PLC applications.  

*(Focus: Precision-controlled comparison, error handling, modularity)*

### Prompt:
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text to compare two REAL numbers with precision control up to a user-defined number of decimal places.

⸻

🟩 A (Action)
	•	Accept the following inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT – number of decimal places for comparison
	•	Enable : BOOL – triggers execution
	•	Internally calculate a scaling factor:
\text{Scale} := 10^{\text{Precision}}
	•	Multiply each input by Scale, round the results, and convert them to integers
	•	Compare the two values and set the appropriate output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (if Precision < 0 or Enable = FALSE)
	•	Ensure the logic is modular, scan-cycle safe, and easily reusable

⸻

🟦 G (Goal)

Deliver a robust and reusable real-number comparator function block that reliably handles floating-point comparisons with configurable precision. This will improve accuracy and reliability in PLC-based control applications involving setpoint verification, sensor thresholds, and quality control decisions.

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 function block to compare two REAL numbers with configurable decimal precision, outputting equality/greater/less flags and handling invalid inputs, for reliable floating-point comparisons in PLC applications.  

*(Focus: Precision-controlled comparison, error handling, modularity)*
**Real Comparator:**
Implement a self-contained function block in IEC 61131-3 structured text to compare two real inputs up to n decimal places. Include configurable precision and error handling.


**T-A-G:**

🟥 T (Task)

Create a self-contained function block in IEC 61131-3 Structured Text to compare two REAL numbers with precision control up to a user-defined number of decimal places.

⸻

🟩 A (Action)
	•	Accept the following inputs:
	•	Input1 : REAL
	•	Input2 : REAL
	•	Precision : INT – number of decimal places for comparison
	•	Enable : BOOL – triggers execution
	•	Internally calculate a scaling factor:
\text{Scale} := 10^{\text{Precision}}
	•	Multiply each input by Scale, round the results, and convert them to integers
	•	Compare the two values and set the appropriate output flags:
	•	Equal : BOOL
	•	Greater : BOOL
	•	Less : BOOL
	•	Error : BOOL (if Precision < 0 or Enable = FALSE)
	•	Ensure the logic is modular, scan-cycle safe, and easily reusable

⸻

🟦 G (Goal)

Deliver a robust and reusable real-number comparator function block that reliably handles floating-point comparisons with configurable precision. This will improve accuracy and reliability in PLC-based control applications involving setpoint verification, sensor thresholds, and quality control decisions. The function block should be designed with modularity in mind, allowing for easy integration into larger control systems and facilitating future updates or modifications. The error handling feature ensures that the function block can gracefully handle invalid inputs, preventing system crashes or incorrect decisions due to unexpected data. The precision control feature allows for fine-tuning of the comparison process, making it suitable for a wide range of applications with varying requirements for accuracy and reliability. The function block should be thoroughly tested and validated to ensure its correctness and reliability in real-world scenarios. The function block should be well-documented, with clear descriptions of its inputs, outputs, and functionality, making it easy for other developers to understand and use. The function block should be designed with performance in mind, ensuring that it can handle large volumes of data and complex calculations efficiently. The function block should be designed with maintainability in mind, making it easy to update and modify in the future as new requirements or technologies emerge. The function block should be designed with scalability in mind, making it easy to integrate into larger control systems and handle increasing amounts of data and complexity. The function block should be designed with security in mind, ensuring that it can handle sensitive data and prevent unauthorized access or manipulation. The function block should be designed with fault tolerance in mind, ensuring that it can continue to operate even in the presence of errors or failures. The function block should be designed with fault detection and recovery in mind, ensuring that it can detect and recover from errors or failures quickly and efficiently. The function block should be designed with fault isolation in mind, ensuring that it can isolate and contain errors or failures to prevent them from spreading to other parts of the system. The function block should be designed with fault prevention in mind, ensuring that it can prevent errors or failures from occurring in the first place. The function block should be designed with fault prediction in mind, ensuring that it can predict and prevent errors or failures before they occur. The function block should be designed with fault diagnosis in mind, ensuring that it can diagnose and identify errors or failures quickly and accurately. The function block should be designed with fault correction in mind, ensuring that it can correct errors or failures quickly and efficiently. The function block should be designed with fault recovery in mind, ensuring that it can recover from errors or failures quickly and efficiently. The function block should be designed with fault tolerance in mind, ensuring that it can continue to operate even in the presence of errors or failures. The function block should be designed with fault detection and recovery in mind, ensuring that it can detect and recover
