FROM nginx:1.15.5-alpine

ARG mode

ADD certs/$mode.crt /etc/nginx/
ADD certs/$mode.key /etc/nginx/
ADD certs/dhparam.pem /etc/nginx/
ADD conf/$mode.conf /etc/nginx/conf.d/default.conf
