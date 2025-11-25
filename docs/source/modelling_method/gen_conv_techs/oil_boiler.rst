Oil Boiler
=======================================

Hulla hopp ist ein guter Sport.

.. include:: ../../how_to_use_the_model/input_csv_as_rst/oil_boiler.rst


+------------------------------+--------------+-----------+------------------------------------------+
| Attribute                    | Unit         | Data type | Description                              |
+==============================+==============+===========+==========================================+
| deployment                   | —            | bool      | If set to 'true', the technology will be |
|                              |              |           | considered in the energy system model    |
|                              |              |           | (this does not necessarily mean it will  |
|                              |              |           | be used). Only relevant for              |
|                              |              |           | optimisation.                            |
+------------------------------+--------------+-----------+------------------------------------------+
| kW_th_max                    | kW           | float     | Maximum thermal capacity (i.e. heat      |
|                              |              |           | output).                                 |
+------------------------------+--------------+-----------+------------------------------------------+
| hv_oil_MJpkg                 | MJ/kg        | float     | Lower heating value of oil.              |
+------------------------------+--------------+-----------+------------------------------------------+
| eta                          | —            | float     | Conversion efficiency from fuel to heat. |
+------------------------------+--------------+-----------+------------------------------------------+
| oil_price_CHFpl              | CHF/l        | float     | Oil price (annual fixed value).          |
+------------------------------+--------------+-----------+------------------------------------------+
| co2_intensity                | kg CO2/kWh   | float     | Carbon-dioxide intensity of technology   |
|                              |              |           | output (annual average value).           |
+------------------------------+--------------+-----------+------------------------------------------+
| lifetime                     | years        | int       | Expected lifetime of technology before   |
|                              |              |           | replacement is required.                 |
+------------------------------+--------------+-----------+------------------------------------------+
| interest_rate                | —            | float     | Interest rate for computing levelised    |
|                              |              |           | costs (if required).                     |
+------------------------------+--------------+-----------+------------------------------------------+
| replacement_factor           | —            | float     | Used for scenario                        |
|                              |              |           | 'fossil_heater_retrofit'. Fraction of    |
|                              |              |           | heating capacity to be replaced by heat  |
|                              |              |           | pumps.                                   |
+------------------------------+--------------+-----------+------------------------------------------+
| capex                        | CHF/kWp      | float     | CAPEX cost of technology per unit of     |
|                              |              |           | capacity.                                |
+------------------------------+--------------+-----------+------------------------------------------+
| capex_one_to_one_replacement | CHF/kWp      | float     | CAPEX cost of technology per unit of     |
|                              |              |           | capacity (when device has reached the    |
|                              |              |           | end of life)                             |
+------------------------------+--------------+-----------+------------------------------------------+
| maintenance_cost             | CHF/kWp/year | float     | OPEX cost of technology.                 |
+------------------------------+--------------+-----------+------------------------------------------+
| fixed_demand_share           | —            | bool      |                                          |
+------------------------------+--------------+-----------+------------------------------------------+
| fixed_demand_share_val       | —            | float     |                                          |
+------------------------------+--------------+-----------+------------------------------------------+
| only_allow_existing          | bool         | bool      |                                          |
+------------------------------+--------------+-----------+------------------------------------------+


The oil boiler represent a device that burns 
heating oil to produce heat for space heating
and domestic hot water. It is situated in individual 
buildings and therefore contributes a constant share
to the overal heat production. It has a constant
efficiency and constant carbon emissions per kWh
of energy converted.

.. csv-table::
	      :file: ../../how_to_use_the_model/input_csv/oil_boiler.csv
	      :widths: auto
	      :header-rows: 0


Balrog ist ein liebes Tier.
Er frisst nur böse Kinder.
Und dann kaut er sie ganz gut.
Wie ein guter Junge.
Denn gute Kinder kauen ihr Essen gründlich.
Sonst verschlucken sie sich ja noch.