# Image Gallery Project (Django + DRF + Cloudinary + PostgreSQL)

## Описание
Проект предоставляет REST API для управления изображениями с хранением в Cloudinary и базой данных PostgreSQL.

### Технологии
- Python 3.11+
- Django 5.2+
- Django REST Framework 3.14+
- Cloudinary
- PostgreSQL
- python-decouple для работы с .env
- Pillow для работы с изображениями

## Установка

1. Клонируем репозиторий и создаем виртуальное окружение:

```bash
git clone <репозиторий>
cd image_gallery_project
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

2. Устанавливаем зависимости:

```bash
pip install -r req.txt
```

3. Создаем файл `.env` в корне проекта и заполняем:

```env
# Django
SECRET_KEY=ваш_секретный_ключ
DEBUG=True

# PostgreSQL
DB_NAME=image_gallery_db
DB_USER=gallery_user
DB_PASSWORD=securepassword
DB_HOST=localhost
DB_PORT=5432

# Cloudinary
CLOUDINARY_CLOUD_NAME=mycloudname
CLOUDINARY_API_KEY=123456789012345
CLOUDINARY_API_SECRET=abcDEFghiJKLmnopQRSTuv
```

4. Применяем миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Создаем суперпользователя для доступа к Admin:

```bash
python manage.py createsuperuser
```

6. Запускаем сервер разработки:

```bash
python manage.py runserver
```

## Endpoints API

### 1. Получение списка изображений
**GET** `/api/images/`

Возвращает список всех изображений:

```json
[
  {
    "id": 1,
    "title": "Мое фото",
    "description": "Тестовое изображение",
    "image_url": "https://res.cloudinary.com/...",
    "cloudinary_public_id": "...",
    "uploaded_at": "2025-10-23T11:00:00Z"
  }
]
```

### 2. Получение изображения по ID
**GET** `/api/images/<id>/`

Возвращает JSON с информацией о конкретном изображении.

### 3. Загрузка изображения
**POST** `/api/images/`

- Тип контента: `multipart/form-data`
- Поля формы:
  - `title` (string) — заголовок
  - `description` (string) — описание
  - `image_file` (file) — файл изображения

**Пример с curl:**

```bash
curl -X POST http://127.0.0.1:8000/api/images/ \
  -F "title=Мое фото" \
  -F "description=Тестовое изображение" \
  -F "image_file=@C:\Users\User\Desktop\test.jpg"
```

Возвращает JSON с информацией о загруженном изображении.

### 4. Обновление изображения
**PUT** `/api/images/<id>/`

- Поля JSON: `title`, `description`
- Файл `image_file` через PUT не поддерживается (только через POST / Admin)

### 5. Удаление изображения
**DELETE** `/api/images/<id>/`

- Удаляет объект из базы, но файл в Cloudinary останется (для удаления файла нужно добавить `cloudinary.uploader.destroy(public_id)` в ViewSet).

## Django Admin

- URL: `/admin/`
- Можно добавить изображение через кастомную форму с полем `image_file`. Файл будет загружен в Cloudinary и автоматически сохранится `image_url` и `cloudinary_public_id`.

## Notes

- В `.env` храните все ключи и пароли.
- Для тестирования загрузки файлов через API рекомендуется использовать **Postman** или **curl** (Thunder Client бесплатная версия не поддерживает загрузку файлов).
- В качестве СУБД используется PostgreSQL, убедитесь, что база и пользователь созданы.

