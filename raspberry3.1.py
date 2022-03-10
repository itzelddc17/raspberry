import re
import subprocess

host = 'jetbrains.com'
ping_output = subprocess.check_output(['ping','-c 5', host])

for line in ping_output.splitlines():
    print (line)