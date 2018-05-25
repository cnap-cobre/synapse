############################
Configuring 3rd Party APIs
############################

To authenticate with 3rd party APIs we use
`Django Allauth <https://github.com/pennersr/django-allauth>`_.

Sites Framework
~~~~~~~~~~~~~~~

Allauth depends on the django
`sites framework <https://docs.djangoproject.com/en/2.0/ref/contrib/sites/>`_.

First, login to the admin panel localhost/admin/ with a superuser account and
update the existing site object with the correct domain name.  For development,
just change ``example.com`` to ``localhost``.  In production, this will be
whatever your domain name is.

.. image:: /_static/django-site.png


Getting an Agave API Client Key and Secret
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, create an Agave account:
https://public.agaveapi.co/create_account

Next, download the Agave CLI to create a client:
https://bitbucket.org/agaveapi/cli/overview

In ``.../agavecli/cli/bin``, run ``./clients-create``, type in your Agave
username and password, and you should receive a key and secret.

You can manage your clients here:  https://public.agaveapi.co/store/#

To configure Django Allauth with these keys, start the application and
navigate to ``/admin/socialaccount/socialapp/add/``.  Make sure to select
``localhost`` (or whatever your domain is) as a chosen site.

.. image:: /_static/allauth-config.png


Getting a Dropbox Client Key and Secret
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At https://www.dropbox.com/developers , navigate to "My Apps".  After you
click "Create App", make sure to select the Dropbox API (rather than Dropbox
Business).  Select "Full Dropbox".