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
| cop_timeseries_file_path      | ""              |Path to COP timeseries file for mode "form_file"                             |
|                               |                 |and "from_file_adjusted_to_spf"                                              | 
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
There are several ways to set the COP of the heat pumps.

In the mode "constant", a constant, user-defined COP is used.

In the mode "from_file", a timeseries provided by the user as
file is used.

In the mode "from_file_adjusted_to_spf", a timeseries provided by
the user is used but using the demand profile, it is scaled
such that the SPF reaches a user-defined value.

In the mode "location_based", a COP model taking into account
many properties of the building stock and location is used. This
model is described further below.

"location_based" COP mode
++++++++++++++++++++++++++++++++++++++++++++

The "location_based" COP mode is the standard COP mode.
It calculates a COP timeseries based on the properties of the
individual buildings, the quality_factors specified in the 
input file, the local weather and internal parameters defined
in the corresponding code file.

For each building, the algorithm assign probabilities for 
several properties for space heating

1. Is the heat dissipator radiator- or underfloor-heating-based
2. Is the heat pump air-source or ground-source.
3. Does the heat pump already exist or is it a new device to be installed by the optimizer.
4. Which heating curve construction period is used.

and for domestic hot water-heating

1. Is the heat pump air-source or ground-source.
2. Does the heat pump already exist or is it a new device to be installed by the optimizer.

For each building, we assign a construction year. This year is the GBAUJ from the RBD if
it is defined. Otherwise, the construction period (GBAUP) is used and the central year
of the construction period is assigned as construction year.

The share of radiators is assumed to be 100\% until 1970. From then on, it rises by 1.66\% per year
until reaching 100\% in 2030. The year here is the construction year of the building.

The share of ASHPs is assumed to be 66\% for existing installations (34\% GSHP), 
while for new installations, 72\% ASHPs and 28\% GSHPs is assumed. These percentages
are based on the statistics for sold heat pumps by the FWS (FWS, 2025).
For existing installations, this is only used if the heat source is not specified
in the RBD.

Whether the heat pump already exists is based on the RBD-information (FSO, 2025).

For the definition of the heating curve construction period, we rely on the 
information sheet "Heizkurve richtig einstellen" by the Swiss Federal Office of Energy 
(SwissEnergy, 2022).

For air-source heat pumps, the outdoor temperature is used as source temperature.
For ground-source heat pumps, a simple harmonic function is used as source temperature, 
with a mean value of 5°C and an amplitude of 3°C, where the lowest point is reached at
the end of February.

For the domestic hot water, a constant temperature of 55°C is assumed.

The COP is then calculated based on the Carnot efficiency of a perfect 
heat pump, capping the efficiency at 20. This value is then corrected
by the quality_factor provided by the user.

.. math::
   COP_{Carnot} = \\frac{T_{cond}}{T_{cond} - T_{evap}}

where temperatures are in kelvin and refer to the condenser (output) and
evaporator (source) sides of the heat pump.

This efficiency is then different for newly installed HPs than for the 
existing ones. Usually the existing HPs profit from being in more modern
buildings, which yields lower heating water temperatures and thereby
higher efficiencies, but their efficiency is reduced by the age of the 
existing heat pumps, which have lower device-level efficiencies, and by 
the fact that new buildings have a higher share of DHW, which is hotter than
heating water.

References
^^^^^^^^^^^

.. alphabetized by first author surname

SwissEnergy (2022, August 29). *Set the heating curve correctly* Federal Office of Energy. https://pubdb.bfe.admin.ch/en/publication/download/9982

FWS (2025). *Jahres-Statistiken & Marktzahlen* FWS Fachvereinigung Wärmepumpen Schweiz. https://www.fws.ch/statistiken/

Federal Statistical Office (FSO). (2025). *Federal register of buildings and dwellings (RBD)*. https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html
