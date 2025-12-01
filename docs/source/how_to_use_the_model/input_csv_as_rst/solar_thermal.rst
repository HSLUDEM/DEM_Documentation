+------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| Attribute                    | Description                              | Standard value | Unit         | Data type | Source |
+==============================+==========================================+================+==============+===========+========+
| deployment                   | If set to 'true', the technology will be | True           | —            | bool      |        |
|                              |                                          |                |              |           |        |
|                              | considered in the energy system model    |                |              |           |        |
|                              |                                          |                |              |           |        |
|                              | (this does not necessarily mean it will  |                |              |           |        |
|                              |                                          |                |              |           |        |
|                              | be used). Only relevant for              |                |              |           |        |
|                              |                                          |                |              |           |        |
|                              | optimisation.                            |                |              |           |        |
+------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| kW_th_max                    | Maximum thermal capacity (i.e. heat      | inf            | kW           | float     |        |
|                              |                                          |                |              |           |        |
|                              | output).                                 |                |              |           |        |
+------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| eta_overall                  | Overall conversion efficiency from solar | 0.7            | —            | float     |        |
|                              |                                          |                |              |           |        |
|                              | radiation to heat output.                |                |              |           |        |
+------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| co2_intensity                | Carbon-dioxide intensity of technology   | 0.025          | kg CO2/kWh   | float     |        |
|                              |                                          |                |              |           |        |
|                              | output (annual average value).           |                |              |           |        |
+------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| lifetime                     | Expected lifetime of technology before   | 25             | years        | int       |        |
|                              |                                          |                |              |           |        |
|                              | replacement is required.                 |                |              |           |        |
+------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| interest_rate                | Interest rate for computing levelised    | 0.025          | —            | float     |        |
|                              |                                          |                |              |           |        |
|                              | costs (if required).                     |                |              |           |        |
+------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| capex                        | CAPEX cost of technology per unit of     | 2857           | CHF/kWp      | float     |        |
|                              |                                          |                |              |           |        |
|                              | capacity.                                |                |              |           |        |
+------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| capex_one_to_one_replacement | CAPEX cost of technology per unit of     | 1000           | CHF/kWp      | float     |        |
|                              |                                          |                |              |           |        |
|                              | capacity (when device has reached the    |                |              |           |        |
|                              |                                          |                |              |           |        |
|                              | end of life)                             |                |              |           |        |
+------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| maintenance_cost             | OPEX cost of technology.                 | 10             | CHF/kWp/year | float     |        |
+------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
