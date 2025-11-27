Wood Gasification CHP
=======================================

The wood gasification CHP first uses a wood gasifier to convert
woody biomass into biogas. This biogas is then used to co-generate
electricity and heat.

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/wood_digestion_chp.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_e\_wguc} = \mathtt{efficiency_electricity} \cdot \mathtt{u\_wd\_wguc}

.. math:: \mathtt{v\_h\_wguc} = \mathtt{efficiency_heat} \cdot \mathtt{u\_wd\_wguc} 

