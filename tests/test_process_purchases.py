import unittest

from process_purchase import calculate_median, parse_json

class TestProcessPurchase(unittest.TestCase): # (inheriting)

    # each method to begin with test_

    def test_calculate_median_when_odd(self):
        # Test median  with an odd num of values
        purchase_data = {
            "id1": 1000,
            "id2": 2000,
            "id3": 3000
        }
        median = calculate_median(purchase_data)
        self.assertEqual(median, 2000)

    def test_calculate_median_when_even(self):
        # Test median  with an even num of values
        purchase_data = {
            "id1": 1000,
            "id2": 2000,
            "id3": 3000,
            "id4": 4000
        }
        median = calculate_median(purchase_data)
        self.assertEqual(median, 2500)

    def test_calculate_median_when_empty(self):
        # Test median calculation with no data
        purchase_data = {}
        median = calculate_median(purchase_data)
        self.assertEqual(median, 0)

    def test_parse_json(self):
        """Test parsing JSON data."""
        # Simulating a basic JSON structure with two purchases
        data = [
            {
                "purchase_id": "id1",
                "items": [
                    {"product_name": "Product A", "quantity": 2, "price": 50}
                ]
            },
            {
                "purchase_id": "id2",
                "items": [
                    {"product_name": "Product B", "quantity": 1, "price": 100}
                ]
            }
        ]

        results = parse_json(data)
        expected_results = {
            "Total Volume of Spend": "$200.00",
            "Average purchase value": "$100.00",
            "Maximum purchase value": "$100.00",
            "Median purchase value": "$100.00",
            "Number of unique products purchased": 2
        }
        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()
