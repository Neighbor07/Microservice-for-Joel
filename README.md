# Microservice-for-Joel
Currency Converter
Communication Contract

The currency converter microservice will take in 3 values. Two of them will be values that will be the currency. For example, USD (Dollar) and AUD (Australian currency). It uses a rest API with flask and the server is hosted locally with a port number 3125. 

Requesting Data

Run the form locally on port 3125 to request data from the microservice. Type in python3 convert.py into the terminal and the program should be hosted on a server. Then the server/form will request the user's input for from_currency, to_currency, and amount. Once the form is submitted, JavaScript takes the data and sends a POST request to the Flask server with the data submitted by the user. 
![Screenshot (41)](https://github.com/Neighbor07/Microservice-for-Joel/assets/167046423/629004f5-897b-4b23-a21b-72b21d002358)


Receiving Data

To receive data, the flask server takes the POST request and extracts the data from the form. The server takes in the data to request the exchange rate from the link that is in the URL. The server processes the API response and calculates the converted amount and sends back the converted amount back to the client. 


Address
The address will be what is said in the convert.py. (http://127.0.0.1:3125 and 3125). It is 3125 because the other port said being used. Feel free to change it if 3125 is not operating. 

UML Sequence Diagram

Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.
Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.
UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.
