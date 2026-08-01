# Book Catalog API

REST API for managing books, built with Django and Django REST Framework.

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Go to http://localhost:8000/api/books/

## Endpoints

- `GET /api/books/` - list all books
- `POST /api/books/` - create a book
- `GET /api/books/<id>/` - get single book
- `PUT /api/books/<id>/` - update a book
- `DELETE /api/books/<id>/` - delete a book

## Example request

```bash
curl -X POST http://localhost:8000/api/books/ -H "Content-Type: application/json" -d '{"title": "Django for Beginners", "author": "William Vincent", "isbn": "9781735467221", "published_date": "2022-01-01"}'
```

## Tests

```bash
python manage.py test books
```

## Docker

```bash
docker-compose up --build
```

## CI/CD

GitHub Actions pipeline in `.github/workflows/ci-cd.yml`:
1. Runs tests on push
2. Builds Docker image and pushes to GHCR
3. Deploys to Kubernetes with Helm

## Helm deployment

```bash
helm install book-catalog ./helm/book-catalog
kubectl get pods
```

## Tech used

- Python 3.12
- Django 5.1
- Django REST Framework
- Docker
- GitHub Actions
- Kubernetes + Helm
