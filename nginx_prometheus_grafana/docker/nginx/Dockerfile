FROM nginx:latest

COPY default.conf /etc/nginx/conf.d/default.conf
COPY index.nginx-debian.html /usr/share/nginx/html/index.html

# NETWORK
EXPOSE 65000

# start app
CMD ["nginx", "-g", "daemon off;"]
