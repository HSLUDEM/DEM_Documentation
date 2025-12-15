.. _demand-side-scenario:

Demand Side
=======================================

The demand side scenario is a multifaceted scenario that 
implements demand-side changes due to retrofitting, building 
renovation and the further deployment of electric vehicles.
Since this scenario involves a lot of parameters,
these are separately discussed in different subsection.

Electric vehicles and their flexibility
---------------------------------------

For electric vehicle (EV) charging demand modelling, see :ref:`electric-vehicles`. Flexibility from EV charging is implemented as defined by Herrera and Hug (2025) and includes lower and upper charging power limits, as well as the daily available flexible energy.
Flexibility from EV charing is only active in the optimisation scenario.

.. _climate-adjustment:

Climate Adjustment
---------------------------------------

The climate adjustement adjusts the heat demand to a future, warmer climate. 
The ``year`` parameter determines which year is simulated.
This parameter does not only influence the climate. It also influences 
how many houses have already been renovated and how many heat generators
have been replaced (see subsection on Renovation and heat generator replacement below).
In addition, the efficiency of heat pumps is influenced by the year (see description of 
heat pump tech).

The relevant parameters for the climate adjustment are

+--------------+----------------+------------------------------------------------------+
| Name         | Standard value | Description                                          |
+==============+================+======================================================+
| ``year``     | 2023           | Year to simulate (influences temperature, renovation |
|              |                |                                                      |
|              |                | and heat generator replacement, heat pump COPs)      |
|              |                |                                                      |
|              |                | Options: 2023, 2030, 2040, 2050                      |
+--------------+----------------+------------------------------------------------------+
| rcp_scenario | 'RCP26'        | Climate change scenario (RCP26, RCP45 or RCP85)      |
+--------------+----------------+------------------------------------------------------+
| ts_type      | 'tas_median'   | temperature type                                     |
+--------------+----------------+------------------------------------------------------+


The climate data is based on the CH2018 scenarios (CH2018 Project Team, 2018).

Renovation and heat generator replacement
---------------------------------------

As time passes, more and more buildings are either totally renovated. In addition, heat generators such 
as oil boilers and heat pumps have a finite lifetime.
At the end of their lifetime, they need to be replaced. 
Both of these effects trigger an improvement in the ecological performance
of the building stock over time.

Total renovation and heat generator replacement are treated
separately in the DEM. 
In the case of a total renovation, the construction period of the affected
building is upgraded to the most modern construction period.
As a consequence of this, the heat demand drops significantly.
In addition, the heat generator is reassigned.
If optimization is active, the heat generator is changed to
'other'. This means that the optimizer then needs to choose
a new heat generator and pay its full price.
If manual scenarios are calculated, the heat generator is reassigned
according to the dictionary defined in the input file.
There are two different ways to define which buildings undergo total renovation.
If ``use_constant_total_renovation_rate`` is False, the buildings 
that are marked as up for renovation up to that year according 
to the corresponding entry in the master file are renovated.
The rates for this are based on the publication by Streicher et al.
There are three different scenarios to choose from: 'renovation_low',
'renovation_high' and 'renovation_base'. Given that already 'renovation_low'
implements are rather high renovation rate, this is the recommended scenario.
If ``use_constant_total_renovation_rate`` is True, a constant
share of each building is renovated each year (i.e. the buildings 
are partially totally renovated, with a given probability that then
defines the overall heat demand). Even then, no total renovations take place during
the first 35 years of a building's existence.

The parameters for the total renovation are described in the table:

