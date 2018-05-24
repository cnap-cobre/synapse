############
Installation
############

Environments
~~~~~~~~~~~~

There are currently three environments: **development** (default),
**production**, and **test**.  Other environments will be created soon.  In
general, the **development** environment has all debugging output enabled
while **production** disables these for security reasons and enables
performance optimizations.

Each environment is specified in its own ``docker-compose.yml`` file.  To
specify any environment other than **development** (it is default), you
must use ``-f docker-compose-<environment>.yml``.


Get the Code
~~~~~~~~~~~~

First, clone the project: ``git clone git@github.com:cnap-cobre/synapse.git``

For read-only situations where you won't need to authenticate with Github
often (like production) the https url is perfectly acceptable.  Otherwise,
setting up an SSH key is highly recommended to save you from having to
enter your password with every ``git push``:
https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/


Configuration
~~~~~~~~~~~~~

Go into the project directory: ``cd synapse``

Copy the ``secret.py`` template and enter secret parameters:
``cp backend/global/settings/secret.py.example backend/global/settings/secret.py``

As of now, only the Django ``SECRET_KEY`` is defined in here.  This should be
something unique and unguessable.

Later, we may have other values defined here.  ``secret.py`` is deliberately
listed in .gitignore to ensure secret keys are not accidentally leaked via
Github.  You would be surprised how often people make this mistake and commit
API keys.

Building and Running
~~~~~~~~~~~~~~~~~~~~

Build the containers.  This may take a while the first time around, but may
take less time if you happen to have some of the dependencies already cached.

| For development: ``docker-compose build``
| For production: ``docker-compose -f docker-compose-prod.yml``

Start it up.  At this point, Docker will download (or use a cached) image for
Postgres and Nginx.

| Development: ``docker-compose up``
| Production: ``docker-compose -f docker-compose-prod.yml up``

At this point, you'll probably see some errors related to the database having
none of the expected tables:  ``You have 23 unapplied migration(s)...``

Ctrl+C to kill the containers, then migrate the database:
``docker-compose run backend python manage.py migrate``

Chance are, you'll probably want to crate a superuser at this point.
``docker-compose run backend python manage.py createsuperuser``

And start it back up:
``docker-compose up``

The site will be served at ``https://localhost/``.  For now we're just using
a self-signed SSL certificate, and your browser will give you a warning.
The reason we even bother with https for the development environment is
so that picky OAuth implimentations will work with us.  Typically, insecure
OAuth redirect URLs are allowed for ``localhost``, but some APIs we work with
don't allow this.