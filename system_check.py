#!/usr/bin/env python3
#
####################################################################
#
# Filename: system_check.py
# Author: Shawn Patterson
# Description: System agnostic script to get basic system info
# Usage: ./system_check.py (Linux) or py system_check.py (Windows)
#
####################################################################

# Import modules
import platform
import getpass
import psutil  # Important, might need to install psutil module on target systems


# Variables
get_os = platform.system()
ram_pct = psutil.virtual_memory()[2]

# Show current user & output header
print()
print("Hello " + getpass.getuser(), ", current system information:")
print("----------------------------------------------")
print()

# Get system platform (Windows, Linux, UNIX, etc,)
if get_os == "Windows":
    print("System Platform:", platform.system(), platform.version(), platform.machine())
if get_os == "Linux":
    print("System Platform:", platform.system(), platform.release(), platform.machine())
print()

# Get system hostname/computer name
print("System hostname:", platform.node())
print()

# Get CPU usage information
print("Gathering system CPU usage over 5 second interval, please wait...")
print()
cpu_pct = psutil.cpu_percent(5)
if cpu_pct > 90:
    print("System CPU usage is above 90% threshold:", str(cpu_pct) + "%")
if cpu_pct < 90:
    print("System CPU usage is below 90% threshold:", str(cpu_pct) + "%")
print()

# Get RAM usage information
if ram_pct > 85:
    print("System RAM usage is above 85% threshold:", str(ram_pct) + "%")
if ram_pct < 85:
    print("System RAM usage is below 85% threshold:", str(ram_pct) + "%")
print()

# Get filesystem information
if get_os == "Windows":
    windows_disk_pct = psutil.disk_usage("C:/")[3]
    if windows_disk_pct > 85:
        print("System filesystem usage for C is above 90% threshold:", str(windows_disk_pct) + "%")
    if windows_disk_pct < 85:
        print("System filesystem usage for C is below 90% threshold:", str(windows_disk_pct) + "%")
if get_os == "Linux":
    linux_disk_pct = psutil.disk_usage("/")[3]
    if linux_disk_pct > 85:
        print("System filesystem usage for / is above 85% threshold:", str(linux_disk_pct) + "%")
    if linux_disk_pct < 85:
        print("System filesystem usage for / is below 85% threshold:", str(linux_disk_pct) + "%")
print()

# Get list of running processes, Linux sorted by top CPU and top MEM usage
if get_os == "Windows":
    print("System processes:" '\n')
    for proc in psutil.process_iter():
        try:
            proc_name = proc.name()
            proc_pid = proc.pid
            proc_mem = proc.memory_percent()
            print("PID:", proc_pid, "::", "Name:", proc_name, "::", "MEM Usage:", str(proc_mem)[:4] + "%")
        except psutil.NoSuchProcess:
            pass

if get_os == "Linux":
    list_cpu = subprocess.Popen(
        ["ps aux --sort -%cpu | head -15"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )
    list_cpu_output, list_cpu_error = list_cpu.communicate()
    print("System processes sorted by top 15 CPU usage:" + '\n' + '\n' + list_cpu_output + list_cpu_error)
    print()

    list_mem = subprocess.Popen(
        ["ps aux --sort -%mem | head -15"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True
    )
    list_mem_output, list_mem_error = list_mem.communicate()
    print("System processes sorted by top 15 MEM usage:" + '\n' + '\n' + list_mem_output + list_mem_error)
    print()

