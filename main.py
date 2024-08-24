import time

services_classed = dict()

Logo="""
  ___           _        _   _           _   
 |_ _|_ __  ___| |_ __ _| | | | ___  ___| |_ 
  | || '_ \/ __| __/ _` | |_| |/ _ \/ __| __|
  | || | | \__ \ || (_| |  _  | (_) \__ \ |_ 
 |___|_| |_|___/\__\__,_|_| |_|\___/|___/\__|
"""

print(Logo)

# Collects the Username of the current user and determines the root directory
username = input("Please enter the name of your newly created user (Case Sensitive): ")

RootDir = "/home/" + username + "/instahost"

print("The directory where your services will be installed is: " + RootDir)

time.sleep(1)

# Determines Timezone
customTimezone = input("Would you like to use a custom timezone? If not, it will be set to your systems time zone (reccommended) (y/n)")
if customTimezone == n:
    timezone = open("/etc/timezone", "r").readline()
else:
    print ("Please refer to this guide: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")
    timezone = input("Please enter your timezone: ")

# Opens a new file called "docker-compose.yml" in write mode
compose = open('docker-compose.yml', 'w')

# Adds the services header to the docker compose file
compose.write(
    '---\n'
    'services:\n'
)

