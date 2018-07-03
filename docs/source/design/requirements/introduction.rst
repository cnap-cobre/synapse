############
Introduction
############

The following Software Requirements Specification document defines all
requirements for Synapse, a data management platform for the Psychological
Sciences.

Purpose
=======

The purpose of this document is to clearly identify and define all
requirements provided by stakeholders.  This document will serve
as a reference for contributors during the design and implementation
process and may be reviewed by stakeholders to refine and clarify
requirements.

Scope
=====

Synapse aims to augment existing research workflows by integrating with
systems and tools that researchers are already using.

With relative ease, Synapse will allow users to:

* Share data with collaborators
* Transfer data between storage systems
* Manipulate files on storage systems
* Define sharable, reusable applications for data analysis
* Launch and monitor computing jobs on research computing clusters
* Maintain metadata (descriptive, structural, administrative, provenance, etc.)
  for research data
* Produce visualizations
* Publish datasets with persistent identifiers

Synapse will not:

* Make you coffee


Definitions
===========

Beocat
  A research cluster at Kansas State University.  `Beocat <beocat_>`_ is the largest
  academic cluster in Kansas with over 8,000 processor cores.  Access
  is free to all researchers in Kansas and their collaborators.

CNAP
  The `Cognitive and Neurobiological Approaches to Plasticity Center of
  Biomedical Research <cnap_>`_ at Kansas State University

File System
  Any system on which files are stored

Globus
  `Globus <globus_>`_ is a platform offering file transfer, sharing, and search capabilities
  as well as identity management with many academic institutions.

GridFTP
  A high-performance, secure data transfer protocol which uses parallel TCP
  streams and offers checkpointing.

HTTP
  Hypertext Transfer Protocol

Identity Provider
  An entity which creates, maintains, and manages identity information for
  users and provides authentication services to dependent applications
  within a federation or distributed network.

iRODS
  The integrated Rule-Oriented Data System is a data management system which
  virtualizes data storage resources of an organization under a unified
  namespace.  It uses a metadata catalog which describes every file, directory,
  and storage resource in an iRODS Zone.

JSON - JavaScript Object Notation
  A data serialization format commonly used for data representation between
  applications on the internet.

Metadata
  Data which provides descriptive, structural, or administrative about
  other data.  Examples include: means of creation, purpose, time and date
  of creation, creator or author of the data, location where the data was
  created, file size, etc.

OAuth2.0
  An industry-standard protocol for authorization which allows applications to
  delegate user authentication to a 3rd party identity provider.  For example,
  the Dropbox "Sign In" page offers a "Sign in with Google" option.  In this
  situation, Google is the identity provider.

Representational State Transfer
  An architectural style which builds on HTTP to define a standard set of
  stateless operations between web services

SFTP
  Secure File Transfer Protocol

Abbreviated Terms
-----------------

* FTP - File Transfer Protocol
* HTTP - HyperText Transfer Protocol
* JSON - JavaScript Object Notation
* REST - Representational State Transfer
* SFTP - Secure File Transfer Protocol
* SSL - Secure Sockets Layer

.. _beocat: https://beocat.ksu.edu/
.. _cnap: http://www.k-state.edu/cnap/
.. _globus: https://www.globus.org/platform

References
==========

Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content - RFC 7231:
  https://tools.ietf.org/html/rfc7231

OAuth 2.0 Authorization Framework - RFC 6749
  https://tools.ietf.org/html/rfc6749

Semantic Versioning
  https://semver.org/

Overview
========

TODO