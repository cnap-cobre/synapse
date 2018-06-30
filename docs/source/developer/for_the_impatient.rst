#################
For the Impatient
#################

This page makes the following assumptions:

* You have Git, Docker, and Docker Compose installed.
* You have SSH keys configured with Github.
* You have done ``sudo usermod -aG docker $USER`` to add yourself to
  the docker group.
* You already have an
  `Agave account <https://public.agaveapi.co/create_account>`_,
  Dropbox account, and `Globus <https://www.globus.org/>`_ acount.

1. Download and Start
=====================

.. code-block:: bash
   :linenos:

   git clone git@github.com:cnap-cobre/synapse.git
   cd synapse
   cp backend/global/settings/secret.py.example backend/global/settings/secret.py
   docker-compose build
   docker-compose up --no-start
   docker-compose run backend python manage.py migrate
   docker-compose run backend python manage.py createsuperuser
   docker-compose up

The site will be accessible via https://localhost/

Self-signed certificate errors should be expected.

2. Housekeeping
===============

Go to https://localhost/admin/sites/site/ and change the default site object to:

.. code-block:: python

   domain_name = 'localhost'
   display_name = 'localhost'

3. Configure 3rd Party APIs
===========================

3.1 Agave
---------

Use the AgaveCLI to get a client ID and client secret.

.. code-block:: bash

   git clone git@bitbucket.org:agaveapi/cli.git agave-cli
   export PATH=$PATH:`pwd`/agave-cli/bin
   tenants-init --tenant 1
   clients-create -N cli_client -D "My client name" -u "$AGAVE_USERNAME" \
   -p "$AGAVE_PASSWORD"

Go to https://public.agaveapi.co/store/ and set the following as a Redirect
URI for your app: ``https://localhost/accounts/agave/login/callback/``

Go to https://localhost/admin/socialaccount/socialapp/ and add a new Social
Account for Agave:

* Name = ``Agave``
* Client ID = ``YOUR_AGAVE_CLIENT_ID``
* Secret Key = ``YOUR_AGAVE_CLIENT_SECRET``
* Key can be empty
* Sites: Add ``localhost`` to the "chosen sites" list.


3.2 Dropbox
-----------

Go to https://www.dropbox.com/developers/apps

Create an app.  Select "Dropbox API" and "Full Dropbox".  Set the following as
a Redirect URI: ``https://localhost/accounts/dropbox/login/callback/``

Go to https://localhost/admin/socialaccount/socialapp/ and add a new Social
Account for Dropbox:

* Name = ``Dropbox``
* Client ID = ``YOUR_DROPBOX_APP_ID``
* Secret Key = ``YOUR_DROPBOX_APP_SECRET``
* Key can be empty
* Sites: Add ``localhost`` to the "chosen sites" list.


3.3 Globus
----------

Go to https://auth.globus.org/v2/web/developers and create a new app.  Set
``https://localhost/accounts/globus/login/callback/`` as a Redirect URI and
get your client ID and secret.

Go to https://localhost/admin/socialaccount/socialapp/ and add a new Social
Account for Globus:

* Name = ``Globus``
* Client ID = ``YOUR_GLOBUS_CLIENT_ID``
* Secret Key = ``YOUR_GLOBUS_CLIENT_SECRET``
* Key can be empty
* Sites: Add ``localhost`` to the "chosen sites" list.