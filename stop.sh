# !/bin/bash
kill -9 $(ps aux | grep "[p]ython main.py" | awk '{print $2}')