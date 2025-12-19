+----------------------------+------------------------------------------+----------------+------+-----------+--------+
| Attribute                  | Description                              | Standard value | Unit | Data type | Source |
+============================+==========================================+================+======+===========+========+
| ``demand_side``            | If set to 'true', the demand side        | False          | —    | bool      | *n/a*  |
|                            |                                          |                |      |           |        |
|                            | scenario will be implemented. This       |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | scenario consists of future climate and  |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | demand scenarios specified in the        |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | 'demand_side' dict.                      |                |      |           |        |
+----------------------------+------------------------------------------+----------------+------+-----------+--------+
| ``fossil_heater_retrofit`` | If set to 'true', the fossil heating     | False          | —    | bool      | *n/a*  |
|                            |                                          |                |      |           |        |
|                            | system retrofit scenario will be         |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | implemented. A fraction of the fossil    |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | heating capacity will be replaced by     |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | heat pumps. The fraction of replacement  |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | can be set in the respective             |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | technologies (oil_boiler, gas_boiler,    |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | wood_boiler).                            |                |      |           |        |
+----------------------------+------------------------------------------+----------------+------+-----------+--------+
| ``pv_integration``         | If set to 'true', the PV integration     | False          | —    | bool      | *n/a*  |
|                            |                                          |                |      |           |        |
|                            | scenario will be implemented. A          |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | specified share of the additional PV     |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | potential will be implemented. The share |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | can be set in the solar_pv technology.   |                |      |           |        |
+----------------------------+------------------------------------------+----------------+------+-----------+--------+
| ``wind_integration``       | If set to 'true', the wind power         | False          | —    | bool      | *n/a*  |
|                            |                                          |                |      |           |        |
|                            | integration scenario will be             |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | implemented. A specified share of the    |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | additional wind power potential will be  |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | implemented. The share can be set in the |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | wind_power technology.                   |                |      |           |        |
+----------------------------+------------------------------------------+----------------+------+-----------+--------+
| ``thermal_energy_storage`` | If set to 'true', the thermal energy     | False          | —    | bool      | *n/a*  |
|                            |                                          |                |      |           |        |
|                            | storage (TES) scenario will be           |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | implemented. A TES of specified size     |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | will be integrated in the energy system  |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | and charged/discharged by heat pump. The |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | TES specifications can be set in the     |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | 'tes' technology.                        |                |      |           |        |
+----------------------------+------------------------------------------+----------------+------+-----------+--------+
| ``nuclear_phaseout``       | If set to 'true', a nuclear phaseout     | False          | —    | bool      | *n/a*  |
|                            |                                          |                |      |           |        |
|                            | will be considered in the simulation,    |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | based on the selected year in the        |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | 'demand_side' dict.                      |                |      |           |        |
+----------------------------+------------------------------------------+----------------+------+-----------+--------+
