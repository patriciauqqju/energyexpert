import os
import subprocess
import ctypes

class EnergyExpert:
    def __init__(self):
        self.guid = self.get_active_power_scheme()

    def get_active_power_scheme(self):
        """Retrieves the active power scheme GUID."""
        try:
            output = subprocess.check_output(['powercfg', '/getactivescheme'], shell=True)
            return output.decode().strip().split()[-1]
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving active power scheme: {e}")
            return None

    def set_power_scheme(self, scheme_name):
        """Sets a specific power scheme."""
        try:
            subprocess.run(['powercfg', '/setactive', scheme_name], check=True, shell=True)
            print(f"Power scheme set to {scheme_name}.")
        except subprocess.CalledProcessError as e:
            print(f"Error setting power scheme: {e}")

    def optimize_for_battery(self):
        """Optimize settings for battery life."""
        try:
            # Reduce display brightness
            subprocess.run(['powercfg', '/change', 'monitor-timeout-dc', '2'], check=True, shell=True)
            # Reduce sleep timeout
            subprocess.run(['powercfg', '/change', 'standby-timeout-dc', '10'], check=True, shell=True)
            # Disable Wi-Fi adapter when on battery
            subprocess.run(['powercfg', '/setdcvalueindex', self.guid, 'SUB_NONE', '00000000-0000-0000-0000-000000000000', '3'], check=True, shell=True)
            print("Optimized settings for better battery life.")
        except subprocess.CalledProcessError as e:
            print(f"Error optimizing settings: {e}")

    def customize_settings(self, monitor_timeout, standby_timeout):
        """Customize power settings."""
        try:
            subprocess.run(['powercfg', '/change', 'monitor-timeout-dc', str(monitor_timeout)], check=True, shell=True)
            subprocess.run(['powercfg', '/change', 'standby-timeout-dc', str(standby_timeout)], check=True, shell=True)
            print(f"Customized settings: Monitor timeout = {monitor_timeout}, Standby timeout = {standby_timeout}.")
        except subprocess.CalledProcessError as e:
            print(f"Error customizing settings: {e}")

    def require_admin(self):
        """Check if the script is run as an administrator."""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

if __name__ == "__main__":
    if not EnergyExpert().require_admin():
        print("This script requires administrative privileges.")
    else:
        expert = EnergyExpert()
        expert.optimize_for_battery()
        # Customize as desired
        # expert.customize_settings(monitor_timeout=5, standby_timeout=15)