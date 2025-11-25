Oil Boiler
=======================================


+==============================+==============+===========+===========+
| Attribute                    | Unit         | Data type | Descrip   |
+==============================+==============+===========+===========+
| deployment                   |              | bool      | If set    |
+------------------------------+--------------+-----------+-----------+
| kWp_max                      | kW           | float     | Kilowat   |
+------------------------------+--------------+-----------+-----------+
| eta_overall                  |              | float     | Overall   |
+------------------------------+--------------+-----------+-----------+
| co2_intensity                | kg CO2/kWh   | float     | Carbon-   |
+------------------------------+--------------+-----------+-----------+
| lifetime                     | years        | int       | Expecte   |
+------------------------------+--------------+-----------+-----------+
| capex                        | CHF/kWp      | float     | CAPEX c   |
+------------------------------+--------------+-----------+-----------+
| maintenance_cost             | CHF/kWp/year | float     | OPEX co   |
+------------------------------+--------------+-----------+-----------+
| interest_rate                |              | float     | Interes   |
+------------------------------+--------------+-----------+-----------+
| potential_integration_factor |              | float     | Used foV. |
+------------------------------+--------------+-----------+-----------+
| virtual_export_tariff        | CHF/kWh      | float     | virtual   |
+------------------------------+--------------+-----------+-----------+
| export_subsidy               | CHF/kWh      | float     | subsidy   |
+------------------------------+--------------+-----------+-----------+
| only_use_installed           |              | bool      |           |
+------------------------------+--------------+-----------+-----------+

+=====+====+
| A   | B  |
+=====+====+
| C   | D  |
| F   | K  |
+-----+----+
| Z   | A  |
+=====+====+


Oily boiler be so kind, bring me warmth.

.. include:: ../../how_to_use_the_model/input_csv_as_rst/oil_boiler.rst


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