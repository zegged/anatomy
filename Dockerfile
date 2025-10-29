FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    git \
    curl ca-certificates gnupg \
    wget unzip && \
    install -d /etc/apt/keyrings && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" > /etc/apt/sources.list.d/nodesource.list && \
    apt-get update && apt-get install -y nodejs && \
    npm i -g http-server@14 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*