+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| Attribute                        | Description                                         | Standard value                        | Unit         | Data type |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``deployment``                   | If set to 'true', the technology will be            | True                                  | —            | bool      |
|                                  |                                                     |                                       |              |           |
|                                  | considered in the energy system model               |                                       |              |           |
|                                  |                                                     |                                       |              |           |
|                                  | (this does not necessarily mean it will             |                                       |              |           |
|                                  |                                                     |                                       |              |           |
|                                  | be used). Only relevant for                         |                                       |              |           |
|                                  |                                                     |                                       |              |           |
|                                  | optimisation.                                       |                                       |              |           |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``kW_max``                       | Maximum thermal capacity (i.e. heat                 | inf'                                  | kW           | float     |
|                                  |                                                     |                                       |              |           |
|                                  | output).                                            |                                       |              |           |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``co2_intensity``                | Carbon-dioxide intensity of technology              | 0 *(emissons allocated to electricity | kg CO2/kWh   | float     |
|                                  |                                                     |                                       |              |           |
|                                  | output (annual average value).                      | tech)*                                |              |           |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``lifetime``                     | Expected lifetime of technology before              | 25                                    | years        | int       |
|                                  |                                                     |                                       |              |           |
|                                  | replacement is required.                            |                                       |              |           |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``interest_rate``                | Interest rate for computing levelised               | 0.025                                 | —            | float     |
|                                  |                                                     |                                       |              |           |
|                                  | costs (if required).                                |                                       |              |           |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``replacement_factor``           | share of electric heaters replaced in               | 1                                     | —            | float     |
|                                  |                                                     |                                       |              |           |
|                                  | fossil_heater_retrofit scenario                     |                                       |              |           |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``capex``                        | CAPEX cost of technology per unit of                | 0                                     | CHF/kWp      | float     |
|                                  |                                                     |                                       |              |           |
|                                  | capacity.                                           |                                       |              |           |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``capex_one_to_one_replacement`` | CAPEX cost of technology per unit of                | 500                                   | CHF/kWp      | float     |
|                                  |                                                     |                                       |              |           |
|                                  | capacity (when device has reached the               |                                       |              |           |
|                                  |                                                     |                                       |              |           |
|                                  | end of life)                                        |                                       |              |           |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``maintenance_cost``             | OPEX cost of technology.                            | 0                                     | CHF/kWp/year | float     |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``fixed_demand_share``           | If set to 'True', a fixed share (per                | False                                 | —            | bool      |
|                                  |                                                     |                                       |              |           |
|                                  | timestep) of the total heat demand will             |                                       |              |           |
|                                  |                                                     |                                       |              |           |
|                                  | be served by this tech. Only relevant if            |                                       |              |           |
|                                  |                                                     |                                       |              |           |
|                                  | :ref:`optimisation` is activated.                   |                                       |              |           |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
| ``fixed_demand_share_val``       | The share (per timestep) of the total               | 0                                     | —            | float     |
|                                  |                                                     |                                       |              |           |
|                                  | heat demand served by this technology.              |                                       |              |           |
|                                  |                                                     |                                       |              |           |
|                                  | Only relevant if ``fixed_demand_share`` == True and |                                       |              |           |
|                                  |                                                     |                                       |              |           |
|                                  | if :ref:`optimisation` is activated.                |                                       |              |           |
+----------------------------------+-----------------------------------------------------+---------------------------------------+--------------+-----------+
