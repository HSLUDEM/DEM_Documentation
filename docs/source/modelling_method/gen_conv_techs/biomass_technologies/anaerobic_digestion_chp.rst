Anaerobic Digestion CHP
=======================================

The anaerboic digestion CHP technology represents
a two-stage biomass technology. In the first stage,
wet biomass is digested to obtain biogas. This biogas
is then burnt in a cogeneration device to co-generate
heat and electricity.

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/anaerobic_digestion_chp.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_e\_aguc} = \mathtt{efficiency\_electricity} \cdot \mathtt{u\_wet\_bm\_aguc} 

.. math:: \mathtt{v\_h\_aguc} = \mathtt{efficiency\_heat} \cdot \mathtt{u\_wet\_bm\_aguc} 
