# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 07:59:12 2024

@author: adiaz
"""

import requests

# Updated token using x-api-key
API_KEY = '816ce8543f358a07dc2497168c07d5e9d844bd7e57415728e3c413b0cf0237f6'
BASE_URL = 'https://api.esios.ree.es/indicators'

def list_indicators():
    headers = {
        'Accept': 'application/json; application/vnd.esios-api-v2+json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }

    try:
        # GET request to list all indicators
        response = requests.get(BASE_URL, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Show the first 10 indicators as an example
        for indicator in data['indicators'][:10]:
            print(f"ID: {indicator['id']}, Name: {indicator['name']}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Call the function to list indicators
list_indicators()



# Function to obtain data from the selected indicator
def get_indicator_data(indicator_id, start_date, end_date):
    headers = {
        'Accept': 'application/json; application/vnd.esios-api-v2+json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }
    
    # Define the specific URL for the indicator
    url = f"{BASE_URL}/{indicator_id}"
    
    # Define the parameters, including the geo_id for Canary Islands (8742)
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'time_trunc': 'day',  # Could be 'hour' if you need higher granularity
    }

    try:
        # Perform the GET request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Process and display the retrieved data
        values = data.get('indicator', {}).get('values', [])
        if values:
            print(f"Data retrieved for indicator {indicator_id}:")
            for value in values[:5]:  # Display the first 5 data points
                print(f"Date: {value['datetime']}, Value: {value['value']} MW")
        else:
            print(f"No data found for indicator {indicator_id}.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Specify the dates of interest (in ISO 8601 format)
start_date = '2024-09-24T00:00:00Z'
end_date = '2024-09-30T23:59:59Z'

# Call the function to get data for the combined cycle indicator (ID: 9)
get_indicator_data(9, start_date, end_date)



# Function to retrieve data from the selected indicator
def get_indicator_data(indicator_id, start_date, end_date):
    headers = {
        'Accept': 'application/json; application/vnd.esios-api-v2+json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }
    
    # Define the URL for the specific indicator
    url = f"{BASE_URL}/{indicator_id}/values"
    
    # Define the parameters, including the geo_id for Canary Islands (8742)
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'time_trunc': 'day',  # Can be 'hour' if you need more granularity
        'geo_ids[]': 8742  # Geographic ID for Canary Islands
    }

    try:
        # Make the GET request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Process and display the retrieved data
        values = data.get('indicator', {}).get('values', [])
        if values:
            print(f"Data retrieved for indicator {indicator_id}:")
            for value in values[:5]:  # Display the first 5 data points
                print(f"Date: {value['datetime']}, Value: {value['value']} MW")
        else:
            print(f"No data found for indicator {indicator_id}.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Specify the dates of interest (in ISO 8601 format)
start_date = '2024-09-24T00:00:00Z'
end_date = '2024-09-30T23:59:59Z'

# Call the function to retrieve data for the Fuel indicator (ID: 10)
get_indicator_data(10, start_date, end_date)



# Updated Token (using x-api-key)
API_KEY = '816ce8543f358a07dc2497168c07d5e9d844bd7e57415728e3c413b0cf0237f6'
BASE_URL = 'https://api.esios.ree.es/indicators'

def list_indicators():
    headers = {
        'Accept': 'application/json; application/vnd.esios-api-v2+json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }

    try:
        # GET request to the API to list indicators
        response = requests.get(BASE_URL, headers=headers)
        response.raise_for_status()
        data = response.json()

        # List some indicators as an example
        for indicator in data['indicators'][:10]:  # Show the first 10
            print(f"ID: {indicator['id']}, Name: {indicator['name']}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Call the function to list the indicators
list_indicators()

# Function to retrieve data from the selected indicator
def get_indicator_data(indicator_id, start_date, end_date):
    headers = {
        'Accept': 'application/json; application/vnd.esios-api-v2+json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }
    
    # Define the URL for the specific indicator
    url = f"{BASE_URL}/{indicator_id}/values"
    
    # Define the parameters, including the geo_id for Canary Islands (8742)
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'time_trunc': 'day',  # Can be 'hour' if you need more granularity
        'geo_ids[]': 8742  # Geographic ID for Canary Islands
    }

    try:
        # Make the GET request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Process and display the retrieved data
        values = data.get('indicator', {}).get('values', [])
        if values:
            print(f"Data retrieved for indicator {indicator_id}:")
            for value in values[:5]:  # Display the first 5 data points
                print(f"Date: {value['datetime']}, Value: {value['value']} MW")
        else:
            print(f"No data found for indicator {indicator_id}.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Specify the dates of interest (in ISO 8601 format)
start_date = '2024-09-24T00:00:00Z'
end_date = '2024-09-30T23:59:59Z'

# Call the function to retrieve data for the Nuclear indicator (ID: 4)
get_indicator_data(4, start_date, end_date)



# Updated Token (using x-api-key)
API_KEY = '816ce8543f358a07dc2497168c07d5e9d844bd7e57415728e3c413b0cf0237f6'
BASE_URL = 'https://api.esios.ree.es/indicators'

def search_indicator_by_name(keyword):
    headers = {
        'Accept': 'application/json; application/vnd.esios-api-v2+json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }

    try:
        # GET request to the API to list all indicators
        response = requests.get(BASE_URL, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Filter indicators by keyword in the name
        found_indicators = [
            indicator for indicator in data['indicators'] if keyword.lower() in indicator['name'].lower()
        ]

        # Display indicators that contain the keyword
        if found_indicators:
            print(f"Indicators that contain the keyword '{keyword}':")
            for indicator in found_indicators:
                print(f"ID: {indicator['id']}, Name: {indicator['name']}")
            return found_indicators
        else:
            print(f"No indicators found with the keyword '{keyword}'.")
            return []

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Call the function to search for indicators that contain 'ciclo combinado'
search_indicator_by_name("ciclo combinado")



# Updated Token (using x-api-key)
API_KEY = '816ce8543f358a07dc2497168c07d5e9d844bd7e57415728e3c413b0cf0237f6'
BASE_URL = 'https://api.esios.ree.es/indicators'

def get_indicator_data(indicator_id, start_date, end_date, geo_id):
    headers = {
        'Accept': 'application/json; application/vnd.esios-api-v2+json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }
    
    # Define the URL for the specific indicator
    url = f"{BASE_URL}/{indicator_id}/values"
    
    # Define the parameters, including the geo_id for Tenerife (8743)
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'time_trunc': 'day',  # Can be 'hour' if you need more granularity
        'geo_ids': [geo_id]  # Geographic ID for Tenerife
    }

    try:
        # Perform the GET request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Process and display the obtained data
        values = data.get('indicator', {}).get('values', [])
        if values:
            print(f"Data retrieved for indicator {indicator_id} in geo_id {geo_id}:")
            for value in values[:5]:  # Show the first 5 data points
                print(f"Date: {value['datetime']}, Value: {value['value']} MW")
        else:
            print(f"No data found for indicator {indicator_id} in geo_id {geo_id}.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Specify the new dates of interest (in ISO 8601 format)
start_date = '2024-08-01T00:00:00Z'
end_date = '2024-08-31T23:59:59Z'

# Call the function to retrieve data for the "Ciclo combinado measured generation" indicator (ID: 1156) for Tenerife
geo_id_tenerife = 8743
get_indicator_data(1156, start_date, end_date, geo_id_tenerife)


# Token updated (using x-api-key)
API_KEY = '816ce8543f358a07dc2497168c07d5e9d844bd7e57415728e3c413b0cf0237f6'
BASE_URL = 'https://api.esios.ree.es/indicators'

def get_indicator_data(indicator_id, start_date, end_date, geo_id):
    headers = {
        'Accept': 'application/json; application/vnd.esios-api-v2+json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }
    
    # Define the URL for the specific indicator
    url = f"{BASE_URL}/{indicator_id}"
    
    # Define the parameters, including the geo_id for Tenerife (8743)
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'time_trunc': 'day',  # Can be 'hour' if you need more granularity
    }

    try:
        # Perform the GET request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Process and display the obtained data
        values = data.get('indicator', {}).get('values', [])
        if values:
            print(f"Data retrieved for indicator {indicator_id} in geo_id {geo_id}:")
            for value in values[:5]:  # Show the first 5 data points
                print(f"Date: {value['datetime']}, Value: {value['value']} MW")
        else:
            print(f"No data found for indicator {indicator_id} in geo_id {geo_id}.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Specify the dates of interest (in ISO 8601 format)
start_date = '2024-09-24T00:00:00Z'
end_date = '2024-09-30T23:59:59Z'

# Call the function to retrieve data for the "Ciclo combinado measured generation" indicator (ID: 1156) for Tenerife
geo_id_tenerife = 8743
get_indicator_data(1156, start_date, end_date, geo_id_tenerife)



# Updated Token (using x-api-key)
API_KEY = '816ce8543f358a07dc2497168c07d5e9d844bd7e57415728e3c413b0cf0237f6'
BASE_URL = 'https://api.esios.ree.es/indicators'

def get_indicator_data(indicator_id, start_date, end_date, geo_id=None):
    headers = {
        'Accept': 'application/json; application/vnd.esios-api-v1+json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }
    
    # Define the URL for the specific indicator
    url = f"{BASE_URL}/{indicator_id}/values"
    
    # Define the parameters, including geo_id if provided
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'time_trunc': 'day'
    }
    
    if geo_id:
        params['geo_ids[]'] = geo_id

    try:
        # Perform the GET request
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Process and display the retrieved data
        values = data.get('indicator', {}).get('values', [])
        if values:
            print(f"Data retrieved for indicator {indicator_id}:")
            for value in values[:5]:  # Display the first 5 data points
                print(f"Date: {value['datetime']}, Value: {value['value']} MW")
        else:
            print(f"No data found for indicator {indicator_id}.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Specify the new dates of interest (in ISO 8601 format)
start_date = '2024-08-01T00:00:00Z'
end_date = '2024-08-31T23:59:59Z'

# Call the function to retrieve data for the "Real-time combined cycle generation SNP" indicator (ID: 1746)
get_indicator_data(1746, start_date, end_date, geo_id=None)



import requests

# Updated token using x-api-key
API_KEY = '816ce8543f358a07dc2497168c07d5e9d844bd7e57415728e3c413b0cf0237f6'
BASE_URL = 'https://apidatos.ree.es/es/datos/generacion/estructura-generacion'

def obtener_datos_generacion(start_date, end_date, time_trunc, geo_limit, geo_ids):
    headers = {
        'Accept': 'application/json; application/vnd.esios-api-v1+json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }

    params = {
        'start_date': start_date,
        'end_date': end_date,
        'time_trunc': time_trunc,
        'geo_limit': geo_limit,
        'geo_ids': geo_ids
    }

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()

        # Debugging output to check what data is returned
        print("Raw data response:", data)

        # Process and extract the data from the 'included' key
        if 'included' in data:
            for entry in data['included']:
                title = entry['attributes'].get('title', 'No title')
                values = entry['attributes'].get('values', [])

                print(f"Title: {title}")
                for value_entry in values[:5]:  # Print first 5 values for brevity
                    date_time = value_entry.get('datetime', 'No datetime')
                    value = value_entry.get('value', 'No value')
                    percentage = value_entry.get('percentage', 'No percentage')
                    print(f"  Date: {date_time}, Value: {value} MW, Percentage: {percentage}")
        else:
            print("No 'included' data found in the response.")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

# Define the parameters for the request
start_date = '2024-01-01T00:00:00'
end_date = '2024-01-31T23:59:59'
time_trunc = 'day'
geo_limit = 'ccaa'
geo_ids = '8742'  # ID for Canarias

# Call the function to get the data
obtener_datos_generacion(start_date, end_date, time_trunc, geo_limit, geo_ids)



import requests

# Example function to filter data by Tenerife
def filter_by_tenerife(data):
    # Here we assume that the data contains some key like 'location' that indicates the island
    tenerife_data = [item for item in data if item.get('location') == 'Tenerife']
    return tenerife_data

# Request to the API to get data for the Canary Islands
url = "https://api.esios.ree.es/indicators/9/values"
params = {
    "start_date": "2024-09-24T00:00:00Z",
    "end_date": "2024-09-30T23:59:59Z",
    "time_trunc": "day",
    "geo_ids[]": "8742"
}

# Making the request
response = requests.get(url, headers={"x-api-key": "your_api_key"}, params=params)

if response.status_code == 200:
    data = response.json()
    # Apply the filter to get only data for Tenerife
    tenerife_data = filter_by_tenerife(data)
    print("Filtered data for Tenerife:", tenerife_data)
else:
    print(f"Request error: {response.status_code}")
    
    

import requests

# Example function to filter data by zones within Tenerife
def filter_by_tenerife_zone(data, zone):
    # Assuming that the data contains a 'zone' or 'region' key that specifies the area within Tenerife
    filtered_data = [item for item in data if item.get('location') == 'Tenerife' and item.get('zone') == zone]
    return filtered_data

# Request to the API to get data for the Canary Islands
url = "https://api.esios.ree.es/indicators/9/values"
params = {
    "start_date": "2024-09-24T00:00:00Z",
    "end_date": "2024-09-30T23:59:59Z",
    "time_trunc": "day",
    "geo_ids[]": "8742"
}

# Making the request
response = requests.get(url, headers={"x-api-key": "your_api_key"}, params=params)

if response.status_code == 200:
    data = response.json()
    # Example zones could be 'north', 'south', 'east', 'west', or specific municipalities like 'Santa Cruz', 'La Laguna', etc.
    zone = 'north'  # You can replace this with any zone you'd like to filter by
    filtered_data = filter_by_tenerife_zone(data, zone)
    print(f"Filtered data for Tenerife - {zone} zone:", filtered_data)
else:
    print(f"Request error: {response.status_code}")
    
    
    
    
import requests

# REE e·sios API: URL and headers
url = "https://api.esios.ree.es/indicators"
headers = {
    "x-api-key": "your_api_key",
    "Content-Type": "application/json"
}

# Parameters to filter infrastructures or substations
params = {
    "geo_ids[]": "8742",  # Geo ID for Canary Islands, adapt it for Tenerife if necessary
    "category": "infrastructure",  # Assuming there's an infrastructure category
}

# Make the request to the API
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Filter for Tenerife if the data contains a location key or similar
    tenerife_substations = [sub for sub in data.get('included', []) if 'Tenerife' in sub.get('attributes', {}).get('title', '')]
    
    # Display the filtered results
    for sub in tenerife_substations:
        print(f"ID: {sub['id']}, Name: {sub['attributes']['title']}")
else:
    print(f"Request error: {response.status_code}")
    
    
