+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| Attribute              | Description                              | Standard value | Unit         | Data type | Source |
+========================+==========================================+================+==============+===========+========+
| deployment             | If set to 'true', the technology will be | True           | —            | bool      |        |
|                        |                                          |                |              |           |        |
|                        | considered in the energy system model    |                |              |           |        |
|                        |                                          |                |              |           |        |
|                        | (this does not necessarily mean it will  |                |              |           |        |
|                        |                                          |                |              |           |        |
|                        | be used). Only relevant for              |                |              |           |        |
|                        |                                          |                |              |           |        |
|                        | optimisation.                            |                |              |           |        |
+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| kWp_max                | Kilowatt Peak: Maximum power output of   | inf            | kW           | float     |        |
|                        |                                          |                |              |           |        |
|                        | hydro power plants.                      |                |              |           |        |
+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| existing_decentralised |                                          | True           |              | bool      |        |
+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| co2_intensity          | Carbon-dioxide intensity of technology   | 0              | kg CO2/kWh   | float     |        |
|                        |                                          |                |              |           |        |
|                        | output (annual average value).           |                |              |           |        |
+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| lifetime               | Expected lifetime of technology before   | 25             | years        | int       |        |
|                        |                                          |                |              |           |        |
|                        | replacement is required.                 |                |              |           |        |
+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| capex                  | CAPEX cost of technology per unit of     | 0              | CHF/kWp      | float     |        |
|                        |                                          |                |              |           |        |
|                        | capacity.                                |                |              |           |        |
+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| maintenance_cost       | OPEX cost of technology.                 | 130            | CHF/kWp/year | float     |        |
+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| interest_rate          | Interest rate for computing levelised    |                | —            | float     |        |
|                        |                                          |                |              |           |        |
|                        | costs (if required).                     |                |              |           |        |
+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| virtual_export_tariff  | virtual export tarriff to prefer         | 0              | CHF/kWh      | float     |        |
|                        |                                          |                |              |           |        |
|                        | internal usage of the electricity        |                |              |           |        |
+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| export_subsidy         | subsidy to make export more likely (and  | 0              | CHF/kWh      | float     |        |
|                        |                                          |                |              |           |        |
|                        | prevent cycling of storages to curtail   |                |              |           |        |
|                        |                                          |                |              |           |        |
|                        | energy)                                  |                |              |           |        |
+------------------------+------------------------------------------+----------------+--------------+-----------+--------+
