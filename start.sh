# !/bin/bash
source "$HOME/tweet-from-message/env/bin/activate"
echo Starting Bot...
python main.py > $HOME/tweet-from-message/run_logs.txt &
sleep 3
echo Bot started.