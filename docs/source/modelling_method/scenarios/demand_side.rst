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

tbd


