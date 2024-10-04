# Backend Coding Assignment: AI Infrasolutions

Instructions on how to run

1. Make sure you have `Docker` running on you device
2. Copy the provided `.env` file into the projects root directory
3. Run `docker compose up --build` to build and start a Docker container with the services defined in the `docker-compose.yaml` file
4. Confirm all containers are running, next run `docker compose exec web python manage.py createsuperuser` to create a superuser account
5. Go to `http://localhost:8000/api/token/` and send a `post` request using the superuser credentials you just created (username and password). Get an access_token
6. Load the data provided into the database by running the script found in the root directory. use the command `python load_data.py your_access_token`
7. If the last step was successful, test out the api by running the second script `python get_data.py your_access_token`
8. Alternatively you could use postman, curl, etc to test out the api

NB: in case of GDAL_LIBRARY_PATH and GEOS_LIBRARY_PATH errors, see the `.env` for details on how to get the right path on your device
