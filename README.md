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
sudo apt-get install nvidia-utils
# For Arch Linux
sudo pacman -S nvidia-utils
# For Fedora
sudo yum install nvidia-utils
sudo dnf install nvidia-utils
```
Since the script has a Shebang, you can run it like this:
```bash
./temps
```