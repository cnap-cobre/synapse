## Getting Started

1. Copy .../dms/global/settings/secret.example.py to secret.py in the same directory
2. Update the secret key in secret.py to something random.
3. Run `docker-compose build`
4. Run `docker-compose up` to launch the project

## Modes

By default, the project starts in development mode.  To run in other modes, we reference alternate *.yml files specifying an alternate docker-compose configuration.  For example,  `docker-compose -f prod.yml up` launches the project in production mode.
