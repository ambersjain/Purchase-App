import os
import json


def main():


    # Get complete current working directory (to ensure the script works regardless of where it is being executed)
    ## Assumption: file will be available within the same directory
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'purchases_v1.json')


    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print("File loaded successfully!")
    except FileNotFoundError:
        print(f"file {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


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
        if purchase['purchase_id'] not in data:
            purchase_data[purchase['purchase_id']] = value_per_purchase
            # As a dict, store purchase_id and price

    # Calculate average
    if len(purchase_data) > 0:
        avg_purchase_value = total_volume_of_spend / len(purchase_data)
    else:
        avg_purchase_value = 0  # Handle division by zero


    # Calculate max value if the dict is non null
    max_purchase_value = max(purchase_data.values(), default = 0)

    #maximum_purchase_value = max()

    # Calculate the median purchase value

    '''
    Example

    # [1, 2, 3, 4, 5, 6]
    # (3+4)/2
    # (list[2] + list[3]) / 2
    # ((len(list) - 1)/2) + len(list)/2

    '''

    if len(purchase_data) > 0:
        # First need to get sorted values in a list
        sorted_purchase_values = sorted(purchase_data.values())
        length_purchase_values = len(sorted_purchase_values)
        index = (length_purchase_values - 1) // 2

        if (length_purchase_values % 2 == 0):
            median = (sorted_purchase_values[index] + sorted_purchase_values[index + 1])/2
        else:
            median = sorted_purchase_values[index]
    else:
        print("No data")
        median = 0


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
    print(json.dumps(results, indent=2))


# Only execute when the file is executed directly, not while being imported as module
if __name__ == "__main__":
    main()