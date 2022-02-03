# Multi-stage
# 1) Node image for building frontend assets
# 2) nginx stage to serve frontend assets

# Node stage named "builder"
FROM node:lts-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Nginx stage named "production"
FROM nginx:stable-alpine AS production
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx/default.conf /etc/nginx/conf.d/
COPY nginx/nginx.conf /etc/nginx/
COPY nginx/mime.types /etc/nginx/
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
