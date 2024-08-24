import subprocess
import json

def get_system_info():
    # Run the lscpu command and get the output
    lscpu_output = subprocess.run(['lscpu'], capture_output=True, text=True)
    lscpu_data = {}
    
    # Parse the lscpu output into a dictionary
    for line in lscpu_output.stdout.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            lscpu_data[key.strip()] = value.strip()
    
    # Run the lsblk command and get the output in JSON format
    lsblk_output = subprocess.run(['lsblk', '-J'], capture_output=True, text=True)
    lsblk_data = json.loads(lsblk_output.stdout)
    
    # Combine both results in a single dictionary
    system_info = {
        "lscpu": lscpu_data,
        "lsblk": lsblk_data
    }
    
    return json.dumps(system_info, indent=4)

# Example usage:
if __name__ == '__main__':
    print(get_system_info())
