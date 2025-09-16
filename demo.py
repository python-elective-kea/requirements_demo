import os
import subprocess
import requests



subprocess.run(['git', 'pull', 'origin', 'main'])
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'amalie sagde det rigtige!'])
subprocess.run(['git', 'push', 'origin ', 'main'])



