FROM nginx

RUN apt-get update && apt-get install \
    bash curl wget nano openssh-server -y

RUN /etc/init.d/ssh start && /etc/init.d/ssh status
