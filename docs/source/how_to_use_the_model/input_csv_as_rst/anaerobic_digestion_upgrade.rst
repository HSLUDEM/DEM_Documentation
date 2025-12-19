+----------------------+------------------------------------------+----------------+--------------+-----------+
| Attribute            | Description                              | Standard value | Unit         | Data type |
+======================+==========================================+================+==============+===========+
| ``deployment``       | If set to 'true', the technology will be | False          | —            | bool      |
|                      |                                          |                |              |           |
|                      | considered in the energy system model    |                |              |           |
|                      |                                          |                |              |           |
|                      | (this does not necessarily mean it will  |                |              |           |
|                      |                                          |                |              |           |
|                      | be used). Only relevant for              |                |              |           |
|                      |                                          |                |              |           |
|                      | optimisation.                            |                |              |           |
+----------------------+------------------------------------------+----------------+--------------+-----------+
| ``color``            | Color for plot                           | #FF00FF        | hex          | str       |
+----------------------+------------------------------------------+----------------+--------------+-----------+
| ``efficiancy``       | Conversion efficiency                    | 0.3            | —            | float     |
+----------------------+------------------------------------------+----------------+--------------+-----------+
| ``capacity_kW``      | maximum power                            | inf            | kWh          | float     |
+----------------------+------------------------------------------+----------------+--------------+-----------+
| ``co2_intensity``    | Carbon-dioxide intensity of technology   | 1.06           | kg CO2/kWh   | float     |
|                      |                                          |                |              |           |
|                      | output (annual average value).           |                |              |           |
+----------------------+------------------------------------------+----------------+--------------+-----------+
| ``lifetime``         | Expected lifetime of technology before   | 25             | years        | int       |
|                      |                                          |                |              |           |
|                      | replacement is required.                 |                |              |           |
+----------------------+------------------------------------------+----------------+--------------+-----------+
| ``om_cost``          | Operation and maintenance cost per       | 0              | CHF/kWh      | float     |
|                      |                                          |                |              |           |
|                      | consumed carrier unit                    |                |              |           |
+----------------------+------------------------------------------+----------------+--------------+-----------+
| ``capital_cost``     | CAPEX cost of technology per unit of     | 1053           | CHF/kWp      | float     |
|                      |                                          |                |              |           |
|                      | capacity.                                |                |              |           |
+----------------------+------------------------------------------+----------------+--------------+-----------+
| ``maintenance_cost`` | OPEX cost of technology per unit         | 10             | CHF/kWp/year | float     |
|                      |                                          |                |              |           |
|                      | capacity                                 |                |              |           |
+----------------------+------------------------------------------+----------------+--------------+-----------+
| ``interest_rate``    | Interest rate for computing levelised    | 0.025          | —            | float     |
|                      |                                          |                |              |           |
|                      | costs (if required).                     |                |              |           |
+----------------------+------------------------------------------+----------------+--------------+-----------+
