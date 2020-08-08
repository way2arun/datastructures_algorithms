import requests
# Import the json module to parse the string to json format
import json


def generate_url(title_name):
    url = "https://jsonmock.hackerrank.com/api/movies/search/?Title=" + title_name
    return url


def getNumberOfMovies():
    header = {
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json'
    }
    title_name = input("Enter the Title Name of the Movie:-")
    # url does not require any parameters, even headers (but giving the header with default values).
    url = generate_url(title_name)
    try:
        response = requests.get(url, headers=header)
        print("Server Response Received.."'[{}] :: [{}]'.format(response.status_code, url))
        if response.status_code != 200:
            raise requests.ConnectionError(
                f'{"Code"}{str(response.status_code)}{" "}{response.text}'
            )
    except requests.exceptions.RequestException as e:
        print("Error:: Server Request Error-"'{}'.format(e))

    movies = json.loads(response.text)
    print(movies['total'])

# Call the number of movies function
getNumberOfMovies()
