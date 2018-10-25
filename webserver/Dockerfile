FROM nginx:1.15.5-alpine

ARG mode

ADD certs/* /etc/nginx/
ADD conf/$mode.conf /etc/nginx/conf.d/default.conf
