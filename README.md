# Process Purchases Python Application

## Overview
This Python script processes a JSON file containing purchase data and calculates the following:
- total Volume of Spend
- avg Purchase Value
- maximum Purchase Value
- median Purchase Value
- num of Unique Products Purchased

## Features
- Error handling for missing or invalid JSON files.
- Dockerized for portability.

## Requirements
- Python 3.9+
- Docker (optional, if using Docker)

## Running the Script Locally

Clone the repository and run via following bash:

   ```bash
   git clone 'url_link'
   cd process-purchases
   pip install -r requirements.txt
   python3 process_purchases.py

   ```

## Running the Script Docker

``` bash
    docker build -t process-purchase-docker .
    docker run process-purchase-docker
```

## Running unit tests

``` bash
python3 -m unittest discover tests  
```

## How can this me made more performant?

1. When json file is large, and doesn't fit in memory, can use ijson, which helps us read json data as a stream (incrementally) or lazy data loading.
2. Can use multi threading, to process data parallely using concurrent.features library.
