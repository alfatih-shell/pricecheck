# Price Check 
[![PyPI Version](https://img.shields.io/pypi/v/pricecheck)](https://pypi.org/project/pricecheck/)

## Overview
This project, **Price Check**, is a Python package designed to retrieve updated prices of your favorite tokens or coins via the birdeye.so platform. Additionally, it can provide alerts when specified price thresholds are reached.

## Prerequisites
Before using this package, ensure the following prerequisites are met:
- Create a free Opsgenie account and obtain an API key to send alerts to your device.
- Create an account on birdeye.so and activate the BDS account on birdeye.so [here](https://bds.birdeye.so/).
- Generate a new API key on birdeye.so.

## Usage
Follow these steps to utilize this package:
1. Import the package into your code.
2. Run the main program.
3. Input the Opsgenie API key.
4. Input the API key from birdeye.so.

## Example
```python
from pricecheck import PriceChecker

# Initialize PriceChecker
price_checker = PriceChecker()

# Run main program
price_checker.run()

```

## License
This project is licensed under the [MIT License](LICENSE).
