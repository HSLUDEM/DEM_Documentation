.. _tutorial_2:

Tutorial 2: Customised District
===================

.. note::
  *UNDER CONSTRUCTION*
  
This tutorial builds a district energy simulation for a small district. While in :ref:`Tutorial 1 <tutorial_1>` the model considered the whole municipality of |Allschwil_Wikipedia_link|, this example looks at a few selected buildings of the same municipality (see figure below).

.. image:: images/district.png
   :width: 80%
  
.. code-block:: yaml

    custom_district:
        implemented: true
        EGID_List: [2348043, 245063143, 2348044, 2348045, 391986, 391987, 391988, 391989, 391993, 391990, 391994, 245025839, 245025840, 391992, 245025841, 245025842, 391995, 391996, 391997, 2348046, 3029563, 391998, 245046103, 391999, 245025843, 245045313, 245046052, 392000, 245027525, 3029067]
        custom_district_name: 'tutorial_2_district'
		

.. code-block:: yaml

    oil_boiler:
        replacement_factor: 0.8
        
    gas_boiler:
        replacement_factor: 0.8
    
    solar_pv:
        potential_integration_factor: 0.8
        
    tes_decentralised:
        deployment: true
        capacity_kWh: 30000
		
		
		
.. Links:

.. |Allschwil_Wikipedia_link| raw:: html

   <a href="https://en.wikipedia.org/wiki/Allschwil" target="_blank">Allschwil</a>
   
   
.. |Swiss_data_Zenodo_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.17603138" target="_blank">Zenodo</a>
   
   
.. |bfs_number_link| raw:: html

   <a href="https://www.bfs.admin.ch/bfs/de/home/grundlagen/agvch.html" target="_blank">BFS municipality identifier</a>