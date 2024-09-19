"""
process_purchases.py

A Python script that processes a JSON file containing purchase data from retail, calculates and returns:
- Total volume of spend
- Average purchase value
- Maximum purchase value
- Median purchase value
- Number of unique products purchased

It also includes error handling for file loading and JSON parsing
"""

import os
import json
import logging # For production ready logging
 


def read_file(file_name):

    """
    Reads a json file format

    Args:
        filename (string): json file in the current working directory

    Returns:
        List of json : Reads the json object and returns it as list
    """

    # Get complete current working directory (to ensure the script works regardless of where it is being executed)
    ## Assumption: file will be available within the same directory
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, file_name)

    try:
        logging.info("Loading JSON data...")
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found")
        print(f"file {file_path} was not found.")
        exit(1)
    except Exception as e:
        logging.error(f"{e}")
        print(f"An unexpected error occurred: {e}")
        exit(1)
    
    return data


def calculate_median(purchase_data):
    """
    Calculate the median value from the purchase_data dictionary.

    Args:
        purchase_data (dict): A dictionary with purchase IDs as keys and purchase amounts as values.

    Returns:
        float: The median of the purchase amounts. Returns 0 if no data is present.

    Median calculation Example

    # [1, 2, 3, 4, 5, 6]
    # (3+4)/2
    # (list[2] + list[3]) / 2
    # ((len(list) - 1)/2) + len(list)/2

    """
    # Check if the dictionary is not empty
    if len(purchase_data) > 0:
        # Get the sorted list of purchase amounts (values from the dictionary)
        sorted_purchase_values = sorted(purchase_data.values())
        length_purchase_values = len(sorted_purchase_values)
        index = (length_purchase_values - 1) // 2

        # If even number of elements, take the average of the middle two
        if length_purchase_values % 2 == 0:
            return (sorted_purchase_values[index] + sorted_purchase_values[index + 1]) / 2
        else:
            # If odd, return the middle element
            return sorted_purchase_values[index]
    else:
        # Return 0 if the dictionary is empty
        print("No data")
        return 0



def parse_json(data):
    """
    Process Data to print values to the STDOUT
    """

    total_volume_of_spend = 0
    unique_purchases = []
    purchase_data = {}  # Dictionary to store purchase_id as keys and purchase_total as values

    #Using set instead of list as it provides a set of unique elements by default
    unique_products = set()

    for purchase in data:
        value_per_purchase = 0
        for item in purchase['items']:
            # Store quantity, purchase and price
            quantity = int(item.get('quantity', 0))  # Default to 0 if quantity is missing
            price = float(item.get('price', 0))  # Default to 0 if price is missing
            total_volume_of_spend += price * quantity
            value_per_purchase += price * quantity
            unique_products.add(item['product_name']) # Automatically check unique product name
            
        # Store unique purchases, Assumption: purchase id might not be unique
        if purchase['purchase_id'] not in purchase_data:
            purchase_data[purchase['purchase_id']] = value_per_purchase
            # As a dict, store purchase_id and price

    # Calculate average
    if len(purchase_data) > 0:
        avg_purchase_value = total_volume_of_spend / len(purchase_data)
    else:
        avg_purchase_value = 0  # Handle division by zero


    # Calculate max value if the dict is non null
    max_purchase_value = max(purchase_data.values(), default = 0)

    # Get the median purchase value
    median = calculate_median(purchase_data)

    # Get the number of unique products purchased
    number_of_unique_products = len(unique_products)


    # Print final results
    results = {
            "Total Volume of Spend": f"${total_volume_of_spend:,.2f}",
            "Average purchase value": f"${avg_purchase_value:,.2f}",
            "Maximum purchase value": f"${max_purchase_value:,.2f}",
            "Median purchase value": f"${median:,.2f}",
            "Number of unique products purchased": number_of_unique_products
        }


    # Print the results in JSON format
    logging.info("Printing results...")
    return results


# Only execute when the file is executed directly, not while being imported as module
if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    # Extendible, this can be an api call too
    read_data = read_file('purchases_v1.json')
    results = parse_json(read_data)
    print(json.dumps(results, indent=2))
