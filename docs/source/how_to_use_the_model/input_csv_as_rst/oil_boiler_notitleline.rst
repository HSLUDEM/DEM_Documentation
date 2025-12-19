+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| Attribute                        | Description                                          | Standard value | Unit         | Data type |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``deployment``                   | If set to 'true', the technology will be             | True           | —            | bool      |
|                                  |                                                      |                |              |           |
|                                  | considered in the energy system model                |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | (this does not necessarily mean it will              |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | be used). Only relevant for                          |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | optimisation.                                        |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``kW_th_max``                    | Maximum thermal capacity (i.e. heat                  | 'inf'          | kW           | float     |
|                                  |                                                      |                |              |           |
|                                  | output).                                             |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``hv_oil_MJpkg``                 | Lower heating value of oil.                          | 42.9           | MJ/kg        | float     |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``eta``                          | Conversion efficiency from fuel to heat.             | 0.85           | —            | float     |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``oil_price_CHFpl``              | Oil price (annual fixed value).                      | 1              | CHF/l        | float     |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``co2_intensity``                | Carbon-dioxide intensity of technology               | 0.301          | kg CO2/kWh   | float     |
|                                  |                                                      |                |              |           |
|                                  | output (annual average value).                       |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``lifetime``                     | Expected lifetime of technology before               | 25             | years        | int       |
|                                  |                                                      |                |              |           |
|                                  | replacement is required.                             |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``interest_rate``                | Interest rate for computing levelised                | 0.025          | —            | float     |
|                                  |                                                      |                |              |           |
|                                  | costs (if required).                                 |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``replacement_factor``           | Used for scenario                                    | 1              | —            | float     |
|                                  |                                                      |                |              |           |
|                                  | 'fossil_heater_retrofit'. Fraction of                |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | heating capacity to be replaced by heat              |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | pumps.                                               |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``capex``                        | CAPEX cost of technology per unit of                 | 3000           | CHF/kWp      | float     |
|                                  |                                                      |                |              |           |
|                                  | capacity.                                            |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``capex_one_to_one_replacement`` | CAPEX cost of technology per unit of                 | 1500           | CHF/kWp      | float     |
|                                  |                                                      |                |              |           |
|                                  | capacity (when device has reached the                |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | end of life)                                         |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``maintenance_cost``             | OPEX cost of technology.                             | 30             | CHF/kWp/year | float     |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``fixed_demand_share``           | If set to 'True', a fixed share (per                 | False          | —            | bool      |
|                                  |                                                      |                |              |           |
|                                  | timestep) of the total heat demand will              |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | be served by this tech. Only relevant if             |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | :ref:`optimisation` is activated.                    |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``fixed_demand_share_val``       | The share (per timestep) of the total                | 0              | —            | float     |
|                                  |                                                      |                |              |           |
|                                  | heat demand served by this technology.               |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | Only relevant if ``fixed_demand_share`` == True and  |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | if :ref:`optimisation` is activated.                 |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
| ``only_allow_existing``          | If set to 'True', only the existing                  | False          | —            | bool      |
|                                  |                                                      |                |              |           |
|                                  | (allready installed) capacity can be                 |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | used. Only relevant if                               |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | :ref:`optimisation` is activated.                    |                |              |           |
|                                  |                                                      |                |              |           |
|                                  | CAREFUL: Avoid conflict with ``fixed_demand_share``. |                |              |           |
+----------------------------------+------------------------------------------------------+----------------+--------------+-----------+
