FROM nginx:1.19.0-alpine
RUN mkdir /app
RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled
WORKDIR /app
