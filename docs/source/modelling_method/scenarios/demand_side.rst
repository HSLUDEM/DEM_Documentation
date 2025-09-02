Demand Side
=======================================

The demand side scenario is a multifaceted scenario that 
implements demand-side changes due to retrofitting, building 
renovation and the further deployment of electric vehicles.
Since this scenario involves a lot of parameters,
these are separately discussed in different subsection.

Electric vehicles and their flexibility
---------------------------------------
tbd

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

+--------------+----------------+------------------------------------------------------------------------------------------------------+
| Name         | Standard value | Description                                                                                          |
+==============+================+======================================================================================================+
| ``year``     | 2023           | Year to simulate (influences temperature, renovation and heat generator replacement, heat pump COPs) |
|              |                | Options: 2023, 2030, 2040, 2050                                                                      |
+--------------+----------------+------------------------------------------------------------------------------------------------------+
| rcp_scenario | 'RCP26'        | Climate change scenario (RCP26, RCP45 or RCP85)                                                      |
+--------------+----------------+------------------------------------------------------------------------------------------------------+
| ts_type      | 'tas_median'   | temperature type                                                                                     |
+--------------+----------------+------------------------------------------------------------------------------------------------------+


The climate data is based on the CH2018 scenarios.

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
defines the overall heat demand).
The parameters for the total renovation are described in the table:




