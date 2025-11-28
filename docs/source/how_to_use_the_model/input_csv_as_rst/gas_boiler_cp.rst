+-------------------+--------------------------+-----------+------------------------------------------+
| Attribute         | Unit                     | Data type | Description                              |
+===================+==========================+===========+==========================================+
| deployment        | —                        | bool      | If set to 'true', the technology will be |
|                   |                          |           |                                          |
|                   |                          |           | considered in the energy system model    |
|                   |                          |           |                                          |
|                   |                          |           | (this does not necessarily mean it will  |
|                   |                          |           |                                          |
|                   |                          |           | be used). Only relevant for              |
|                   |                          |           |                                          |
|                   |                          |           | optimisation.                            |
+-------------------+--------------------------+-----------+------------------------------------------+
| kW_th_max         | Maximum thermal capacity | str       | Maximum thermal power output             |
+-------------------+--------------------------+-----------+------------------------------------------+
| hv_gas_MJpkg      | MJ/kg                    | float     | heating value of gas in MJ per kg        |
+-------------------+--------------------------+-----------+------------------------------------------+
| eta               | —                        | float     | Conversion efficiency from gas to heat   |
+-------------------+--------------------------+-----------+------------------------------------------+
| gas_price_CHFpkWh | CHF/kWh                  | float     |                                          |
+-------------------+--------------------------+-----------+------------------------------------------+
| co2_intensity     | kg CO2/kWh               | float     | Carbon-dioxide intensity of technology   |
|                   |                          |           |                                          |
|                   |                          |           | output (annual average value).           |
+-------------------+--------------------------+-----------+------------------------------------------+
| lifetime          | years                    | int       | Expected lifetime of technology before   |
|                   |                          |           |                                          |
|                   |                          |           | replacement is required.                 |
+-------------------+--------------------------+-----------+------------------------------------------+
| interest_rate     | —                        | float     | Interest rate for computing levelised    |
|                   |                          |           |                                          |
|                   |                          |           | costs (if required).                     |
+-------------------+--------------------------+-----------+------------------------------------------+
| capex             | CHF/kW                   | int       | CAPEX cost of technology per unit of     |
|                   |                          |           |                                          |
|                   |                          |           | capacity.                                |
+-------------------+--------------------------+-----------+------------------------------------------+
| maintenance_cost  | CHF/kW/year              | float     | OPEX cost of technology per unit of      |
|                   |                          |           |                                          |
|                   |                          |           | capacity.                                |
+-------------------+--------------------------+-----------+------------------------------------------+
