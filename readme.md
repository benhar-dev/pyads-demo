# Example using pyads with TwinCAT

## Disclaimer

This is a personal guide not a peer reviewed journal or a sponsored publication. We make
no representations as to accuracy, completeness, correctness, suitability, or validity of any
information and will not be liable for any errors, omissions, or delays in this information or any
losses injuries, or damages arising from its display or use. All information is provided on an as
is basis. It is the reader’s responsibility to verify their own facts.

The views and opinions expressed in this guide are those of the authors and do not
necessarily reflect the official policy or position of any other agency, organization, employer or
company. Assumptions made in the analysis are not reflective of the position of any entity
other than the author(s) and, since we are critically thinking human beings, these views are
always subject to change, revision, and rethinking at any time. Please do not hold us to them
in perpetuity.

## Install 
Pyads installation and instructions are here
https://pypi.org/project/pyads/

## TwinCAT
This project uses TcXaeShell 3.1.4024.0

## Getting started
This is not a guide for TcXaeShell, please visit http://beckhoff.com/ for further guides
* Open the included TwinCAT project and activate on your local machine
* Login and set the PLC running
* Run the HelloWorld.py

## Common error messages

### ADSError: target machine not found    Missing ADS routes (7). 
Incorrect ads address

### ADSError: timeout elapsed (1861).
Correct Route on the Client, but Route missing on the target side.

### ADSError: target port not found   ADS Server not started (6). 
Incorrect target port (by default this is 851 for TwinCAT3)

### ADSError: symbol not found (1808).
Possible incorrect runtime port selected
