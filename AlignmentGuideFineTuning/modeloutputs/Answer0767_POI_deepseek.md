### Intent:
**Intent Summary:**  
Create a structured technical guide explaining object-oriented programming (OOP) in IEC 61131-3 (V3.0) for industrial automation, covering classes, inheritance, and polymorphism with practical examples, trade-offs, and best practices.  

**Industrial Control Task:**  
The provided code implements a state-machine-driven polyethylene batch control process, handling raw material preparation, reaction, cooling, and discharge phases with safety checks, input validation, and modular logic.  

*(Focus: OOP explanation for automation, bridging to the batch control example.)*

### Prompt:
**Object-oriented 61131-3:**
Discuss the concept of classes and methods introduced in IEC 61131-3 Version 3.0, including a detailed explanation of their limitations, advantages, and disadvantages in the context of industrial automation. Provide a relevant example to illustrate these concepts in practice.

Explain how inheritance is implemented in IEC 61131-3, building on the previous example to show how derived classes can extend base functionality. Additionally, refine the example further to demonstrate polymorphism within this framework, discussing its practical applications and constraints.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC software developer or automation systems engineer seeking to understand and explain how object-oriented programming (OOP) is applied in IEC 61131-3 Version 3.0, particularly for use in industrial automation.

⸻

🟩 T (Task) – What You Need to Do

Create a technical explanation that covers:
	1.	The concept of classes and methods in IEC 61131-3 V3.0
	2.	Their benefits and limitations in an industrial context
	3.	A working example that demonstrates:
	•	How to define and use a class
	•	How inheritance works by extending a base class
	•	How polymorphism allows dynamic behavior via base class references
	4.	A discussion of practical trade-offs, including:
	•	Increased abstraction vs. complexity in debugging
	•	Portability and vendor support
	•	Impact on scan-cycle performance

⸻

🟦 F (Format) – What the Output Should Look Like

Your final output should be a structured technical document or guide including:
	•	✅ A brief conceptual overview of object-oriented features in IEC 61131-3
	•	✅ A step-by-step code example with structured text (ST) showing class definition, inheritance, and polymorphism
	•	✅ A table or bullet list comparing advantages vs. disadvantages
	•	✅ A summary section highlighting best practices and common use cases for OOP in automation (e.g., modular machinery, device templates)

### Generated Code:
**Intent Summary:**  
Create a structured technical guide explaining object-oriented programming (OOP) in IEC 61131-3 (V3.0) for industrial automation, covering classes, inheritance, and polymorphism with practical examples, trade-offs, and best practices.  

**Industrial Control Task:**  
The provided code implements a state-machine-driven polyethylene batch control process, handling raw material preparation, reaction, cooling, and discharge phases with safety checks, input validation, and modular logic.  

*(Focus: OOP explanation for automation, bridging to the batch control example.)*
**Object-oriented 61131-3:**
Discuss the concept of classes and methods introduced in IEC 61131-3 Version 3.0, including a detailed explanation of their limitations, advantages, and disadvantages in the context of industrial automation. Provide a relevant example to illustrate these concepts in practice.

Explain how inheritance is implemented in IEC 61131-3, building on the previous example to show how derived classes can extend base functionality. Additionally, refine the example further to demonstrate polymorphism within this framework, discussing its practical applications and constraints.

**R-T-F:**

🟥 R (Role) – Your Role

You are a PLC software developer or automation systems engineer seeking to understand and explain how object-oriented programming (OOP) is applied in IEC 61131-3 Version 3.0, particularly for use in industrial automation.

⸻

🟩 T (Task) – What You Need to Do

Create a technical explanation that covers:
	1.	The concept of classes and methods in IEC 61131-3 V3.0
	2.	Their benefits and limitations in an industrial context
	3.	A working example that demonstrates:
	•	How to define and use a class
	•	How inheritance works by extending a base class
	•	How polymorphism allows dynamic behavior via base class references
	4.	A discussion of practical trade-offs, including:
	•	Increased abstraction vs. complexity in debugging
	•	Portability and vendor support
	•	Impact on scan-cycle performance

⸻

🟦 F (Format) – What the Output Should Look Like

Your final output should be a structured technical document or guide including:
	•	✅ A brief conceptual overview of object-oriented features in IEC 61131-3
	•	✅ A step-by-step code example with structured text (ST) showing class definition, inheritance, and polymorphism
	•	✅ A table or bullet list comparing advantages vs. disadvantages
	•	✅ A summary section highlighting best practices and common use cases for OOP in automation (e.g., modular machinery, device templates)

**Guidelines:**

1.	Explain the concepts of classes, methods, inheritance, and polymorphism in a clear and concise manner.
2.	Provide a practical example that demonstrates the use of these concepts in an industrial automation context.
3.	Discuss the trade-offs and limitations of using OOP in IEC 61131-3, including increased abstraction, debugging complexity, vendor support, and performance impact.
4.	Highlight best practices and common use cases for OOP in automation, such as modular machinery and device templates.
5.	Ensure the document is well-structured, easy to follow, and includes relevant examples and diagrams.
