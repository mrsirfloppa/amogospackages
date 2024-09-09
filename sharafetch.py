import platform
import os
import subprocess
import sys
import time
from packages.core import update
from packages.core import amogos

def ensure_psutil():
    try:
        import psutil
    except ImportError:
        print("Installing required package: psutil")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
        import psutil
    return psutil

psutil = ensure_psutil()

def get_os_name():
    return "SharaOS"

def get_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime_seconds = int(current_time - boot_time)
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

def get_installed_packages():
    core_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'core')
    user_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'userpacks')
    amogos_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'amogospacks')
    
    core_packages = len([f for f in os.listdir(core_dir) if f.endswith('.py')])
    user_packages = len([f for f in os.listdir(user_dir) if f.endswith('.py')])
    amogos_packages = len([f for f in os.listdir(amogos_dir) if f.endswith('.py')])
    
    total_installed = core_packages + user_packages + amogos_packages
    return total_installed, core_packages, user_packages, amogos_packages

def get_available_packages():
    return len(amogos.list_all_available_packages())

def get_shell():
    return "SharaOS Shell"

def get_cpu_info():
    return f"{psutil.cpu_count(logical=False)} cores, {psutil.cpu_count()} threads"

def get_memory_info():
    mem = psutil.virtual_memory()
    return f"{mem.used // (1024 * 1024)}MB / {mem.total // (1024 * 1024)}MB"

def run(sharaos, *args):
    logo = [
        "    ____  _                    ____  ____",
        "   / ___|| |__   __ _ _ __ __ / __ \\/ ___|",
        "   \\___ \\| '_ \\ / _` | '__/ _` \\/ _\\ \\___ \\",
        "    ___) | | | | (_| | | | (_| | (_) |__) |",
        "   |____/|_| |_|\\__,_|_|  \\__,_|\\____/____/"
    ]

    total_installed, core, user, amogos_installed = get_installed_packages()
    available_packages = get_available_packages()

    info = [
        f"OS: {get_os_name()}",
        f"Uptime: {get_uptime()}",
        f"CPU: {get_cpu_info()}",
        f"Memory: {get_memory_info()}",
        f"Installed Packages: {total_installed}",
        f"  Core: {core}",
        f"  User: {user}",
        f"  Amogos: {amogos_installed}",
        f"Available Packages: {available_packages}",
        f"Shell: {get_shell()}"
    ]

    max_length = max(len(line) for line in logo + info)

    for i, line in enumerate(logo):
        if i < len(info):
            print(f"{line:<{max_length}}  {info[i]}")
        else:
            print(line)

    for line in info[len(logo):]:
        print(f"{'':<{max_length}}  {line}")
