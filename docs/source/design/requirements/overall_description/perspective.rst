Product Perspective
===================

Synapse is best described as an "open science gateway".

Similar products include

* `Cyverse <cyverse_>`_ - a bioinfomatics platform
* `Sci-GalA Open Science Platform <scigala_>`_ - Sci-GalA is a
  consortium similar to XSEDE which is broadly focused on advancing
  scientific computing and data management in Africa.
*

.. _cyverse: http://www.cyverse.org/
.. _scigala: http://www.sci-gaia.eu/osp/

TODO - Put the product into perspective with other related products.  It
is not standalone but rather integrates many 3rd party components mediating
their interactions.  Compare to existing systems in the marketplace.

System Interfaces
-----------------

TODO - Discuss APIs of existing components and how Synapse will interface with them.

User Interfaces
---------------

TODO - Discuss the interface between Synapse and its users.  GUI, CLI, etc?
ADA compliance, mobile responsiveness

Hardware Interfaces
-------------------

TODO - Discuss interface between Synapse and hardware components of the system.
This includes configuration details, what devices are supported, how they are
supported, and protocols.  (This will probably be fairly short.)

Software Interfaces
-------------------

TODO - Specify other software products that Synapse will interface with. What
are they?  Why does Synapse interface with them?  What is the type of messages
passed and their format?  (Don't specify software that Synapse will use.  Only
list the systems that Synapse must interact with.  For ex. choosing a specific
database software without a requirement is a design choice, not a
requirement.)

Communications Interfaces
-------------------------

TODO - This will be fairly short.  Specify network protocols.  Perhaps OAuth2
would be worth listing.

Memory Constraints
------------------

TODO - Maybe not quite applicable, but perhaps the size of the Webpack bundle
could get ridiculous.  Perhaps this should be some other perf. constraint
like load times.

Operations
----------

TODO - Elements of user-required operations.  When use is active vs unattended.
Backup and recovery.  Business process constraints.  (i.e. load is heavier in
the morning when everyone checks their email.  Or... Agave has regular
scheduled maintenance during the day which breaks everything.)

Site Adaptation Requirements
----------------------------

TODO - Requirements for initialization sequences.  (Adding Beocat to Agave
profile for example.)  Any configuration that the use would need to do,
external to Synapse, in order for Synapse and the overall system to
operate correctly.