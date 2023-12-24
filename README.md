# I014 API Documentation 
###### v2.0.0 (Flask)

This project is a simple Flask API with several endpoints. It's written in Python and uses the Flask framework.

## Endpoints

The API has the following endpoints:

1. `POST /modify-clipboard-link`: This endpoint accepts a JSON payload with a `link` key. It modifies the link by replacing `?forcedownload=1` with `?forcedownload=0` in the link and returns the modified link. If the `link` key is not present in the payload, it returns an error.

2. `GET /emt-bicimad`: This endpoint returns a JSON array with data about EMT Bicimad.

3. `GET /emt-bicimad-rel`: This endpoint returns a JSON array with data about EMT Bicimad Totem relations.

4. `GET /emt-bus`: This endpoint returns a JSON array with data about EMT Bus.

5. `POST /bicimad-gethashcode`:

   - This endpoint is used to process bike data. It accepts a JSON payload with the following keys: `D1`, `D2`, `BikeNumber`, `Docker`, and `DNI`. 

   The endpoint performs the following operations:

   1. Decodes the access key and bike key.
   2. Generates a first cipher string using the provided data. The coordinates `D1` and `D2` are resized to a length of 10 characters. If the length of the first cipher string is not a multiple of 8, it is padded with `#` characters.
   3. Generates a second cipher string by encrypting the first cipher string using the decoded bike key. The encrypted string is then prefixed with `B`. If the length of the second cipher string is not a multiple of 8, it is padded with `Z` characters.
   4. Encrypts the second cipher string using the decoded access key and returns the base64-encoded result.

   > ❗️ Ojo al dato
   >
   >   If any error occurs during the encryption process, the endpoint logs the error and returns a 500 status code.


## Running the Project

To run the project, execute the following command:

```bash
python main.py
```

This will start the Flask development server on `localhost:5000`.