+-----------------------------------------------+-----------------------------------------------------+------------------------------------------+
| Name                                          | Standard value                                      | Description                              |
+===============================================+=====================================================+==========================================+
| total_renovation_activated                    | True                                                | Is the total renovation activated?       |
+-----------------------------------------------+-----------------------------------------------------+------------------------------------------+
| use_constant_total_renovation_rate            | False                                               | Use constant renovation rate or          |
|                                               |                                                     |                                          |
|                                               |                                                     | pre-defined scenario                     |
+-----------------------------------------------+-----------------------------------------------------+------------------------------------------+
| renovation_scenario                           | 'renovation_low'                                    | If scenario is used, which one           |
+-----------------------------------------------+-----------------------------------------------------+------------------------------------------+
| constant_total_renovation_rate                | 0.01                                                | If a constant rate is used, value of it  |
+-----------------------------------------------+-----------------------------------------------------+------------------------------------------+
| total_renovation_heat_generator_reassignment  | {'v_h_eh' : 0.0,'v_h_hp' : 0.8, 'v_h_dh' : 0.05,    | Reassignment of heat generators for      |
|                                               |                                                     |                                          |
| _rates_space_heating_for_manual_scenarios     | 'v_h_gb' : 0.05,'v_h_ob' : 0.05, 'v_h_wb' : 0.05,   | space heating for manual scenarios       |
|                                               |                                                     |                                          |
|                                               | 'v_h_solar' : 0.0,'v_h_other' : 0.0 }               |                                          |
+-----------------------------------------------+-----------------------------------------------------+------------------------------------------+
| total_renovation_heat_generator_reassignment  | {'v_hw_eh' : 0.1,'v_hw_hp' : 0.7, 'v_hw_dh' : 0.05, | Reassignment of heat generators for      |
|                                               |                                                     |                                          |
| _rates_dhw_for_manual_scenarios               | 'v_hw_gb' : 0.05,'v_hw_ob' : 0.05,'v_hw_wb' : 0.05, | domestic hot water for manual scenarios  |
|                                               |                                                     |                                          |
|                                               | 'v_hw_solar' : 0.0,'v_hw_other' : 0.0 }             |                                          |
+-----------------------------------------------+-----------------------------------------------------+------------------------------------------+



Heat generator replacement is controlled separately by the parameters

+-------------------------------+---------------+-----------------------------------------------------------------------------+
| Name                          | Standard value| Description                                                                 |
+===============================+===============+=============================================================================+
| heat_generator_renovation     | True          | Is heat generator replacement activated?                                    |
+-------------------------------+---------------+-----------------------------------------------------------------------------+
| act_on_fossil_heater_retrofit | False         | For manual scenarios:                                                       |
|                               |               |                                                                             |
|                               |               | Does the heat generator replacement replace a fossil heater retrofit?       | 
|                               |               |                                                                             |
|                               |               | If yes, the rate of fossil heater retrofit is increased according to the    |
|                               |               |                                                                             |
|                               |               | heat generator replacement rate                                             |  
+-------------------------------+---------------+-----------------------------------------------------------------------------+

The heat generator renovation is happening according to two different criteria:
For buildings that were recently built, i.e. the data collection year is smaller equal 
to the construction year of the buiding plus the lifetime of the heat generator,
heat generator replacement takes place when the end of the lifetime of the heat generator is
reached (e.g. after 25 years). For old buildings, a constant rate of 1.0/lifetime of the heat
generator is applied. This constant rate applies for every year that passes between the year of 
data collection and the simulation year.
When heat generators reach the end of their life, they are marked as having reached the end of their life.
If optimization takes place, keeping this type of heat generator incurs a cost. Furthermore, the COP of 
heat pumps can be positively affected by replacement. If no optimization takes place (for manual scenarios),
nothing happens unless ``act_on_fossil_heater_retrofit`` is active. If that parameter is active,
it is ensured that the fossil_heater_retrofit rates are at least as high as the rate of such
heat generators that have reached the end of their life. Furthermore, if fossil_heater_retrofit
is not activated, it is turned on and its rates correspond to the end-of-life rates of the heat
generators.

Testtext hier.


References
^^^^^^^^^^^

CH2018 Project Team (2018): *CH2018 – Climate Scenarios for Switzerland*. National Centre for Climate Services. doi: https://doi.org/10.18751/Climate/Scenarios/CH2018/1.0

Parajeles Herrera, M., & Hug, G. (2025). *Modeling Charging Demand and Quantifying Flexibility Bounds for Large-Scale BEV Fleets*. arXiv e-prints, arXiv-2504.