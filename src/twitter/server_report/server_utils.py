# Twitter Code Challenge.

# Import the requests library to query urls.
import requests
# Import the json module to parse the string to json format
import json


# Class ServerAPI for API CRUD operations, data and functionality is together.
class ServerAPI(object):

    # Constructor to initialize the class with header value.
    def __init__(self):
        self._header = {
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json'
        }

    # Function to do the GET Operation,
    def get_server(self, server_url) -> tuple:
        try:
            # Initialize the status and the response_json with none.
            status = True
            response_json = ""
            # Server url does not require any parameters, even headers (but giving the header with default values).
            response = requests.get(server_url, headers=self._header)
            print("Server Response Received.."'[{}] :: [{}]'.format(response.status_code, server_url))
            if response.status_code != 200:
                raise requests.ConnectionError(
                    f'{"Code"}{str(response.status_code)}{" "}{response.text}'
                )
            # The response is coming in "binary/octet-stream", hence converting to json format.
            # un-comment the print for debugging and testing
            # print(response.headers['Content-Type'])
            # Convert the string/txt to json format.
            response_json = self._parse_string_to_json(response.text)
        except requests.exceptions.RequestException as e:
            print("Error:: Server Request Error-"'{}'.format(e))
            status = False
        # Return the value in json format
        return response_json, status

    # Function to parse the String to JSON format,
    def _parse_string_to_json(self, response) -> object:
        # Return the parsed json value
        return json.loads(response)
