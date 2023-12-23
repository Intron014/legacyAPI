# I014 API Documentation 
###### v2.0.0 (Flask)

This project is a simple Flask API with several endpoints. It's written in Python and uses the Flask framework.

## Endpoints

The API has the following endpoints:

1. `POST /modify-clipboard-link`: This endpoint accepts a JSON payload with a `link` key. It modifies the link by replacing `?forcedownload=1` with `?forcedownload=0` in the link and returns the modified link. If the `link` key is not present in the payload, it returns an error.

2. `GET /emt-bicimad`: This endpoint returns a JSON array with data about EMT Bicimad.

3. `GET /emt-bicimad-rel`: This endpoint returns a JSON array with data about EMT Bicimad Totem relations.

4. `GET /emt-bus`: This endpoint returns a JSON array with data about EMT Bus.

## Running the Project

To run the project, execute the following command:

```bash
python main.py
```

This will start the Flask development server on `localhost:5000`.
