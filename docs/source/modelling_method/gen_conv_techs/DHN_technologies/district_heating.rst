District Heating
=======================================

The district heating technology represents the district
heating network (DHN).

The district heating network can be supplied with 
heat in two different ways: Firstly, it can import heat
from an unknown source. This is what is represented
when running the model for an arbitrary Swiss municipality
with a district heating network *without optimization*. 
The imported district heat has a constant CO2 intensity and
cost that do not depend on time.
Alternatively, heat generators, which are connected in the 
``heat_sources`` section, can be connected to the DHN. These
``heat_sources`` are only used when running the ``model`` *with
optimization*.

Then running *without optimization*, the amount of heat demand 
attached to the DHN is determined from the heat generator 
entries in the RBD (Federal Registry of buildings and dwellings).
When *optimizing*, also other buildings can be attached to the
DHN. For this, there are two different capex calculation mode.
Firstly, the if ``closeness_based_dh_expansio_cost`` is 
``False``, the cost is a constant capex cost per kW of power needed.
Secondly, if ``closeness_based_dh_expansio_cost = True``, the buildings
are grouped into four groups: firstly those already connected to the
DHN, and then three different categories grouped by their heat demand
relative to their average distance to neighbouring buildings. Thereby,
both an approximative distance to neighbouring buildings, giving 
a measure for the cost of grid expansion, and a heat demand
per group is determiend. The cost of expansion
and of maintaining the DHN is then calculated
based on the parameters ``investment_dh_grid_per_m`` and
``maintenance_cost_dh_grid_per_m``.

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/district_heating.rst

