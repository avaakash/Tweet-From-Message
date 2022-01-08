# !/bin/bash
echo $HOME
source "$HOME/tweet-from-message/env/bin/activate"
echo Starting Bot...
python main.py > run_logs.txt &
sleep 3
echo Bot started.