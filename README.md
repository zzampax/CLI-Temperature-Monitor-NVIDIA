# Simple-Temperature-Monitor-NVIDIA-
Simple Python implementation of a Linux based temperature monitor script (build for NVIDIA GPU) that periodically fetches temps and their deltas compared to previous iterations.
You need to have installed the `lm-sensors` package and the `nvidia-smi` command line tool.
To install `lm-sensors`:
```bash
sudo apt-get install lm-sensors
```
```bash
sudo pacman -S lm_sensors
```
```bash
sudo yum install lm_sensors
```
```bash
sudo dnf install lm_sensors
```
To install `nvidia-smi`:
```bash
sudo apt-get install nvidia-smi
```
```bash
sudo pacman -S nvidia-smi
```
```bash
sudo yum install nvidia-smi
```
```bash
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
