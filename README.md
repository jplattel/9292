# A basic crawler for m.9292.nl to get all leaving vehicles from a bus/trainstop

## Dependencies

*	BeautifulSoup
*	Mechanize

## Usage

Import the libary and use the function leaving_from()

	import leaving
	leaving.leaving_from('Utrecht Centraal')
	
This should return a dictionary containing all vehicles leaving from that stop. The number in the dictionary is either the track or number for the train and bus.

## Todo

Make it more verbose and robust.
