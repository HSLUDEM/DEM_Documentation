+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| Attribute                             | Description                              | Standard value | Unit         | Data type | Source |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| deployment                            | If set to 'true', the technology will be | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | considered in the energy system model    |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | (this does not necessarily mean it will  |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | be used). Only relevant for              |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | optimisation.                            |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| force_asynchronous_prod_con           | If set to 'true', the tes cannot be      | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | charged and discharged simultaneously    |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| eta_chg_dchg                          | Charging and discharging efficiency      | 0.95           | —            | float     |        |
|                                       |                                          |                |              |           |        |
|                                       | (fixed). Roundtrip-efficiency is         |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | calculated as eta_chg_dchg*eta_chg_dchg. |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| tes_gamma                             | Loss rate: fraction of heat lost to the  | 0.001          | 1/timestep   | float     |        |
|                                       |                                          |                |              |           |        |
|                                       | environment during one timestep (e.g. 1  |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | hour)                                    |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| capacity_kWh                          | Storage capacity.                        | inf            | kWh          | float     |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| force_cap_max                         |                                          | False          |              | bool      |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| chg_dchg_per_cap_max                  | Max. charge/discharge (kW) per storage   | 0.1            | 1/timestep   | float     |        |
|                                       |                                          |                |              |           |        |
|                                       | cap (kWh) per timestep.                  |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| initial_charge                        | Initial charge of storage (fraction of   | 0              | —            | float     |        |
|                                       |                                          |                |              |           |        |
|                                       | total storage capacity)                  |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| optimized_initial_charge              | If True, initial_charge is determined    | True           |              | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | within the optimization s.t. the initial |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | charge and the final charge are the same |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections                           | Technologies connected to TES can be     |                | —            | dict      |        |
|                                       |                                          |                |              |           |        |
|                                       | switched on (True) of off (False).       |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: district_heating_network | If set to 'true', the district heating   | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | network is connected to TES. Technology  |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | must be deployed accordingly.            |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: district_heat_import     | If set to 'true', district_heat_import   | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | is connected to TES. Technology must be  |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | deployed accordingly.                    |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: chp_gt                   | If set to 'true', the CHP gas turbine is | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | connected to TES. Technology must be     |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | deployed accordingly.                    |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: steam_turbine            | If set to 'true', the steam turbine is   | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | connected to TES. Technology must be     |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | deployed accordingly.                    |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: waste_to_energy          | If set to 'true', the waset-to-energy    | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | plant is connected to TES. Technology    |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | must be deployed accordingly.            |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: oil_boiler_cp            | If set to 'true', a centralised oil      | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | boiler is connected to TES. Technology   |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | must be deployed accordingly.            |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: electric_heater_cp       | If set to 'true', a centralised electric | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | heater is connected to TES. Technology   |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | must be deployed accordingly.            |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: wood_boiler_cp           | If set to 'true', a centralised wood     | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | boiler is connected to TES. Technology   |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | must be deployed accordingly.            |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: gas_boiler_cp            | If set to 'true', a centralised gas      | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | boiler is connected to TES. Technology   |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | must be deployed accordingly.            |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: heat_pump_cp             | If set to 'true', a centralised heat     | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | pump is connected to TES. Technology     |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | must be deployed accordingly.            |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: heat_pump_cp_lt          | If set to 'true', a centralised heat     | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | pump converting low-temperature waste    |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | heat to high-temperature useful heat is  |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | connected to TES. Technology must be     |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | deployed accordingly.                    |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: waste_heat               | If set to 'true', a waste heat source is | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | connected to TES. Technology must be     |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | deployed accordingly.                    |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| connections: biomass                  | If set to 'true', a biomass technologies | True           | —            | bool      |        |
|                                       |                                          |                |              |           |        |
|                                       | are connected to TES. Technology must be |                |              |           |        |
|                                       |                                          |                |              |           |        |
|                                       | deployed accordingly.                    |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| co2_intensity                         | Carbon-dioxide intensity of technology   | 0              | kg CO2/kWh   | float     |        |
|                                       |                                          |                |              |           |        |
|                                       | output (annual average value).           |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| lifetime                              | Expected lifetime of technology before   | 25             | years        | int       |        |
|                                       |                                          |                |              |           |        |
|                                       | replacement is required.                 |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| capex                                 | CAPEX of TES per kWh capacity            | 1.67           | CHF/kWh      | float     |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| maintenance_cost                      | OPEX of TES per kWh capacity and year    | 0              | CHF/kWh/year | float     |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| interest_rate                         | Interest rate for computing levelised    | 0.025          | —            | float     |        |
|                                       |                                          |                |              |           |        |
|                                       | costs (if required).                     |                |              |           |        |
+---------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
