# fix_installation.py
import subprocess
import sys

def reinstall_packages():
    """Reinstall pandas and numpy to fix compatibility issues"""
    packages = ['numpy', 'pandas']
    
    for package in packages:
        try:
            # Uninstall package
            subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', package])
            print(f"Uninstalled {package}")
            
            # Reinstall package
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"Reinstalled {package}")
            
        except Exception as e:
            print(f"Error with {package}: {e}")

if __name__ == "__main__":
    reinstall_packages()
    print("\nNow run your main program again.")
    