import subprocess
from shlex import split

cmd = "git reset --hard ADDED_SD"
cmd_parts = split(cmd)
subprocess.run(cmd_parts)

cmd = "rm -rf dsd_logs/"
cmd_parts = split(cmd)
subprocess.run(cmd_parts)
