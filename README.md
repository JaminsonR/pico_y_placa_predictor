# Pico y Placa Predictor

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Flask 1.1.2
- Python 3.7.3
- Pytest 6.0.1

## Getting Started

Clone this project in your local machine executing the following instructions:

```
git clone https://github.com/JaminsonR/pico_y_placa_predictor.git
```

### Setting up the server

1. Install the requirements inside of a Python venv.
   .. code:: sh
   cd server
   python3 -m venv venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python api.py

2. Start server
   .. code:: sh
   python api.py

### Setting up the webapp

The webapp should be accessible at local http://localhost:8080/

## Running API Tests

This project uses pytest for testing the API.

Navigate to the API directory
.. code:: sh
cd server
Activate the venv
.. code:: sh
source .venv/bin/activate
And run the following command to start the tests:
.. code:: sh
pytest

## Author

- **Jaminson Riascos**
