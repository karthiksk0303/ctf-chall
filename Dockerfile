FROM node:18

# Install PHP for the secondary internal service
RUN apt-get update && apt-get install -y php-cli

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .

# Expose the Node.js port
EXPOSE 10000

# Start PHP internal server on 8080 and Node.js on 10000
CMD (php -S localhost:8080 internal.php &) && npm start
