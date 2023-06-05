FROM alpine:latest

RUN apk --update add nginx && \
	ln -sf /dev/stdout /var/log/nginx/access.log && \
	ln -sf /dev/stderr /var/log/nginx/error.log && \
	mkdir /etc/nginx/sites-enabled/ && \
	mkdir -p /run/nginx && \
	rm -fr /etc/nginx/conf.d/* &&\
    rm -rf /etc/nginx/nginx.conf &&\
	rm -rf /var/cache/apk/* &&\
	mkdir /app

COPY ./nginx.conf ./etc/nginx/conf.d/default.conf
COPY ./nginx.conf ./etc/nginx/nginx.conf

# EXPOSE 80 443
EXPOSE 80 433

CMD ["nginx", "-g", "daemon off;"]