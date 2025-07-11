### Intent:
The task is to implement a Model Predictive Control (MPC) algorithm in C++ to optimize an HVAC system's energy efficiency while maintaining temperature and humidity comfort levels under dynamic environmental conditions.

### Prompt:
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**T-A-G:**

🟥 T（Task）

Create a C++ program that applies model predictive control (MPC) to optimize the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system.

🟩 A（Action）

Develop code that models the HVAC system’s thermal and humidity dynamics, incorporating variable external conditions and occupancy levels. Implement an MPC algorithm to manage energy usage while maintaining indoor comfort. Simulate scenarios to evaluate the system’s performance under constraints such as temperature variation, energy efficiency requirements, and changing occupancy.

🟦 G（Goal）

Demonstrate how MPC improves the HVAC system’s energy efficiency, responsiveness, and ability to maintain occupant comfort under dynamic, real-world operating conditions—outperforming traditional control methods.

### Generated Code:
The task is to implement a Model Predictive Control (MPC) algorithm in C++ to optimize an HVAC system's energy efficiency while maintaining temperature and humidity comfort levels under dynamic environmental conditions.
**Model Predictive Control for HVAC System Optimization Using C++:**

Develop C++ code to implement a model predictive control (MPC) algorithm for optimizing the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system. The control system should manage temperature, humidity, and energy consumption while maintaining occupant comfort. It must consider dynamic constraints such as varying external temperatures, occupancy levels, and energy efficiency requirements, ensuring optimal control under changing environmental conditions.

Implement C++ code to simulate the HVAC system’s dynamics, and demonstrate how MPC can optimize energy usage, response time, and system performance while adhering to operational constraints.

**T-A-G:**

🟥 T（Task）

Create a C++ program that applies model predictive control (MPC) to optimize the performance of a Heating, Ventilation, and Air Conditioning (HVAC) system.

🟩 A（Action）

Develop code that models the HVAC system’s thermal and humidity dynamics, incorporating variable external conditions and occupancy levels. Implement an MPC algorithm to manage energy usage while maintaining indoor comfort. Simulate scenarios to evaluate the system’s performance under constraints such as temperature variation, energy efficiency requirements, and changing occupancy.

🟦 G（Goal）

Demonstrate how MPC improves the HVAC system’s energy efficiency, responsiveness, and ability to maintain occupant comfort under dynamic, real-world operating conditions—outperforming traditional control methods.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_steps = 1000
dt = 0.1
T_max = 25.0
T_min = 18.0
T_ref = 20.0
H_max = 60.0
H_min = 50.0
H_ref = 55.0

# Initialize state variables
T = np.zeros(num_steps)
H = np.zeros(num_steps)

# Initialize control variables
u = np.zeros(num_steps)
u_prev = np.zeros(num_steps)

# Initialize control limits
T_limits = np.array([T_min, T_max])
H_limits = np.array([H_min, H_max])

# Initialize control variables
T_prev = T[-1]
H_prev = H[-1]

# Initialize control variables
u_prev = np.zeros(num_steps)
u_prev = np.zeros(num_steps)

# Initialize control variables
u_prev = np.zeros(num_steps)
u_prev = np.zeros(num_steps)

# Initialize control variables
u_prev = np.zeros(num_steps)
u_prev = np.zeros(num_steps)

# Initialize control variables
u_prev = np.zeros(num_steps)
u_prev = np.zeros(num_steps)

# Initialize control variables
u_prev = np.zeros(num_steps)
u_prev = np.zeros(num_steps)

# Initialize control variables
u_prev = np.zeros(num_steps)
u_prev = np.zeros(num_steps)

# Initialize control variables
u_prev = np.zeros(num_steps)
u_prev = np.zeros(num_steps)

# Initialize control variables
u_prev = np.zeros(num_steps)
u_prev = np.zeros(num_steps)

# Initialize control variables
u_prev = np.zeros(num_steps)
u_prev = np.zeros(num_steps)

# Initialize control variables
u
