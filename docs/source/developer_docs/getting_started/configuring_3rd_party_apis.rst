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


Getting an Agave API Token
~~~~~~~~~~~~~~~~~~~~~~~~~~

