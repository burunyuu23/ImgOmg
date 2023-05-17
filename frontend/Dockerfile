# Используем базовый образ с Node.js
FROM node:latest

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем остальные файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN npm install

CMD ["npm", "run", "dev", "--", "--port", "5173"]

# docker run -p 5173:5173 --name kputoi_frontend -d kputoi_frontend
