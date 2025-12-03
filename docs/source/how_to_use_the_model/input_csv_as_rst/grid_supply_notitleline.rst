+----------------+------------------------------------------+----------------+------------+-----------+--------+
| Attribute      | Description                              | Standard value | Unit       | Data type | Source |
+----------------+------------------------------------------+----------------+------------+-----------+--------+
| deployment     | If set to 'true', the technology will be | True           | —          | bool      |        |
|                |                                          |                |            |           |        |
|                | considered in the energy system model    |                |            |           |        |
|                |                                          |                |            |           |        |
|                | (this does not necessarily mean it will  |                |            |           |        |
|                |                                          |                |            |           |        |
|                | be used). Only relevant for              |                |            |           |        |
|                |                                          |                |            |           |        |
|                | optimisation.                            |                |            |           |        |
+----------------+------------------------------------------+----------------+------------+-----------+--------+
| kW_max         | Maximum supply capacity of grid          | inf            | kW         | float     |        |
|                |                                          |                |            |           |        |
|                | connection.                              |                |            |           |        |
+----------------+------------------------------------------+----------------+------------+-----------+--------+
| tariff_CHFpkWh | Electricity tariff (annual fixed value). | 0.29           | CHF/kWh    | float     |        |
+----------------+------------------------------------------+----------------+------------+-----------+--------+
| co2_intensity  | Carbon-dioxide intensity of technology   | 0.128          | kg CO2/kWh | float     |        |
|                |                                          |                |            |           |        |
|                | output (annual average value).           |                |            |           |        |
+----------------+------------------------------------------+----------------+------------+-----------+--------+
| lifetime       | Expected lifetime of technology before   | 25             | years      | int       |        |
|                |                                          |                |            |           |        |
|                | replacement is required.                 |                |            |           |        |
+----------------+------------------------------------------+----------------+------------+-----------+--------+
| interest_rate  | Interest rate for computing levelised    | 0.025          | —          | float     |        |
|                |                                          |                |            |           |        |
|                | costs (if required).                     |                |            |           |        |
+----------------+------------------------------------------+----------------+------------+-----------+--------+
