
#Import the os to get the directoy details
import os

#Get the current working directory
current_working_directory = os.getcwd()

#This code will help to generate 1000 or n number of server urls for querying.
total_count = 1
server_txt_file = current_working_directory+"//server.txt"
#Open the file in write mode
with open(server_txt_file, "w") as f:
    #Loop through total count
    for i in range(total_count):
        #write to the file
        f.write('http://revsreinterview.s3-website-ap-northeast-1.amazonaws.com/hosts/host{}/status\n'.format(i))
