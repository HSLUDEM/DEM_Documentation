+-----------------------------+--------------+-----------+------------------------------------------+
| Attribute                   | Unit         | Data type | Description                              |
+=============================+==============+===========+==========================================+
| deployment                  | —            | bool      | If set to 'true', the technology will be |
|                             |              |           |                                          |
|                             |              |           | considered in the energy system model    |
|                             |              |           |                                          |
|                             |              |           | (this does not necessarily mean it will  |
|                             |              |           |                                          |
|                             |              |           | be used). Only relevant for              |
|                             |              |           |                                          |
|                             |              |           | optimisation.                            |
+-----------------------------+--------------+-----------+------------------------------------------+
| force_asynchronous_prod_con | —            | bool      | If set to 'true', the tes cannot be      |
|                             |              |           |                                          |
|                             |              |           | charged and discharged simultaneously    |
+-----------------------------+--------------+-----------+------------------------------------------+
| eta_chg_dchg                | —            | float     | Charging and discharging efficiency      |
|                             |              |           |                                          |
|                             |              |           | (fixed). Roundtrip-efficiency is         |
|                             |              |           |                                          |
|                             |              |           | calculated as eta_chg_dchg*eta_chg_dchg. |
+-----------------------------+--------------+-----------+------------------------------------------+
| bes_gamma                   | 1/timestep   | float     | Loss rate: fraction of electricity lost  |
|                             |              |           |                                          |
|                             |              |           | during one timestep (e.g. 1 hour)        |
+-----------------------------+--------------+-----------+------------------------------------------+
| capacity_kWh                | kWh          | float     | Storage capacity.                        |
+-----------------------------+--------------+-----------+------------------------------------------+
| chg_dchg_per_cap_max        | 1/timestep   | float     | Max. charge/discharge (kW) per storage   |
|                             |              |           |                                          |
|                             |              |           | cap (kWh) per timestep.                  |
+-----------------------------+--------------+-----------+------------------------------------------+
| initial_charge              | —            | float     | Initial charge of battery (fraction of   |
|                             |              |           |                                          |
|                             |              |           | total storage capacity)                  |
+-----------------------------+--------------+-----------+------------------------------------------+
| optimized_initial_charge    | —            | bool      |                                          |
+-----------------------------+--------------+-----------+------------------------------------------+
| co2_intensity               | kg CO2/kWh   | float     | Carbon-dioxide intensity of technology   |
|                             |              |           |                                          |
|                             |              |           | output (annual average value).           |
+-----------------------------+--------------+-----------+------------------------------------------+
| lifetime                    | years        | int       | Expected lifetime of technology before   |
|                             |              |           |                                          |
|                             |              |           | replacement is required.                 |
+-----------------------------+--------------+-----------+------------------------------------------+
| interest_rate               | —            | float     | Interest rate for computing levelised    |
|                             |              |           |                                          |
|                             |              |           | costs (if required).                     |
+-----------------------------+--------------+-----------+------------------------------------------+
| capex                       | CHF/kWh      |           | CAPEX cost of technology per unit of     |
|                             |              |           |                                          |
|                             |              |           | capacity.                                |
+-----------------------------+--------------+-----------+------------------------------------------+
| maintenance_cost            | CHF/kWh/year | float     | OPEX of the technology                   |
+-----------------------------+--------------+-----------+------------------------------------------+
