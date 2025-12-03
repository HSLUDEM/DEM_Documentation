Heat Pump Central Plant
=======================================

The heat pump central plant represents a large scale heat pump
connected to the district heating network. It supplies directly
useful heat.
Its COP is calculated based on a constant demand-side temperature
and an inflow temperature as well as a quality factor. 
The inflow temperature can be the air temperature or a fixed temperature
defined by the user.

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/heat_pump_cp.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_h\_hpcp} = \mathtt{COP} \cdot \mathtt{u\_e\_hpcp} 

The symbols and names of the flows are

.. include:: ../../../how_to_use_the_model/flows_tables/hpcp.rst
