FROM nginx:alpine

ARG mode

ADD certs/$mode.crt /etc/nginx/
ADD certs/$mode.key /etc/nginx/
ADD conf/$mode.conf /etc/nginx/conf.d/default.conf
