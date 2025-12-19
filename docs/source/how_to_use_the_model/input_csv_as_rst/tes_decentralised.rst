+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| Attribute                       | Description                              | Standard value | Unit         | Data type |
+=================================+==========================================+================+==============+===========+
| ``deployment``                  | If set to 'true', the technology will be | False          | —            | bool      |
|                                 |                                          |                |              |           |
|                                 | considered in the energy system model    |                |              |           |
|                                 |                                          |                |              |           |
|                                 | (this does not necessarily mean it will  |                |              |           |
|                                 |                                          |                |              |           |
|                                 | be used). Only relevant for              |                |              |           |
|                                 |                                          |                |              |           |
|                                 | optimisation.                            |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``force_asynchronous_prod_con`` | If set to 'true', the tes cannot be      | True           | —            | bool      |
|                                 |                                          |                |              |           |
|                                 | charged and discharged simultaneously    |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``eta_chg_dchg``                | Charging and discharging efficiency      | 0.95           | —            | float     |
|                                 |                                          |                |              |           |
|                                 | (fixed). Roundtrip-efficiency is         |                |              |           |
|                                 |                                          |                |              |           |
|                                 | calculated as eta_chg_dchg*eta_chg_dchg. |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``tes_gamma``                   | Loss rate: fraction of heat lost to the  | 0.001          | 1/timestep   | float     |
|                                 |                                          |                |              |           |
|                                 | environment during one timestep (e.g. 1  |                |              |           |
|                                 |                                          |                |              |           |
|                                 | hour)                                    |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``capacity_kWh``                | Storage capacity.                        | inf            | kWh          | float     |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``chg_dchg_per_cap_max``        | Max. charge/discharge (kW) per storage   | 0.1            | 1/timestep   | float     |
|                                 |                                          |                |              |           |
|                                 | cap (kWh) per timestep.                  |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``initial_charge``              | Initial charge of storage (fraction of   | 0              | —            | float     |
|                                 |                                          |                |              |           |
|                                 | total storage capacity)                  |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``optimized_initial_charge``    | If True, initial_charge is determined    | True           | —            | bool      |
|                                 |                                          |                |              |           |
|                                 | within the optimization s.t. the initial |                |              |           |
|                                 |                                          |                |              |           |
|                                 | charge and the final charge are the same |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``connections``                 | Technologies connected to TES can be     |                | —            | dict      |
|                                 |                                          |                |              |           |
|                                 | switched on (True) of off (False).       |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``connections: heat_pump``      | If set to 'true', decentralised heat     | True           | —            | bool      |
|                                 |                                          |                |              |           |
|                                 | pumps are connected to TES. Technology   |                |              |           |
|                                 |                                          |                |              |           |
|                                 | must be deployed accordingly.            |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``connections: solar_thermal``  | If set to 'true', decentralised heat     | True           | —            | bool      |
|                                 |                                          |                |              |           |
|                                 | pumps are connected to TES. Technology   |                |              |           |
|                                 |                                          |                |              |           |
|                                 | must be deployed accordingly.            |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``co2_intensity``               | Carbon-dioxide intensity of technology   | 0              | kg CO2/kWh   | float     |
|                                 |                                          |                |              |           |
|                                 | output (annual average value).           |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``lifetime``                    | Expected lifetime of technology before   | 25             | years        | int       |
|                                 |                                          |                |              |           |
|                                 | replacement is required.                 |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``capex``                       |                                          | 3              | CHF/kWh      |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``maintenance_cost``            | OPEX cost of technology                  | 0.02           | CHF/kWh/year | float     |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
| ``interest_rate``               | Interest rate for computing levelised    | 0.025          | —            | float     |
|                                 |                                          |                |              |           |
|                                 | costs (if required).                     |                |              |           |
+---------------------------------+------------------------------------------+----------------+--------------+-----------+
