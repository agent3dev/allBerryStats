#  Poke-berries statistics API.

This API allows for the retrieval of berries from the pokeapi and calculation of some basic statistics. 
And the showcase of a histogram graph

## Installation

1. Clone the repository:

```
   git clone https://github.com/agent3dev/allBerryStats.git
```  
Create a virtual environment:

```
python -m venv venv
```

Activate the virtual environment:

For Windows:

bash
Copy
.\venv\Scripts\activate
For macOS and Linux:

bash
Copy
source venv/bin/activate
Install the required dependencies:

```
pip install -r requirements.txt
```

To launch the api execute the command:

```
./allBerryStats/venv/bin/python ./allBerryStats/main.py 
```

Adjusting the routes if necessary.

The following endpoints are supported:

```
GET /allBerryStats

GET /histogram
```

To launch the API tests execute the command:

```
./allBerryStats/venv/bin/pytest ./allBerryStats/test_berries.py
```
Adjusting the routes if necessary.