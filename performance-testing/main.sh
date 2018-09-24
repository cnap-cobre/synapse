echo "Please enter an active sessionid:  "
read sessionid

time ./login-page-serving-time.sh
time ./application-serving-time.sh $sessionid
time ./profile-serving-time.sh $sessionid
