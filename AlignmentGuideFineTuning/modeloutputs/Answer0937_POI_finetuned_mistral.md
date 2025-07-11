### Intent:
**Intent Summary:**  
Explain IEC 61131-3's object-oriented features (classes, inheritance, polymorphism) with industrial automation examples, highlighting their benefits, limitations, and practical implementation for modular PLC programming.  

**Key Focus:**  
- OOP concepts in IEC 61131-3 V3.0  
- Pros/cons for industrial automation  
- Demonstration via inheritance/polymorphism  
- Real-world applicability (e.g., device abstraction, reusable templates)

### Prompt:
**Object-oriented 61131-3:**
Discuss the concept of classes and methods introduced in IEC 61131-3 Version 3.0, including a detailed explanation of their limitations, advantages, and disadvantages in the context of industrial automation. Provide a relevant example to illustrate these concepts in practice.

Explain how inheritance is implemented in IEC 61131-3, building on the previous example to show how derived classes can extend base functionality. Additionally, refine the example further to demonstrate polymorphism within this framework, discussing its practical applications and constraints.


**T-A-G:**

🟥 T (Task) – What You Need to Do

Explain the object-oriented programming (OOP) features introduced in IEC 61131-3 Version 3.0, focusing on:
	•	The concepts of classes and methods
	•	Their advantages, disadvantages, and limitations in industrial automation
	•	How inheritance and polymorphism are implemented and applied
	•	A relevant example that demonstrates all three concepts in context

⸻

🟩 A (Action) – How You Should Approach It
	1.	Introduce object-oriented concepts in the context of IEC 61131-3:
	•	Define classes, methods, and their role in encapsulating functionality
	•	Clarify the syntax and structure of OOP in structured text (ST)
	2.	Discuss strengths and weaknesses of using OOP in PLCs:
	•	Advantages: modularity, reusability, abstraction
	•	Disadvantages: scan-cycle impact, limited vendor support, steeper learning curve
	3.	Demonstrate inheritance:
	•	Show how a derived function block extends a base class to add or override behavior
	4.	Demonstrate polymorphism:
	•	Use a reference to a base class that calls subclass-specific implementations at runtime
	5.	Highlight practical constraints and typical application scenarios:
	•	Real-time control
	•	Device abstraction
	•	Reusable component templates

⸻

🟦 G (Goal) – What You Will Deliver

A clear, practical guide that helps automation professionals:
	•	Understand how OOP is implemented in IEC 61131-3 V3.0
	•	Apply classes, inheritance, and polymorphism effectively in industrial control projects
	•	Evaluate when and how to use these features based on system requirements and platform capabilities
	•	Gain confidence in writing modular, scalable, and reusable PLC code using object-oriented principles

### Generated Code:
**Intent Summary:**  
Explain IEC 61131-3's object-oriented features (classes, inheritance, polymorphism) with industrial automation examples, highlighting their benefits, limitations, and practical implementation for modular PLC programming.  

**Key Focus:**  
- OOP concepts in IEC 61131-3 V3.0  
- Pros/cons for industrial automation  
- Demonstration via inheritance/polymorphism  
- Real-world applicability (e.g., device abstraction, reusable templates)
**Object-oriented 61131-3:**
Discuss the concept of classes and methods introduced in IEC 61131-3 Version 3.0, including a detailed explanation of their limitations, advantages, and disadvantages in the context of industrial automation. Provide a relevant example to illustrate these concepts in practice.

Explain how inheritance is implemented in IEC 61131-3, building on the previous example to show how derived classes can extend base functionality. Additionally, refine the example further to demonstrate polymorphism within this framework, discussing its practical applications and constraints.


**T-A-G:**

🟥 T (Task) – What You Need to Do

Explain the object-oriented programming (OOP) features introduced in IEC 61131-3 Version 3.0, focusing on:
	•	The concepts of classes and methods
	•	Their advantages, disadvantages, and limitations in industrial automation
	•	How inheritance and polymorphism are implemented and applied
	•	A relevant example that demonstrates all three concepts in context

⸻

🟩 A (Action) – How You Should Approach It
	1.	Introduce object-oriented concepts in the context of IEC 61131-3:
	•	Define classes, methods, and their role in encapsulating functionality
	•	Clarify the syntax and structure of OOP in structured text (ST)
	2.	Discuss strengths and weaknesses of using OOP in PLCs:
	•	Advantages: modularity, reusability, abstraction
	•	Disadvantages: scan-cycle impact, limited vendor support, steeper learning curve
	3.	Demonstrate inheritance:
	•	Show how a derived function block extends a base class to add or override behavior
	4.	Demonstrate polymorphism:
	•	Use a reference to a base class that calls subclass-specific implementations at runtime
	5.	Highlight practical constraints and typical application scenarios:
	•	Real-time control
	•	Device abstraction
	•	Reusable component templates

⸻

🟦 G (Goal) – What You Will Deliver

A clear, practical guide that helps automation professionals:
	•	Understand how OOP is implemented in IEC 61131-3 V3.0
	•	Apply classes, inheritance, and polymorphism effectively in industrial control projects
	•	Evaluate when and how to use these features based on system requirements and platform capabilities
	•	Gain confidence in writing modular, scalable, and reusable PLC code using object-oriented principles
(* IEC 61131-3 Structured Text: Classes and Inheritance Example *)
(* Demonstrates object-oriented concepts for modular PLC programming *)

PROGRAM MainProgram
VAR
    // Base class for a sensor
    SensorClass : SENSOR;
    // Derived class for a temperature sensor
    TempSensor : TEMP_SENSOR;
    // Derived class for a pressure sensor
    PressureSensor : PRESSURE_SENSOR;
    // Variables for sensor data
    TempValue : REAL;
    PressureValue : REAL;
    // Error flag
    Error : BOOL;
END_VAR

(* Sensor Class Interface *)
CLASS SENSOR
VAR
    (* Common properties *)
    Name : STRING;
    
    (* Methods *)
    METHOD Execute : BOOL
        (* Executes sensor operation *)
        Error := FALSE;
        (* Simulate execution *)
        TempValue := 25.0;
        PressureValue := 1013.2;
        RETURN TRUE;
    END_METHOD;
END_CLASS

(* Temperature Sensor Class *)
CLASS TEMP_SENSOR : SENSOR
VAR
    (* Inherited from Sensor *)
    Name : STRING;
    
    (* New properties *)
    MaxTemp : REAL;
    
    (* Methods *)
    METHOD Execute : BOOL
        (* Calls base class method *)
        RETURN SENSOR.Execute();
    END_METHOD;

    (* Overridden method *)
    METHOD GetTemp : REAL
        (* Returns temperature value *)
        RETURN TempValue;
    END_METHOD;

    (* New method *)
    METHOD CheckTemp : BOOL
        (* Checks if temperature is within limits *)
        IF TempValue > MaxTemp THEN
            Error := TRUE;
        ELSE
            Error := FALSE;
        END_IF;
        RETURN Error;
    END_METHOD;
END_CLASS

(* Pressure Sensor Class *)
CLASS PRESSURE_SENSOR : SENSOR
VAR
    (* Inherited from S
