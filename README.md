<!-- ABOUT THE PROJECT -->
## About The Project

Save & Load List Flask API

Developed to Faciliate the saving/loading of a passed list.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

- Python
- Flask

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is a Flask API developed to Save/Load a passed list of items with HTTPS requests.

### Prerequisites

Python must be installed along with the following modules:

- Flask
- Json
- os
- requests


### Installation

1) Download Python & make sure your the modules above have been installed.
2) Clone the Repository to your local machine
3) Open the repository in your IDE, and open a terminal in the file location of the "Microservice" folder.
4) Type in the terminal "flask run", this will automatically run "app.py" which is in the Microservice folder.
5) The terminal will show that the Flask API is running on your machine, and it will give you the IP address of the server.
6) Done!

If you run into trouble, make sure your modules are downloaded correctly and that you have the updated version of Python.

In the application you're using to call the API you need to import these modules: requests, json.

<!-- USAGE EXAMPLES -->
## Communication Contract

There is 1 main function of this API: To Save and Load a list of data.

Within the API there are two method calls you can use:

1) /data_get - Returns a JSON file from the JSON file within the API. 
2) /data_save - Saves a passed list to the API's JSON file.

An example of the code needed to sucessfully save a list to the API is as follows:

test_list = [1,2,3,4,5]

        json_data = json.dumps(test_list)
        headers = {'Content-Type': 'application/json'}
        response = requests.get('http://127.0.0.1:5000/data_get', data=json_data, headers=headers).json()

In this example the test_list is being converted to a JSON format, and then an HTTPS requests is being made
to "http://127.0.0.1:5000/data_get". This is the IP address of the API. The important part of this request is the .get and the /data_get URL which tells the requests method that you're sending information and where to send it. e.g saving and sending the list to the API.

If I wanted to load that same list I would change the .get to .post and the url to /data_save in the response variable to the following:

        response = requests.post('http://127.0.0.1:5000/data_save', data=json_data, headers=headers).json()

If you request the data, the response variable will be assigned with the JSON file!

<!-- ROADMAP -->
## Roadmap

<img width="908" alt="Screenshot 2023-05-08 at 10 15 44 PM" src="https://user-images.githubusercontent.com/65273756/237004489-38ccc889-3d3b-4511-bc09-48be2796e3d3.png">


<!-- CONTRIBUTING -->
## Contributing


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact




<p align="right">(<a href="#readme-top">back to top</a>)</p>

