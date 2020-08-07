# Pico y Placa Predictor

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Flask 1.1.2
- Python 3.7.3
- Pytest 6.0.1

## Getting Started

Clone the project:

```
git clone https://github.com/JaminsonR/pico_y_placa_predictor.git
```

### Setting up the server

1. Navigate to Server directory

```
cd server
```

2. Install the requirements inside of a Python venv.

```
python3 -m venv venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Start server

```
python api.py
```

### Setting up the webapp

1. Navigate to Webapp directory

```
cd webapp
```

2. Install dependencies.

```
npm install
```

3. Start Webapp.

```
ng serve --open
```

The webapp should be accessible at local http://localhost:4200/

## Running API Tests

This project uses pytest for testing the API.

Navigate to the API directory

```
cd server
```

Activate the venv

```
source .venv/bin/activate
```

And run the following command to start the tests:

```
pytest
```

## Author

- **Jaminson Riascos**
