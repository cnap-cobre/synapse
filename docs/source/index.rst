.. Synapse documentation master file, created by
   sphinx-quickstart on Wed Apr 18 22:21:04 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: https://raw.githubusercontent.com/cnap-cobre/synapse/master/logo.png
   :width: 300 px
   :align: center

#######
Synapse
#######

An open science gateway for the Psychological Sciences

* Integrated with Agave_, Globus_, Dropbox_, `Google Drive`_
* Built with open source technologies
* Use your own cluster (Slrum, SGE, Torque, Condor, ...anything supported by Agave_)
* Use your own filesystem (SFTP, IRODS, GridFTP, AmazonS3, Dropbox)
* Share data with collaborators
* Publish datasets for reproducible research

.. _Agave: https://agaveapi.co/
.. _Globus: https://www.globus.org/
.. _Dropbox: https://www.dropbox.com/
.. _`Google Drive`: https://www.google.com/drive/

Goals
=====

Synapse aims to provide a user-friendly web interface for research computing resources.
Core goals include:

* Share data among collaborators
* Launch and monitor cluster computing jobs
* Trace data provenance with metadata
* Search data by content and metadata
* Automate backups of critical research data
* Publish prepared datasets with a DOI_
* Produce data visualizations

.. _DOI: https://www.doi.org/


Synapse is developed for the `Cognitive and Neurobiological Approaches to Plasticity
Center of Biomedical Research <http://www.k-state.edu/cnap/>`_ at
`Kansas State University <http://www.k-state.edu>`_.

Contributors
============

* Kevin Dice
* Gabe Maddex

Submitting a PR?  Add yourself to this list.

License
=======

Synapse is licensed under the `MIT License <https://tldrlegal.com/license/mit-license>`_.

Essentially, you are free to do anything with this software except hold its creators liable.
You must include the copyright notice and MIT License in all copies or substantial uses of
this software.

See the full license text `here <https://github.com/cnap-cobre/synapse/blob/master/LICENSE.md>`_.

Contents
========
.. toctree::
   :maxdepth: 2

   design/index
   user/index
   developer/index
   deployment/index

Funding
=======

Synapse and The CNAP Center of Biomedical Research Excellence (COBRE) is funded
through a $10.6M grant from the National Institute of General Medical Sciences
(P20 GM113109) in 2017.

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
