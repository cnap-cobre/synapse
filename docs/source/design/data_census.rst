###########
Data Census
###########

The following is a summary of our early requirements gathering work.

While Synapse is first and foremost an open science gateway for the
`CNAP Center <cnap_>`_ at Kansas State University, we hope others may find use
in this software.

Intended Audience:

* Source code contributors
* HPC, IT, and Library directors evaluating data management options for their
  own institution

.. _cnap: http://www.k-state.edu/cnap/

We put out a survey to the Principal Investigators of the `CNAP Center <cnap_>`_
to learn what needs they have with respect to data management and research
computing.

.. toctree::
   :maxdepth: 1
   :caption: Contents

What we asked
=============

* Provenance

  * Where does your data come from?
  * How do you collect it?

* Size

  * What is the current size of your datasets?
  * What is your projected data growth rate?

* Formats

  * In what formats are your data represented?

* Sharing

  * With whom do you need to share your data?
  * How do you currently share your data?
  * Are there any restrictions on sharing such as HIPPA or PII?

* Backup

  * What is your current backup strategy?

* Metadata

  * How do you currently manage metadata (i.e. associate meaning to a dataset)?

* Computation

  * What software do you use, especially domain specific software?
  * Do you find your computations take a significant amount of time?
  * What is your experience with HPC resources currently offered
    (`Beocat <beocat_>`_)?
  * What is your comfort level with the Linux terminal?
  * If you had unlimited computing resources, what might you do that you feel
    you can't do now?

.. _beocat: https://support.beocat.ksu.edu/BeocatDocs/index.php/Main_Page


What we learned
===============

Provenance, Size & Formats
--------------------------

Rat behavioral data (MED-PC)
  10s of GB per year, ASCII files

Eye tracking data (EyeLink) from driving simulations
  < 10 TB currently, under 1 TB per year

Human EEG data
  < 100 GB per year

Rodent fMRI imagery
  100 GB - 1 TB in current size, 100 GB per year, nifti format

Rodent behavioral video
  100 GB - 1 TB in current size, 100 GB per year, *.mp4

2D optical brain images
  10 - 100 GB in current size, 10 GB per year, unknown

Human cognitive tasks which are encoded into text files via a Livecode program
  < 1 GB in current size, < 10 GB per year, ASCII

Sharing
-------

Data will need to be shared both within labs and with external collaborators.
Common data sharing methods currently in use include:

* Email
* External Hard Drives
* Dropbox
* Google Drive

Backup
------

Data stored with cloud providers is inherently backed up on distributed,
redundant infrastructure.  For those not using cloud storage, backup
strategies may be in place but are not automated or monitored.

Metadata
--------

* Metadata tends to be included in file names.
* Schemata tend to be undocumented, known only to those within a lab.
* As such, data is not easily searchable by its metadata.

.. image:: /_static/metadata.png
   :width: 600 px
   :align: center

Software Packages
-----------------

Software packages include:

* EyeLink
* IDKSnap
* JMP
* Matlab
* MED-PC
* Python
* R (lme4, brms, lattice, ggplot2)
* SPSS
* Statistica

General
-------

* Some users are less comfortable with a command line interface
* Public hosting of prepared data sets is desired
* Reproducibility is highly valued
* Some processes rely on passing around hard drives
* The ability to search data sets is desired