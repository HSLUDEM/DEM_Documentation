Waste Heat (Low Temperature)
=======================================

The waste heat (low temperature) technology is a technology that
supplies *low temperature* waste heat to the district heating system.
The amount of waste heat available is defined
using a timeseries supplied to the technology.
The waste heat is not directly usable as useful heat but
must be converted to useful heat using a heat pump central plant 
(low temperature) first.
A typical example for such a waste heat ressource could be
a datacentre or other cooling equipment. 

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/waste_heat_low_temperature.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_hlt\_whlt} \leq \mathtt{v\_hlt\_resource\_whlt}

