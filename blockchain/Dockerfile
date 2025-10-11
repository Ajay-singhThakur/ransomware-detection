FROM node:18-alpine

# ADD THIS LINE to install the netcat utility for health checks
RUN apk add --no-cache netcat-openbsd

WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the Hardhat network port
EXPOSE 8545

# Command to run the Hardhat node and the deploy script
CMD ["npx", "hardhat", "node"]