+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| Attribute        | Description                              | Standard value | Unit         | Data type | Source |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| deployment       | If set to 'true', the technology will be | False          | —            | bool      |        |
|                  |                                          |                |              |           |        |
|                  | considered in the energy system model    |                |              |           |        |
|                  |                                          |                |              |           |        |
|                  | (this does not necessarily mean it will  |                |              |           |        |
|                  |                                          |                |              |           |        |
|                  | be used). Only relevant for              |                |              |           |        |
|                  |                                          |                |              |           |        |
|                  | optimisation.                            |                |              |           |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| kW_el_max        | Maximum electrical power output.         | inf            | kW           | float     |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| force_cap_max    | Force implementation of maximum capacity | False          | kW           | bool      |        |
|                  |                                          |                |              |           |        |
|                  | specified in kW_el_max. Only relevant    |                |              |           |        |
|                  |                                          |                |              |           |        |
|                  | for optimisation.                        |                |              |           |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| cap_min_use      | Minimum capacity to use.                 | 0              | kW           | float     |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| hv_gas_MJpkg     | Heating value (lower) of gas             | 46             | MJ/kg        | float     |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| eta_el           | Electrical conversion effiency.          | 0.35           | —            | float     |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| htp_ratio        | Heat-to-power (htp) ratio (kW_th/kW_el)  | 1.5            | kW_th/kW_el  | float     |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| co2_intensity    | Carbon-dioxide intensity of technology   | 0              | kg CO2/kWh   | float     |        |
|                  |                                          |                |              |           |        |
|                  | output (annual average value).           |                |              |           |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| lifetime         | Expected lifetime of technology before   | 25             | years        | int       |        |
|                  |                                          |                |              |           |        |
|                  | replacement is required.                 |                |              |           |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| capital_cost     | CAPEX cost of technology per unit of     | 5000           | CHF/kWp      | float     |        |
|                  |                                          |                |              |           |        |
|                  | capacity.                                |                |              |           |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| maintenance_cost | OPEX cost of technolgoy per unit of      | 40.1           | CHF/kWp/year | float     |        |
|                  |                                          |                |              |           |        |
|                  | capacity                                 |                |              |           |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
| interest_rate    | Interest rate for computing levelised    | 0.025          | —            | float     |        |
|                  |                                          |                |              |           |        |
|                  | costs (if required).                     |                |              |           |        |
+------------------+------------------------------------------+----------------+--------------+-----------+--------+
