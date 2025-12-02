---
title: 'District Energy Model (DEM): An open-source model for local energy system optimisation.'
tags:
  - Python
  - Optimisation
  - multi-energy system
  - scenario analysis
  - renewable integration
authors:
  - name: Ueli Schilt
    orcid: 0000-0002-6104-1389
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
  - name: Pascal M. Vecsei
    orcid: 0000-0003-1058-8808
    affiliation: 1
  - name: Somesh Vijayananda
    orcid: 0009-0009-4558-7064
    affiliation: 1
  - name: Philipp Schuetz
    orcid: 0000-0001-7564-1468
    affiliation: 1
	
affiliations:
 - name: Competence Centre for Thermal Energy Storage, School of Engineering and Architecture, Lucerne University of Applied Sciences, Horw, Switzerland
   index: 1
 - name: School of Architecture, Civil and Environmental Engineering, École Polytechnique Fédérale de Lausanne (EPFL), Lausanne, Switzerland
   index: 2
   
date: 24 November 2025
bibliography: paper.bib

---

# Summary

The transition from centralised to decentralised energy systems for achieving net-zero emission targets requires the evaluation of potential future scenarios on various spatial scales [ref]. The *District Energy Model (DEM)* is a Python-based multi-energy system model designed to simulate energy flows from neighbourhood to regional scale with a focus on the integration of decentralized renewable energy technologies (e.g., solar, wind, biomass). DEM runs simulation and optimisation studies in hourly resolution using a "snapshot-year" approach [ref Marchal]. For selected regions (e.g., Switzerland), compiled input data from public sources is provided to run studies without the need of collecting and compiling such data. 

# Statement of need

Similar open-source modelling frameworks exist, such as e.g., SESMG [ref], EHTOS.FINE [ref], REHO [ref], (..find more). However, while all of these models provide valuable frameworks for evaluating multi-energy systems on various spatial and temporal scales, they all require the user to provide input data such as demand profiles, cost information, or technology specifications. DEM already provides this type of data for selected regions. It has been collected from various public sources and processed for use in simulation studies. Therefore, simulation and optimisation studies can be run in DEM with only minimal configuration requirements (e.g., which buildings to consider), while still maintaining maximum flexibility of substituting any of the pre-configured data with custom data and model configurations.
While an optimisation study is very useful to determine optimal technology design and operation, many energy provision scenarios can be simulated without applying optimisation. Therefore, DEM can also be run as a simulation without optimisation for various scenarios. This allows for short computation times and fast result generation.

-	What stands out from a research perspective? Flexibility considerations; local boundaries, while also considering national electricity provision (as an interface model between local, regional, and national energy planning)
-	Availability of open-source data: pulling it together in one model
-	Bottom-up demand consideration of individual buildings
-	Focus on integration of local, decentralized energy sources and technologies
-	Energy-planning on neighbourhood-scale
-	No extensive modelling required, yet flexible in scenario creation.
-	Pre-configured with standard values for the Swiss energy system
-	Automated parametrisation: Provided for Switzerland; Other countries to be added  can also be added by users, as the required data structure is provided
-	Selection of custom district
-	Optimisation optional


# Acknowledgements

The research published in this publication was carried out with the support of the Swiss Federal Office of Energy as part of the SWEET consortium EDGE. The authors bear sole responsibility for the conclusions and the results presented in this publication.

# References