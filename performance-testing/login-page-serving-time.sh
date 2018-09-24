echo "Starting login page test."
echo "Hitting https://synapse.ksu.edu/accounts/login/"
echo "1000 times with 100 concurrent connections."
seq 1 1000 | xargs -n1 -P100 bash -c "curl --write-out "+" --silent --output /dev/null -s https://synapse.ksu.edu/accounts/login/"
