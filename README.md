# Тестовое задание: Парсер Kaspi магазина  

## 📌 Описание проекта  
Программа парсит страницы товаров магазина Kaspi.  
Собирает следующие данные:  
- Название товара  
- Цена  
- Рейтинг  
- Изображения  
- Список продавцов с ценой и условиями доставки  

Сохраняет данные в:  
- JSON (`app/export/product.json`)  
- Опционально можно подключить PostgreSQL  

Дополнительно:  
- Вычисляет минимальную и максимальную цену среди продавцов  

## 🚀 Установка и запуск  

### 1. Клонирование репозитория  
```bash
git clone https://github.com/yyyeleshnur/kaspi-parser.git
```
cd kaspi-parser
2. Установка зависимостей
```bash
pip install -r requirements.txt
```
3. Настройка окружения
Создайте файл .env (если планируете использовать PostgreSQL) и укажите:
```bash
DB_HOST=localhost
DB_PORT=5432
DB_NAME=kaspi
DB_USER=postgres
DB_PASSWORD=postgres
```
4. Запуск парсера
```bash
python parser.py
```
Данные сохраняются в app/export/product.json.

📂 Структура проекта
```bash
kaspi-parser/
│── parser.py
│── seed.json
│── app/
│    ├── export/
│    │    └── product.json
│    ├── main.py
│    ├── database.py
│    ├── models.py
│    ├── schemas.py
│── Dockerfile
│── requirements.txt
│── README.md
```
Пример таблиц:
```bash
products

id

name

min_price

max_price

rating

offers

id

product_id

seller

price

delivery
```
🔄 Обновления данных
В текущей версии обновление выполняется вручную через запуск парсера

Поля, которые обновляются: цена, список продавцов, доставка

✅ Что сделано
 Парсинг товара

 Сохранение в JSON

 Сохранение в PostgreSQL

 Docker

📄 Дополнительно
Больше всего времени ушло на корректный парсинг таблицы продавцов

Можно улучшить: автоматическое обновление данных, Docker контейнеризация
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/31494ca5-a1ee-4078-b2a1-c075a9f1eb8c" />
