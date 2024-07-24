# Simple-Temperature-Monitor-NVIDIA
Simple Python implementation of a Linux based temperature monitor script (build for NVIDIA GPU) that periodically fetches temps and their deltas compared to previous iterations.
You need to have installed the `lm-sensors` package and the `nvidia-smi` command line tool.
To install `lm-sensors`:
```bash
# For Ubuntu/Debian
sudo apt-get install lm-sensors
# For Arch Linux
sudo pacman -S lm_sensors
# For Fedora
sudo yum install lm_sensors
sudo dnf install lm_sensors
```
To install `nvidia-smi`:
```bash
# For Ubuntu/Debian
sudo apt-get install nvidia-smi
# For Arch Linux
sudo pacman -S nvidia-smi
# For Fedora
sudo yum install nvidia-smi
sudo dnf install nvidia-smi
```
To run the script you should install the `requirements.txt` preferably in a virtual environment:
```bash
pip install -r requirements.txt
```
Then you can run the script:
```bash
python3 main.py
```
