# EnergyExpert

EnergyExpert is a Python program designed to customize and optimize energy settings for extending battery life on Windows laptops and tablets. It provides functionality to adjust power schemes, optimize settings for battery efficiency, and customize power management parameters.

## Features

- **Retrieve Active Power Scheme:** Get the current active power scheme GUID.
- **Set Power Scheme:** Switch to a specified power scheme.
- **Optimize for Battery:** Apply settings that enhance battery life:
  - Reduce display brightness timeout.
  - Reduce system standby timeout.
  - Disable Wi-Fi adapter when on battery.
- **Customize Settings:** Adjust specific power management parameters like monitor and standby timeout.

## Prerequisites

- Windows operating system.
- Python 3.x installed.
- Administrative privileges to run power management commands.

## Usage

1. Clone the repository or download the `energy_expert.py` file.
2. Open a terminal with administrative privileges.
3. Navigate to the directory containing `energy_expert.py`.
4. Run the script:

   ```bash
   python energy_expert.py
   ```

5. Customize settings by uncommenting and modifying the `customize_settings` method call if needed.

## Note

- This script requires administrative privileges to execute system power management commands effectively.
- Use the script at your own risk. Ensure you understand the changes being made to your power settings.

## License

This project is licensed under the MIT License.

## Author

Developed by [Your Name].