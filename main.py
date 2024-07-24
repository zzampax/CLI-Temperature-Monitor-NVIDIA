import subprocess
import time
import sys
import json
import xml.etree.ElementTree as ET
import colorama

def handle_temps(temps):
    output = {}
    # Get the CPU temperature
    cpu_temp = temps["coretemp-isa-0000"]["Package id 0"]["temp1_input"]
    # Get the ACPI temperature
    acpi_temp = temps["acpitz-acpi-0"]["temp1"]["temp1_input"]
    output["CPU\t(°C)"] = cpu_temp
    output["ACPI\t(°C)"] = acpi_temp
    for core in temps["coretemp-isa-0000"]:
        if "Core" not in core: continue
        index = int(core.split(" ")[1])
        output[f"CORE#{index}\t(°C)"] = temps["coretemp-isa-0000"][core][f"temp{index + 2}_input"]
    return output

def handle_nvidia(nvidia):
    # gpu subelement --> temperature subelement
    gpu_temp = nvidia.find("gpu").find("temperature").find("gpu_temp").text
    return {"GPU\t(°C)": float(gpu_temp.split(" ")[0])}

def get_temps():
    # Get the temperatures from the sensors as JSON
    temps = subprocess.check_output(["sensors", "-j"])
    # Get the nvidia-smi output as XML
    nvidia = subprocess.check_output(["nvidia-smi", "-q", "-x"])
    # Parse the JSON and XML
    temps = json.loads(temps)
    nvidia = ET.fromstring(nvidia)
    # concatenate the two dictionaries
    return handle_temps(temps) | handle_nvidia(nvidia)

if __name__ == "__main__":
    # Interval has to be int and greater than 0, passed via 'python3 temps.py -s <interval>'
    interval = sys.argv[sys.argv.index("-s") + 1] if "-s" in sys.argv else 1
    prev = {}
    try:
        while True:
            # Clear the screen
            print("\033c", end="")
            # Get the temperatures and print them
            json_output, output, separator = get_temps(), "", f"{colorama.Fore.BLUE}>>>{colorama.Fore.RESET}"
            for key, value in json_output.items():
                if key not in prev: prev[key] = value
                # Calculate the difference between the current and previous temperature
                delta = float(value) - float(prev.get(key, 0))
                # Color the delta based on the sign and stringify it
                delta = f"{colorama.Fore.RED}+{delta}{colorama.Fore.RESET}" if delta > 0 else f"{colorama.Fore.GREEN}{delta}{colorama.Fore.RESET}" if delta < 0 else f"+{delta}{colorama.Fore.RESET}"
                output += f"{key}\t{separator}\t{value} ({delta}°C {interval}s delta)\n"
            print(f"Fetching Temperatures every {interval}s ({time.ctime()})")
            print("Press Ctrl+C to exit")
            print(output)
            prev = json_output
            time.sleep(int(interval))
    except KeyboardInterrupt:
        print("\nExiting...")
