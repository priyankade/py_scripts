"""
1. Reading the file
2. extract IP address and error and success logs
3. save the output in csv/excel file
4. send mail
"""
import re #regular expression
# import pandas as pd
import datetime
from dateutil.parser import parse


logfile = open("server.log", "r") #read only file

# regex for IP address pattern (Source: GeeksforGeeks)
# use r - raw string handles space sequences etc.
ip_pattern = r"((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]?)"

ip_add_lst = []
success_list = []
error_4xx_list = []
error_5xx_list = []
success_count = 0
error_4xx_count = 0
error_5xx_count = 0

starttime = datetime.datetime.strptime('22/Jan/2019:03:56:14 +0330', '%d/%b/%Y:%H:%M:%S +0330')
endtime = datetime.datetime.strptime('22/Jan/2019:03:56:27 +0330', '%d/%b/%Y:%H:%M:%S +0330')
print(f"Start time is {starttime}")
print(f"End time is {endtime}")

for log in logfile:
    ip_add = re.search(ip_pattern, log)    #iterating through line by line and searching IP pattern
    # print(ip_add)  #gives the index (0,12)
    # print(ip_add.group())
    ip_add_lst.append(ip_add.group())
  
        
    log_list = log.split(" ")              # splits the log line string into a list
    # print(log_list)
    for i in range(len(log_list)):
        time = log_list[3]
        parsed_time = datetime.datetime.strptime(time, '[%d/%b/%Y:%H:%M:%S')
        # print(f"Current time is {time}")
        # print(f"Current parsed_time is {parsed_time}")
        if parsed_time >= starttime and parsed_time <= endtime: 
            if log_list[i] == "200":
                success_count += 1
                success_list.append(log_list)
            elif log_list[i].startswith("4"):
                error_4xx_count += 1
            elif log_list[i].startswith("5"):
                error_5xx_count += 1
                          
    
# print(ip_add_lst)
print("No. of IPs/ same as lines", len(ip_add_lst))

print("No. of success HTTP 200 code responses are:", success_count)
print("No. of error HTTP 4xx code responses are:", error_4xx_count)
print("No. of error HTTP 5xx code responses are:", error_5xx_count)
# print(f"The success list is: {success_list}")

# df = pd.DataFrame(columns=["IP Address", "2xx response", "4xx response"])
# df["IP Address"] = ip_add_lst
# df["2xx response"] = success_list
# df["4xx response"] = error_4xx_list
# pprint.pprint(df)
# df.to_csv("output.csv", index=False)
