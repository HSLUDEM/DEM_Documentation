
.. _tech_solar_pv:

Solar PV
=======================================

The solar PV technology represents solar PV installations on rooftops and soon fassades. It is adjusted to the available roof potential in a given municipality.

For Switzerland, building-level estimates of annual rooftop photovoltaic potential are derived from a geospatial assessment published by the Swiss Federal Office of Energy (2023). Temporal PV production is represented by hourly generation profiles, which were simulated with the PV*SOL software (Valentin Software GmbH, 2025) for a set of representative locations across Switzerland and provided to DEM as time-series inputs.

.. include:: ../../how_to_use_the_model/input_csv_as_rst/solar_pv.rst

The symbols and names of the flows are

.. include:: ../../how_to_use_the_model/flows_tables/pv.rst


References
^^^^^^^^^^^

Swiss Federal Office of Energy. (2023, January). *Dokumentation Geodatenmodell – Solarenergie: Eignung Dächer (Sonnendach.ch); Solarenergie: Eignung Fassaden (Sonnenfassade.ch)* (Technical report). Bern, Switzerland. Retrieved December 17, 2025, from |sonnendach_link|

.. |sonnendach_link| raw:: html

   <a href="https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/geoinformation/geodata/solar-energy/suitability-of-roofs-for-use-of-solar-energy.html" target="_blank">https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/geoinformation/geodata/solar-energy/suitability-of-roofs-for-use-of-solar-energy.html</a>
   
Valentin Software GmbH. (2025). *PVSOL* [Software]. Berlin, Germany. Retrieved December 17, 2025, from |pvsol_link|

.. |pvsol_link| raw:: html

   <a href="https://valentin-software.com/en/products/pvsol/" target="_blank">https://valentin-software.com/en/products/pvsol/</a>