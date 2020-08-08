# Twitter Code Challenge
"""
Create a tool that will query the ‘status’ page on 1000 fictitious servers listed in “server.txt”, and 
create a report based on data within the status pages. 

Each server has a ‘status’ endpoint that returns JSON data with the service information, a count of requests, 
and a success count. The tool report the aggregated success rate (total success / total requests) 
broken down by application and version. 

Sample endpoint:
http://revsreinterview.s3-website-ap-northeast-1.amazonaws.com/hosts/host211/status 
(you can find other endpoints at /hosts/host0/status, /hosts/host1/status, ..., /hosts/host999/status).

{
  "requests_count": 96447, 
  "application": "WebApp1", 
  "version": "2.0", 
  "success_count": 96427, 
  "error_count": 20
}

Sample Report Output:
WebApp1,1.0,60.0
WebApp1,1.3,90.5
WebApp2,2.0,21.5

"""

# from server_utils class Import the ServerAPI function
from server_utils import ServerAPI
# Import os module to get the current working directory.
import os

# Initialize the serverAPI Class
serverapi = ServerAPI()


def _calculate_aggregated_success_rate(success_count, requests_count) -> float:
    return round(((success_count * 1.0) / (requests_count * 1.0)) * 100.0, 2)


class ServerReport(object):
    # Constructor to initialize the server text location and server report list.
    def __init__(self):
        # server text file location.get the current working directory
        current_working_dir = os.getcwd()
        self._server_text_file = current_working_dir + "//server.txt"

    # Function to read the server.txt file and fetch all the APIs,
    # The Assumption here it is use apis, instead of the full urls, where the base url is captured in the class file,
    # This works only for the particular base url, and expecting a particular set of json format.
    def _get_apis_from_text_file(self) -> list:
        # Initialize the server url set
        server_urls = set()
        # Travers through the file and read the APIs and hit the URLs to get the status.
        with open(self._server_text_file) as file:
            for urls in file:
                # As the contents are coming from the file, and it the new line character is getting added,
                # and server is not accepting any wild characters, so right stripping the \n or new line of control n
                # from the urls. Concatenate the base url with apis
                server_url = urls.rstrip()
                # Add all the urls in to the server_url list, so the file can be closed after that, this will reduced
                # the memory and device opening.
                server_urls.add(server_url)
        # return the server_urls
        return server_urls

    # Function to run the server report,
    # This runs through the urls in the server_url list and get the json format response, and makes the server report
    def get_server_report(self) -> bool:
        # Initialize the list to capture all the server responses.
        server_responses = []

        # Get the Server URLs in a list,
        server_urls = self._get_apis_from_text_file()
        # Loop around the server url list, and hit the url and get the status and response
        print("*********************************************************************")
        for server_url in server_urls:
            # Hit the Server URL and get the Status, if success return 200 OK and the response, if error, return 403
            server_response, status = serverapi.get_server(server_url)
            if not status:
                print(server_response)
                print("Error in getting the response from {}".format(server_url))
                continue
            # print(server_response)
            # Add a new attribute - visited in the json dictionary
            server_response['visited'] = True
            # Add the json dictionary to the list.
            server_responses.append(server_response)

        # Once we get all the server response, call the _get_aggregated_success_rate function to calculate the
        # aggregated success rate depends upon the application and version
        server_reports = self._get_aggregated_success_rate(server_responses)

        # Display the Server Report
        self._display_server_report(server_reports)
        return True

    def _get_aggregated_success_rate(self, server_responses) -> list:
        # Initialize the list for capturing the final server records
        server_reports = []
        server_responses_len = len(server_responses)
        # Traverse through the dictionaries and get it compared with rest of the elements in the dictionaries
        # Searching the dictionary -
        # Ends up in 2 loops, 1 for fetching the first record, second loop for searching and calculating the results.

        for first_itter in range(server_responses_len):
            # Check if the record is already visited
            if server_responses[first_itter]['visited']:
                success_count = 0
                requests_count = 0
                aggregated_success_rate = 0
                # To check the single instance of the application
                single_instance = True
                # Initialize the temporary list for storing the server reports.
                report = []
                # Fetch the records.
                application = server_responses[first_itter]['application']
                version = server_responses[first_itter]['version']
                success_count = server_responses[first_itter]['success_count']
                requests_count = server_responses[first_itter]['requests_count']

                # Update the visited to False,
                server_responses[first_itter]['visited'] = False

                # Traverse through the list with incremented by 1 and search for the application and version.
                for second_itter in range(first_itter + 1, server_responses_len):
                    if application == server_responses[second_itter]['application'] and version == \
                            server_responses[second_itter]['version'] and server_responses[second_itter]['visited']:
                        # Updated second itter visited to False
                        server_responses[second_itter]['visited'] = False
                        # Multiplied it with 1.0 to ensure the decimal values and rounded to the nearest value.
                        # Aggregated Success Rate = Total Success / Total Requests * 100 aggregated_success_rate =
                        # success_count / request_count  * 100 depends upon the application and version.
                        if ((requests_count >= 0.0 or type(requests_count) == type(int) or type(requests_count) == type(
                                float)) and
                                (success_count >= 0 or type(success_count) == type(int) or type(success_count) == type(
                                    float))):
                            # Get the total success count of the application and version
                            success_count += server_responses[second_itter]['success_count']
                            # Get the total requests count of the application and version
                            requests_count += server_responses[second_itter]['requests_count']
                            # Calculate the aggregated_success_rate, rounding off to 2 decimal points to get the
                            # approximate value
                            aggregated_success_rate = _calculate_aggregated_success_rate(success_count,
                                                                                         requests_count)
                            single_instance = False

                # If it hits only 1 url or dictionary with 1 application,
                # aggregated_success_rate has to be calculated.
                if single_instance:
                    aggregated_success_rate = _calculate_aggregated_success_rate(success_count, requests_count)
                # Append the report structure to the temporary list
                report.append(application)
                # Converting the aggregated success rate and version to string format, so it is easy to append the
                # coma ",", later while displaying.
                report.append(str(version))
                report.append(str(aggregated_success_rate))
                # append to the parent server_reports.
                server_reports.append(report)
        # Return the server_reports
        return server_reports

    # Function to display the server reports in
    # application name,
    # version,
    # aggregated success rate
    def _display_server_report(self, server_reports) -> bool:
        # Print the full report, with application name, version, and aggregated_success_rate
        print("\n")
        print("*********************************************************************")
        print("Server Report Output")
        print("*********************************************************************")
        server_count = 0
        for values in server_reports:
            server_count += 1
            serverreport = ', '.join(values)
            print("{}".format(serverreport))

        print("*********************************************************************")
        print("Retrieved {} Server Reports".format(server_count))
        print("*********************************************************************")
        return True


# Main function.
def main():
    # Calling the Server Report Class and retrieves the report.
    serverreport = ServerReport()
    # Call the server report
    if not serverreport.get_server_report():
        print("Not able to produce the Server Report")


if __name__ == "__main__":
    main()
