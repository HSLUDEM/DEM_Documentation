District Heating
=======================================

The district heating technology represents the district
heating network.

The district heating network can be supplied with 
heat in two different ways: Firstly, it can import heat
from an unknown source. This is what is represented
when running the model for an arbitrary Swiss municipality
with a district heating network *without optimization*. 
The imported district heat has a constant CO2 intensity and
cost that do not depend on time.
Alternatively, heat generators, which are connected in the 
*heat_sources* section, can be connected to the DHN. These
*heat_sources* are only used when running the model *with
optimization*.

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/district_heating.rst

