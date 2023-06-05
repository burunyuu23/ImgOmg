FROM node:latest

WORKDIR /app

COPY . .

RUN npm install

EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

# docker run -p 5173:5173 --name kputoi_frontend -d kputoi_frontend
