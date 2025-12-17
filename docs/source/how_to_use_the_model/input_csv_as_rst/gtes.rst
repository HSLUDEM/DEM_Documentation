+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| Attribute                       | Description                              | Standard value | Unit         | Data type | Source |
+=================================+==========================================+================+==============+===========+========+
| ``deployment``                  | If set to 'true', the technology will be | True           | —            | bool      |        |
|                                 |                                          |                |              |           |        |
|                                 | considered in the energy system model    |                |              |           |        |
|                                 |                                          |                |              |           |        |
|                                 | (this does not necessarily mean it will  |                |              |           |        |
|                                 |                                          |                |              |           |        |
|                                 | be used). Only relevant for              |                |              |           |        |
|                                 |                                          |                |              |           |        |
|                                 | optimisation.                            |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``force_asynchronous_prod_con`` | If set to 'true', the storage cannot be  | True           | —            | bool      |        |
|                                 |                                          |                |              |           |        |
|                                 | charged and discharged simultaneously    |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``eta_chg_dchg``                | Charging and discharging efficiency      | 0.95           | —            | float     |        |
|                                 |                                          |                |              |           |        |
|                                 | (fixed). Roundtrip-efficiency is         |                |              |           |        |
|                                 |                                          |                |              |           |        |
|                                 | calculated as eta_chg_dchg*eta_chg_dchg. |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``gtes_gamma``                  | Loss rate: fraction of gas lost during   | 0              | 1/timestep   | float     |        |
|                                 |                                          |                |              |           |        |
|                                 | one timestep (e.g. 1 hour)               |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``capacity_kWh``                | Storage capacity.                        | inf            | kWh          | str       |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``chg_dchg_per_cap_max``        | Max. charge/discharge (kW) per storage   | 0.1            | 1/timestep   | float     |        |
|                                 |                                          |                |              |           |        |
|                                 | cap (kWh) per timestep.                  |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``initial_charge``              | Initial charge of gas tank (fraction of  | 0              | —            | float     |        |
|                                 |                                          |                |              |           |        |
|                                 | total storage capacity)                  |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``optimized_initial_charge``    | If True, initial_charge is determined    | True           | —            | bool      |        |
|                                 |                                          |                |              |           |        |
|                                 | within the optimization s.t. the initial |                |              |           |        |
|                                 |                                          |                |              |           |        |
|                                 | charge and the final charge are the same |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``co2_intensity``               | Carbon-dioxide intensity of technology   | 0              | kg CO2/kWh   | float     |        |
|                                 |                                          |                |              |           |        |
|                                 | output (annual average value).           |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``lifetime``                    | Expected lifetime of technology before   | 25             | years        | int       |        |
|                                 |                                          |                |              |           |        |
|                                 | replacement is required.                 |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``interest_rate``               | Interest rate for computing levelised    | 0.025          | —            | float     |        |
|                                 |                                          |                |              |           |        |
|                                 | costs (if required).                     |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``capex``                       | CAPEX cost of technology per unit of     | 0.2            | CHF/kWh      | float     |        |
|                                 |                                          |                |              |           |        |
|                                 | capacity.                                |                |              |           |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``maintenance_cost``            | OPEX of the technology                   | 0.01           | CHF/kWh/year | float     |        |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
