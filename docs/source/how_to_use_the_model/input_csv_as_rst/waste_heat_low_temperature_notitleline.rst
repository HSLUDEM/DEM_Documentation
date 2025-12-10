+----------------------+------------------------------------------+----------------+-------------+-----------+--------+
| Attribute            | Description                              | Standard value | Unit        | Data type | Source |
+----------------------+------------------------------------------+----------------+-------------+-----------+--------+
| deployment           | If set to 'true', the technology will be | True           | —           | bool      |        |
|                      |                                          |                |             |           |        |
|                      | considered in the energy system model    |                |             |           |        |
|                      |                                          |                |             |           |        |
|                      | (this does not necessarily mean it will  |                |             |           |        |
|                      |                                          |                |             |           |        |
|                      | be used). Only relevant for              |                |             |           |        |
|                      |                                          |                |             |           |        |
|                      | optimisation.                            |                |             |           |        |
+----------------------+------------------------------------------+----------------+-------------+-----------+--------+
| capex                | CAPEX cost of technology per unit of     | 0              | CHF/kW      | float     |        |
|                      |                                          |                |             |           |        |
|                      | capacity.                                |                |             |           |        |
+----------------------+------------------------------------------+----------------+-------------+-----------+--------+
| maintenance_cost     | OPEX cost of technology per unit of      | 0              | CHF/kW/year | float     |        |
|                      |                                          |                |             |           |        |
|                      | capacity.                                |                |             |           |        |
+----------------------+------------------------------------------+----------------+-------------+-----------+--------+
| lifetime             | Expected lifetime of technology before   | 25             | years       | int       |        |
|                      |                                          |                |             |           |        |
|                      | replacement is required.                 |                |             |           |        |
+----------------------+------------------------------------------+----------------+-------------+-----------+--------+
| timeseries_file_path | Path to file with waste heat timeseries  | ''             | —           | str       |        |
|                      |                                          |                |             |           |        |
|                      | (in kWh/h)                               |                |             |           |        |
+----------------------+------------------------------------------+----------------+-------------+-----------+--------+
| co2_intensity        | Carbon-dioxide intensity of technology   | 0              | kg CO2/kWh  | float     |        |
|                      |                                          |                |             |           |        |
|                      | output (annual average value).           |                |             |           |        |
+----------------------+------------------------------------------+----------------+-------------+-----------+--------+
| tariff_CHFpkWh       | Cost of waste heat                       | 0.01           | CHF/kWh     | float     |        |
+----------------------+------------------------------------------+----------------+-------------+-----------+--------+
| interest_rate        | Interest rate for computing levelised    | 0.025          | —           | float     |        |
|                      |                                          |                |             |           |        |
|                      | costs (if required).                     |                |             |           |        |
+----------------------+------------------------------------------+----------------+-------------+-----------+--------+
