+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| Attribute                        | Description                              | Standard value                        | Unit         | Data type |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``deployment``                   | If set to 'true', the technology will be | True                                  | —            | bool      |
|                                  |                                          |                                       |              |           |
|                                  | considered in the energy system model    |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | (this does not necessarily mean it will  |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | be used). Only relevant for              |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | optimisation.                            |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``kW_th_max``                    | Maximum thermal capacity (i.e. heat      | inf                                   | kW           | str       |
|                                  |                                          |                                       |              |           |
|                                  | output).                                 |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``co2_intensity``                | Carbon-dioxide intensity of technology   | 0 *(emissons allocated to electricity | kg CO2/kWh   | float     |
|                                  |                                          |                                       |              |           |
|                                  | output (annual average value).           | tech)*                                |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``lifetime``                     | Expected lifetime of technology before   | 25                                    | years        | int       |
|                                  |                                          |                                       |              |           |
|                                  | replacement is required.                 |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``interest_rate``                | Interest rate for computing levelised    | 0.025                                 | —            | float     |
|                                  |                                          |                                       |              |           |
|                                  | costs (if required).                     |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``capex``                        | CAPEX cost of technology per unit of     | 6000                                  | CHF/kWp      | float     |
|                                  |                                          |                                       |              |           |
|                                  | capacity (new installations).            |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``capex_one_to_one_replacement`` | CAPEX cost of technology per unit of     | 2000                                  | CHF/kWp      | float     |
|                                  |                                          |                                       |              |           |
|                                  | capacity (when device has reached the    |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | end of life).                            |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``maintenance_cost``             | OPEX cost of technology.                 | 10                                    | CHF/kWp/year | float     |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``fixed_demand_share``           |                                          | False                                 |              | bool      |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``fixed_demand_share_val``       |                                          | 0                                     |              | float     |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``only_allow_existing``          | If True, only existing heat pumps are    | False                                 | —            | bool      |
|                                  |                                          |                                       |              |           |
|                                  | allowed to continue to operate.          |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``cop_mode``                     | Method for estimating the COP            | location_based                        | —            | str       |
|                                  |                                          |                                       |              |           |
|                                  | timeseries. Options are: “from_file”,    |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | “constant”, “from_file_adjusted_to_spf”, |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | “location_based”. “location_based” is an |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | intricate algorithm taking into account  |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | building and heat pump properties as     |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | well as the local weather (detailed      |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | description below). “constant” means     |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | that a constant COP is used. “from_file” |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | means means that a timeseries loaded     |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | from a given file is used.               |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | “from_file_adjusted_to_spf” means that a |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | timeseries loaded form a file is is      |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | scaled s.t. a given value for the        |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | seasonal performance factor (SPF) is     |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | reached                                  |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``cop_timeseries_file_path``     | Path to COP timeseries file for mode     | <path>                                | <path>       | str       |
|                                  |                                          |                                       |              |           |
|                                  | “form_file” and                          |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | “from_file_adjusted_to_spf”              |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``cop_constant_value``           | Constant COP value to use if             | 3.5                                   | —            | float     |
|                                  |                                          |                                       |              |           |
|                                  | cop_mode=constant                        |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``spf_to_target``                | Seasonal performance factor (SPF) to     | 3.5                                   | —            | float     |
|                                  |                                          |                                       |              |           |
|                                  | which the COP is adjusted in the mode    |                                       |              |           |
|                                  |                                          |                                       |              |           |
|                                  | from_file_adjusted_spf                   |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``quality_factor_ashp_new``      | Quality factor for new ASHPs for mode    | 0.4                                   | —            | float     |
|                                  |                                          |                                       |              |           |
|                                  | “location_based”.                        |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``quality_factor_ashp_old``      | Quality factor for old ASHPs for mode    | 0.4                                   | —            | float     |
|                                  |                                          |                                       |              |           |
|                                  | “location_based”.                        |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``quality_factor_gshp_new``      | Quality factor for new GSHPs for mode    | 0.48                                  | —            | float     |
|                                  |                                          |                                       |              |           |
|                                  | “location_based”.                        |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
| ``quality_factor_gshp_old``      | Quality factor for old GSHPs for mode    | 0.48                                  | —            | float     |
|                                  |                                          |                                       |              |           |
|                                  | “location_based”.                        |                                       |              |           |
+----------------------------------+------------------------------------------+---------------------------------------+--------------+-----------+
