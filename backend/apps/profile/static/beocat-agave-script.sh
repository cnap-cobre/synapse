#!/bin/bash -l

ssh-keygen -f ~/.ssh/synapse_agave -t rsa -N ''
cat ~/.ssh/synapse_agave.pub >> ~/.ssh/authorized_keys

PRIVATE_KEY=`cat ~/.ssh/synapse_agave | awk '$1=$1' ORS='!!!'`
PUBLIC_KEY=`cat ~/.ssh/synapse_agave.pub | awk '$1=$1' ORS='!!!'`

printf "\n\n\nCopy and paste the following into the text box in your browser:\n\n\n"

printf "\n\n\n{\"id\": \"beocat-`whoami`\",\"name\": \"Beocat\",\"status\": \"UP\",\"type\": \"STORAGE\",\"description\": \"Beocat supercomputer at K-State\",\"site\": \"beocat.ksu.edu\",\"storage\": {  \"host\": \"beocat.ksu.edu\",  \"port\": 22,  \"protocol\": \"SFTP\",  \"auth\": {      \"username\": \"`whoami`\",      \"publicKey\": \"${PUBLIC_KEY}\",      \"privateKey\": \"${PRIVATE_KEY}\",      \"type\": \"SSHKEYS\"   }  }}\n\n\n"