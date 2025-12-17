+----------------------------+------------------------------------------+----------------+------+-----------+--------+
| Attribute                  | Description                              | Standard value | Unit | Data type | Source |
+============================+==========================================+================+======+===========+========+
| ``demand_side``            | If set to 'true', the demand side        |                | —    | bool      |        |
|                            |                                          |                |      |           |        |
|                            | scenario will be implemented. This       |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | scenario consists of future climate and  |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | demand scenarios specified in the        |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | 'demand_side' dict.                      |                |      |           |        |
+----------------------------+------------------------------------------+----------------+------+-----------+--------+
| ``fossil_heater_retrofit`` | If set to 'true', the fossil heating     |                | —    | bool      |        |
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
| ``pv_integration``         | If set to 'true', the PV integration     |                | —    | bool      |        |
|                            |                                          |                |      |           |        |
|                            | scenario will be implemented. A          |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | specified share of the additional PV     |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | potential will be implemented. The share |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | can be set in the solar_pv technology.   |                |      |           |        |
+----------------------------+------------------------------------------+----------------+------+-----------+--------+
| ``wind_integration``       | If set to 'true', the wind power         |                | —    | bool      |        |
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
| ``thermal_energy_storage`` | If set to 'true', the thermal energy     |                | —    | bool      |        |
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
| ``nuclear_phaseout``       | If set to 'true', a nuclear phaseout     |                | —    | bool      |        |
|                            |                                          |                |      |           |        |
|                            | will be considered in the simulation,    |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | based on the selected year in the        |                |      |           |        |
|                            |                                          |                |      |           |        |
|                            | 'demand_side' dict.                      |                |      |           |        |
+----------------------------+------------------------------------------+----------------+------+-----------+--------+
