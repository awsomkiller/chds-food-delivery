# Stage 1: Build the Vue.js app
FROM node:18-alpine as build

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:stable-alpine

# Remove default Nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy built files from Stage 1
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom Nginx config
COPY deployment/nginx/frontend.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
