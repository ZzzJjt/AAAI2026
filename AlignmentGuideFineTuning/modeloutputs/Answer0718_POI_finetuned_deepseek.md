### Intent:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block that wraps a C-based Open62541 OPC UA subscription handler, enabling PLCs to dynamically establish and manage OPC UA subscriptions with configurable intervals, priority, and timeout, while providing real-time status feedback (Done/Busy/Error) and error handling.  

*(Focus: C-to-ST integration for OPC UA subscriptions with cyclic execution and adjustable parameters.)*

### Prompt:
**OPC UA Subscription Creation Using Open62541 and IEC 61131-3 Structured Text:**

Develop a C function block for OPC UA subscription creation using the Open62541 library, which will be wrapped in IEC 61131-3 structured text code. The function block receives a Connection Handle as a DWORD and has the following inputs: an executed flag (BOOL), a priority (BYTE), and a timeout (TIME). As outputs, it provides three status flags (Done, Busy, Error) along with two DWORD outputs (ErrorID, SubscriptionHdl). The function block also includes an IN/OUT variable PublishingInterval (type TIME), which allows dynamic adjustment of the subscription interval.

In your explanation, describe how this C function block can be wrapped inside IEC 61131-3 structured text code, highlighting the integration steps and providing an example of how to call the function block within an ST program. Discuss error handling, subscription management, and real-time communication with OPC UA servers.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a control systems developer implementing OPC UA functionality using C and IEC 61131-3 Structured Text (ST) for industrial communication.

⸻

🟩 T (Task) – What You Need to Do

Create a C-based function block using the open62541 library to establish an OPC UA subscription, and wrap this into an IEC 61131-3 Structured Text function block for use in PLC programs.

The ST function block should include the following interface:

Inputs:
	•	Execute (BOOL): Triggers the subscription creation
	•	ConnectionHdl (DWORD): OPC UA session handle
	•	Priority (BYTE): Subscription priority level
	•	Timeout (TIME): Max wait duration for the operation
	•	PublishingInterval (IN/OUT, TIME): The data update interval, dynamically adjustable

Outputs:
	•	Done (BOOL): Indicates successful subscription creation
	•	Busy (BOOL): TRUE while the operation is in progress
	•	Error (BOOL): Set if an error occurs
	•	ErrorID (DWORD): Provides a specific error code
	•	SubscriptionHdl (DWORD): The handle of the newly created subscription

Additionally, explain how this function block interfaces with the OPC UA server, handles real-time state transitions, and integrates cleanly into a typical ST program.

⸻

🟧 F (Format) – Expected Output

Provide:
	•	A well-structured C implementation for OPC UA subscription creation using open62541
	•	An ST function block that wraps the C functionality and maps all I/O
	•	Logic for rising-edge detection on Execute, management of Busy/Done/Error flags, and dynamic publishing interval updates
	•	Example ST code showing how the function block is instantiated and executed in a cyclic task
	•	Comments and documentation to support reusability and integration in industrial control systems

### Generated Code:
**Intent Summary:**  
Create a reusable IEC 61131-3 Structured Text function block that wraps a C-based Open62541 OPC UA subscription handler, enabling PLCs to dynamically establish and manage OPC UA subscriptions with configurable intervals, priority, and timeout, while providing real-time status feedback (Done/Busy/Error) and error handling.  

*(Focus: C-to-ST integration for OPC UA subscriptions with cyclic execution and adjustable parameters.)*
**OPC UA Subscription Creation Using Open62541 and IEC 61131-3 Structured Text:**

Develop a C function block for OPC UA subscription creation using the Open62541 library, which will be wrapped in IEC 61131-3 structured text code. The function block receives a Connection Handle as a DWORD and has the following inputs: an executed flag (BOOL), a priority (BYTE), and a timeout (TIME). As outputs, it provides three status flags (Done, Busy, Error) along with two DWORD outputs (ErrorID, SubscriptionHdl). The function block also includes an IN/OUT variable PublishingInterval (type TIME), which allows dynamic adjustment of the subscription interval.

In your explanation, describe how this C function block can be wrapped inside IEC 61131-3 structured text code, highlighting the integration steps and providing an example of how to call the function block within an ST program. Discuss error handling, subscription management, and real-time communication with OPC UA servers.

**R-T-F:**

🟥 R (Role) – Your Role

Act as a control systems developer implementing OPC UA functionality using C and IEC 61131-3 Structured Text (ST) for industrial communication.

⸻

🟩 T (Task) – What You Need to Do

Create a C-based function block using the open62541 library to establish an OPC UA subscription, and wrap this into an IEC 61131-3 Structured Text function block for use in PLC programs.

The ST function block should include the following interface:

Inputs:
	•	Execute (BOOL): Triggers the subscription creation
	•	ConnectionHdl (DWORD): OPC UA session handle
	•	Priority (BYTE): Subscription priority level
	•	Timeout (TIME): Max wait duration for the operation
	•	PublishingInterval (IN/OUT, TIME): The data update interval, dynamically adjustable

Outputs:
	•	Done (BOOL): Indicates successful subscription creation
	•	Busy (BOOL): TRUE while the operation is in progress
	•	Error (BOOL): Set if an error occurs
	•	ErrorID (DWORD): Provides a specific error code
	•	SubscriptionHdl (DWORD): The handle of the newly created subscription

Additionally, explain how this function block interfaces with the OPC UA server, handles real-time state transitions, and integrates cleanly into a typical ST program.

⸻

🟧 F (Format) – Expected Output

Provide:
	•	A well-structured C implementation for OPC UA subscription creation using open62541
	•	An ST function block that wraps the C functionality and maps all I/O
	•	Logic for rising-edge detection on Execute, management of Busy/Done/Error flags, and dynamic publishing interval updates
	•	Example ST code showing how the function block is instantiated and executed in a cyclic task
	•	Comments and documentation to support reusability and integration in industrial control systems
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>

#define I2C_ADDR 0x04 // I2C address of the sensor
#define I2C_REG_TEMP 0x00 // Register for temperature data
#define I2C_REG_HUMID 0x01 // Register for humidity data

#define I2C_READ 0x01 // Read command
#define I2C_WRITE 0x02 // Write command

#define I2C_ACK 0x01 // ACK signal
#define I2C_NAK 0x00 // NAK signal

#define I2C_TIMEOUT 1000 // Timeout in milliseconds

int i2c_open(const char *devname, int flags, mode_t mode) {
    int fd = open(devname, flags | O_RDWR);
    if (fd < 0) {
        printf("Failed to open I2C device: %s\n", devname);
        return -1;
    }
    return fd;
}

int i2c_write(int fd, uint8_t addr, uint8_t reg, uint8_t *data, int len) {
    if (len > 8) {
        printf("Error: Length of data too large\n");
        return -1;
    }

    uint8_t buffer[8];
    buffer[0] = addr;
    buffer[1] = reg;
    memcpy(buffer + 2, data, len);

    if (ioctl(fd, I2C_IOC_WRITE, buffer) < 0) {
        printf("Failed to write to I2C device: %s\n", devname);
        return -1;
    }
    return len;
}

int i2c_read(int fd, uint8_t addr, uint8_t reg, uint8_t *data, int len
