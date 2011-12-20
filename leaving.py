#!/usr/local/bin/python

import re
import mechanize
from BeautifulSoup import BeautifulSoup

def remove_html_tags(data): # Function for removing all HTML tags from a string
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def leaving_from(location="Utrecht Overvecht"): # Get all vehicles leaving at a certain station
    
    # Build a browser and navigate to the 9292 mobile website
    br = mechanize.Browser() 
    br.open("http://m.9292.nl/")
    
    # Select the second form and populate it with the location data
    br.select_form(nr=1)
    br['q'] = location
    
    # Submit the form and put the response in Beautiful Soup
    response = br.submit()
    html = BeautifulSoup(response.read())
    
    
    #
    # TODO: Build somethign to better catch errors and see if the times ar e
    #
    
    try:
        # Filter for trains and strip all HTML
        vehicles = html.findAll("tbody")[0]

        # Cycle trough the table and build a list containing dictionaries with all information
        leaving = []
        for vehicle in str(vehicles).split("</tr>\n<tr>"):
            # Remove spaces/html and make a list of the table
            v = remove_html_tags(vehicle).replace('\n'," ").strip().split(' ')
            
            # Build the dictionary
            leave = {'time': v[0], 'direction': ' '.join(v[1:-1]), 'number': v[-1]}
            leaving.append(leave) # Append to the list
            
        return leaving #Return if succesfull
    except:
        return "Something went wrong.. Did you got the name right?" # Make this more verbose
        
