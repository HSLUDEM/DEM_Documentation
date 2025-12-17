+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| Attribute                        | Description                              | Standard value | Unit         | Data type | Source |
+==================================+==========================================+================+==============+===========+========+
| ``deployment``                   | If set to 'true', the technology will be | True           | —            | bool      |        |
|                                  |                                          |                |              |           |        |
|                                  | considered in the energy system model    |                |              |           |        |
|                                  |                                          |                |              |           |        |
|                                  | (this does not necessarily mean it will  |                |              |           |        |
|                                  |                                          |                |              |           |        |
|                                  | be used). Only relevant for              |                |              |           |        |
|                                  |                                          |                |              |           |        |
|                                  | optimisation.                            |                |              |           |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``kWp_max``                      | Kilowatt Peak: Maximum power output of   | inf            | kW           | float     |        |
|                                  |                                          |                |              |           |        |
|                                  | PV system under standard test conditions |                |              |           |        |
|                                  |                                          |                |              |           |        |
|                                  | (STC).                                   |                |              |           |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``eta_overall``                  | Overall conversion efficiency from solar | 0.15           | —            | float     |        |
|                                  |                                          |                |              |           |        |
|                                  | radiation to electricity output at AC    |                |              |           |        |
|                                  |                                          |                |              |           |        |
|                                  | side.                                    |                |              |           |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``co2_intensity``                | Carbon-dioxide intensity of technology   | 0.0157         | kg CO2/kWh   | float     |        |
|                                  |                                          |                |              |           |        |
|                                  | output (annual average value).           |                |              |           |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``lifetime``                     | Expected lifetime of technology before   | 25             | years        | int       |        |
|                                  |                                          |                |              |           |        |
|                                  | replacement is required.                 |                |              |           |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``capex``                        | CAPEX cost of technology per unit of     | 3000           | CHF/kWp      | float     |        |
|                                  |                                          |                |              |           |        |
|                                  | capacity.                                |                |              |           |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``maintenance_cost``             | OPEX cost of the technology.             | 6.45           | CHF/kWp/year | float     |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``interest_rate``                | Interest rate for computing levelised    | 0.025          | —            | float     |        |
|                                  |                                          |                |              |           |        |
|                                  | costs (if required).                     |                |              |           |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``potential_integration_factor`` | Used for scenario 'pv_integration'. This | 0.3            | —            | float     |        |
|                                  |                                          |                |              |           |        |
|                                  | factor specifies the fraction of         |                |              |           |        |
|                                  |                                          |                |              |           |        |
|                                  | additional solar VP potential to be      |                |              |           |        |
|                                  |                                          |                |              |           |        |
|                                  | implemented. The additional PV potential |                |              |           |        |
|                                  |                                          |                |              |           |        |
|                                  | is based on suitable roof-space that is  |                |              |           |        |
|                                  |                                          |                |              |           |        |
|                                  | not yet covered with PV.                 |                |              |           |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``virtual_export_tariff``        | virtual export tarriff to prefer         | 0              | CHF/kWh      | float     |        |
|                                  |                                          |                |              |           |        |
|                                  | internal usage of the electricity        |                |              |           |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``export_subsidy``               | subsidy to make export more likely (and  | 0              | CHF/kWh      | float     |        |
|                                  |                                          |                |              |           |        |
|                                  | prevent cycling of storages to curtail   |                |              |           |        |
|                                  |                                          |                |              |           |        |
|                                  | energy)                                  |                |              |           |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``only_use_installed``           |                                          | False          | —            | bool      |        |
+----------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
