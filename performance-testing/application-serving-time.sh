echo "Application serving test"
echo "Hitting https://synapse.ksu.edu/files/systems"
echo "1000 times with 100 concurrent connections."
seq 1 1000 | xargs -n1 -P100 bash -c "curl --cookie sessionid=$1 https://synapse.ksu.edu/files/systems --write-out '+' --silent --output /dev/null"
