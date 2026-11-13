# madad

catalog geniza content / powered by pgpv4

Preliminary proof-of-concept django site that uses the PGPv4 `geniza` codebase as a dependency and installs
the `geniza.common` and `geniza.corpus` apps.

Use `uv` to install dependencies.

Requires a postgresql database — should be similar set up to geniza. Run migrations and create a db super user account (different from your netid):

```bash
python manage.py migrate
python createsuperuser
```

The application requires solr even though we aren't using it yet; recommend using the provisional `docker-compose.yml` file. Manually edit the yml to set the path for the solr configset to a local checkout of the geniza codebase, then start with:

```bash
docker compose up -d
```

Start the application with Django runserver, then open the django admin interface - you should see the corpus section with fragments and documents.
