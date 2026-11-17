# madad

catalog geniza content / powered by pgpv4

Preliminary proof-of-concept django site that uses the PGPv4 `geniza` codebase as a dependency and installs
the `geniza.common` and `geniza.corpus` apps.

Use `uv` to install dependencies.

Requires a postgresql database — should be similar set up to geniza. Run migrations and create a db super user account (different from your netid):

```bash
python manage.py migrate
python manage.py createsuperuser
```

The application requires Solr 9.9 even though we aren't using it yet. We recommend using the provisional `docker-compose.yml` configuration. For now, this requires a path to the solr configset in a local checkout of the geniza codebase. The base path to the local checkout of the geniza codebase should be set as environment variable **GENIZA_PATH**. We recommend using [direnv](https://direnv.net/) with a `.env` or `.envrc` file something like this:

```sh
# path to geniza git checkout
GENIZA_PATH=/Users/username/documents/geniza
```

Once you have the path to `geniza` configured, run docker to start the Solr 9.9 server with the geniza solr configset.

```bash
docker compose up -d
```

You will have to create a `madad` solr collection/core the first time you do this.

Start the application with Django runserver, then open the django admin interface - you should see the corpus section with fragments and documents.
