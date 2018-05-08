FROM nginx:alpine

ARG mode

ADD certs/* /etc/nginx/
ADD conf/$mode.conf /etc/nginx/conf.d/default.conf
