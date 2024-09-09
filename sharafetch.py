import platform
import os
import subprocess
import sys

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

def get_kernel():
    return platform.release()

def get_uptime():
    return str(int(psutil.boot_time()))

def get_packages():
    core_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'core')
    user_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'userpacks')
    amogos_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'amogospacks')
    
    core_packages = len([f for f in os.listdir(core_dir) if f.endswith('.py')])
    user_packages = len([f for f in os.listdir(user_dir) if f.endswith('.py')])
    amogos_packages = len([f for f in os.listdir(amogos_dir) if f.endswith('.py')])
    
    return f"{core_packages + user_packages + amogos_packages} (core: {core_packages}, user: {user_packages}, amogos: {amogos_packages})"

def get_shell():
    return "SharaOS Shell"

def get_resolution():
    return f"{os.get_terminal_size().columns}x{os.get_terminal_size().lines}"

def run(sharaos, *args):
    logo = [
        "    ____  _                    ____  ____",
        "   / ___|| |__   __ _ _ __ __ / __ \\/ ___|",
        "   \\___ \\| '_ \\ / _` | '__/ _` \\/ _\\ \\___ \\",
        "    ___) | | | | (_| | | | (_| | (_) |__) |",
        "   |____/|_| |_|\\__,_|_|  \\__,_|\\____/____/"
    ]

    info = [
        f"OS: {get_os_name()}",
        f"Kernel: {get_kernel()}",
        f"Uptime: {get_uptime()} seconds",
        f"Packages: {get_packages()}",
        f"Shell: {get_shell()}",
        f"Resolution: {get_resolution()}"
    ]

    max_length = max(len(line) for line in logo + info)

    for i, line in enumerate(logo):
        if i < len(info):
            print(f"{line:<{max_length}}  {info[i]}")
        else:
            print(line)

    for line in info[len(logo):]:
        print(f"{'':<{max_length}}  {line}")
