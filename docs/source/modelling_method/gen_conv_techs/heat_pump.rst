Heat Pump
=======================================

A heat pump is a device that uses work to transport environmental heat into heat at a useful 
temperature level. In our model, we have electric heat pumps available as a technology.

The heat pump technology models a small to medium size heat pump located in a building.

The power available to the heating system is given by the electric input power multiplied
with the coefficient of performance (COP).
::math P_\\text{out} = \\text{COP} \\cdot P_\\text{elec}

Our model contains a module for the detailed modeling of the COP based on properties 
of the building and the heat pumps. For this, there are plenty of parameters in the input 
file.

+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| Name                          | Standard value  | Description                                                                 |
+===============================+=================+=============================================================================+
| deployment                    | True            | Are heat pumps deployed in the energy system?                               |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| kW_th_max                     | 'inf'           | Maximum power of the heat pumps                                             |
|                               |                 |                                                                             | 
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| co2_intensity                 | 0               | CO2 intensity of heat pumps (per kWh heat produced).                        |
|                               |                 | CO2 for electricity used is already accounted for via electricity           | 
|                               |                 | import CO2 intensity.                                                       | 
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| lifetime                      | 25              | Lifetime of the heat pumps.       (in years)                                |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| interest_rate                 | global variable | Interest rate used for cost calculation. Usually a global variable          |
|                               |                 | (the same for all technologies.)                                            | 
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| capex                         | 6000            | Capex for building new heat pumps (per kW)      CHF/kW                      |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| capex_one_to_one_replacement  | 2000            | Capex for replacing a heat pump by a new heat pump CHF/kW.                  |
|                               |                 | (i.e. only replacing the heat pump by a newer one)                          | 
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| maintenance_cost              | 10              | Maintenance cost of the heat pump CHF/kW/year                               |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| fixed_demand_share            | False           |                                                                             |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| fixed_demand_share_val        | 0.0             |                                                                             |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| only_allow_existing           | False           | If True, only existing heat pumps are allowed to continue to operate.       |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| cop_mode                      | "location_based"| Method for estimating the COP timeseries.                                   |
|                               |                 | Options are: "from_file", "constant",                                       | 
|                               |                 | "from_file_adjusted_to_spf", "location_based".                              | 
|                               |                 | "location_based" is an intricate algorithm taking into account building     | 
|                               |                 | and heat pump properties as well as the local weather (detailed description | 
|                               |                 | below). "constant" means that a constant COP is used. "from_file" means     | 
|                               |                 | means that a timeseries loaded from a given file is used.                   | 
|                               |                 | "from_file_adjusted_to_spf" means that a timeseries loaded form a file is   | 
|                               |                 | is scaled s.t. a given value for the seasonal performance factor (SPF)      | 
|                               |                 | is reached                                                                  | 
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| cop_timeseries_file_path      | ""              | |Path to COP timeseries file for mode "form_file"                          ||
|                               |                 | | and "from_file_adjusted_to_spf"                                          || 
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| cop_constant_value            | 3.0             | Constant COP value for COP mode "constant"                                  |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| spf_to_target                 | 4.0             | SPF for COP mode "from_file_adjusted_to_spf"                                |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| quality_factor_ashp_new       | 0.4             | Quality factor for new ASHPs for mode "location_based".                     |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| quality_factor_ashp_old       | 0.4             | Quality factor for old ASHPs for mode "location_based".                     |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| quality_factor_gshp_new       | 0.48            | Quality factor for new GSHPs for mode "location_based".                     |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+
| quality_factor_gshp_old       | 0.48            | Quality factor for old GSHPs for mode "location_based".                     |
+-------------------------------+-----------------+-----------------------------------------------------------------------------+


COP modes
-----------------------------------------------------------


