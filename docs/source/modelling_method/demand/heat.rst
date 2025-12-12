Heat Demand
========================

Space Heating
--------------------

Annual space-heating demand is calculated using the heat loss coefficient method according to Schneeberger et al. (2025). A regional correction factor is applied only in regions where measured data are available. The method relies on individual building properties from the Federal Register of Buildings and Dwellings (RBD) (Federal Statistical Office, 2025), the geometry of a reference building and thermal transmittance (U-value) assumptions by building archetype (Pongelli, 2023) and weather data from the Meteostat Python library. The resulting annual demand per building is then temporally distributed using normalized heating-degree-hour (HDH) profiles (Schneeberger et al., 2025). Aggregating the hourly building-level series yields district- or municipality-level demand.


Industry and Services
--------------------
The space heating demand for industry and services is computed with the standard factor method (Schneeberger et al., 2025), which is based on the framework of the Sonnendach.ch project (Swiss Federal Office of Energy, 2023). The calculation uses space heating energy performance indicator by building archetype, building attributes from the RBD (Federal Statistical Office, 2025), and mean annual ambient temperature from the Meteostat Python library. As with residential buildings, a regional correction factor is applied only where measured data are available. Annual demand is downscaled to hourly values using normalized HDH profiles (Schneeberger et al., 2025), and the hourly building demands are aggregated to district- or municipality-level totals.


Domestic Hot Water (DHW)
------------------------
At the municipality level, the population is distributed across the residential floor area to estimate the number of residents per building. Hot-water demand is then calculated by multiplying a standard value of 850 kWh per person per year by the number of residents per building. The 850 kWh corresponds to an average hot-water use of 40 L per person per day (Arpagaus et al., 2016; Schweizerischer Ingenieur- und Architektenverein, 2025) and an outlet temperature of 60°C.

Flows
----

The symbols and names of the flows are

.. include:: ../../how_to_use_the_model/flows_tables/d_h.rst

References
^^^^^^^^^^^

.. alphabetized by first author surname

Arpagaus, C., Vetsch, B., & Bertsch, S. (2016, November 14). *Domestic hot water heat pumps: Task 1 market overview, country report Switzerland (HPT Annex 46).* Interstaatliche Hochschule für Technik Buchs, Institut für Energiesysteme (IES), for the Swiss Federal Office of Energy (SFOE). |Arpagaus2016_link|

.. |Arpagaus2016_link| raw:: html

   <a href="https://www.fws.ch/wp-content/uploads/2018/10/Market_Overview_Country_Report_Switzerland_Annex_46_DHWHP_Task1.pdf" target="_blank">https://www.fws.ch/wp-content/uploads/2018/10/Market_Overview_Country_Report_Switzerland_Annex_46_DHWHP_Task1.pdf</a>

Federal Statistical Office (FSO). (2025). *Federal register of buildings and dwellings (RBD)*. |FSO2025_link|

.. |FSO2025_link| raw:: html

   <a href="https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html" target="_blank">https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html</a>

Pongelli, A., Priore, Y. D., Bacher, J. P., & Jusselme, T. (2023). *Definition of building archetypes based on the Swiss energy performance certificates database*. Buildings, 13 (1), 40. |Pongelli2023_link|

.. |Pongelli2023_link| raw:: html

   <a href="https://doi.org/10.3390/buildings13010040" target="_blank">https://doi.org/10.3390/buildings13010040</a>

Schneeberger, S., Meister, C., & Schuetz, P. (2025). Estimating the heating energy demand of residential buildings in Switzerland using only public data. Energy and Buildings, 116371. |Schneeberger2025_DOI_link|

.. |Schneeberger2025_DOI_link| raw:: html

   <a href="https://doi.org/10.1016/j.enbuild.2025.116371" target="_blank">https://doi.org/10.1016/j.enbuild.2025.116371</a>

Schneeberger, S., Lucas, E., Meister, C., & Schuetz, P. (2024, February). Wärmebedarfsschätzung für Wohngebäude. In Proceedings of the 18th Symposium Energieinnovation. TU Graz, Austria. |Schneeberger2024_link|

.. |Schneeberger2024_link| raw:: html

   <a href="https://www.tugraz.at/fileadmin/user_upload/tugrazExternal/f560810f-089d-42d8-ae6d-8e82a8454ca9/files/lf/Session_F3/631_LF_Schneeberger.pdf" target="_blank">https://www.tugraz.at/fileadmin/user_upload/tugrazExternal/f560810f-089d-42d8-ae6d-8e82a8454ca9/files/lf/Session_F3/631_LF_Schneeberger.pdf</a>

Schweizerischer Ingenieur- und Architektenverein (SIA). (2025). *SIA 385/2:2025, Anlagen für Trinkwarmwasser in Gebäuden – Warmwasserbedarf, Gesamtanforderungen und Auslegung.* Zürich: Schweizerischer Ingenieur- und Architektenverein.

Swiss Federal Office of Energy (SFOE). (2023, January). *Dokumentation Geodatenmodell – Solarenergie: Eignung Dächer (Sonnendach.ch); Solarenergie: Eignung Fassaden (Sonnenfassade.ch).* Bern: Swiss Federal Office of Energy. |SFOE2023_link|

.. |SFOE2023_link| raw:: html

   <a href="https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/geoinformation/geodata/solarenergy/suitability-of-roofs-for-use-of-solar-energy.html" target="_blank">https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/geoinformation/geodata/solarenergy/suitability-of-roofs-for-use-of-solar-energy.html</a>

