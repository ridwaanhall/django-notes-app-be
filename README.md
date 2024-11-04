# Django REST Framework HATEOAS Implementation

A robust REST API implementation using Django REST Framework (DRF) with HATEOAS (Hypertext as the Engine of Application State) principles, enabling self-discoverable and navigable APIs.

## 🌟 Features

- Full HATEOAS implementation following REST maturity level 3
- Token-based authentication
- Pagination with navigable links
- Nested resource serialization
- Hypermedia controls

## 🔧 Technology Stack

- Python 3.10+
- Django 4.2+
- Django REST Framework 3.15+
- PostgreSQL 14+

## 📋 Prerequisites

Ensure you have the following installed:
- Python 3.10 or higher
- pip (Python package manager)
- Pipenv
- PostgreSQL

## 🚀 Quick Start

1. Clone the repository
```bash
git clone https://github.com/arasopraza/django-notes-app-be.git
```

2. Create and activate virtual environment
```bash
python -m venv venv
or
pipenv shell
```

3. Install dependencies
```bash
pipenv install
```

4. Run migrations
```bash
python manage.py migrate
```

6. Start development server
```bash
python manage.py runserver
```

## 💡 HATEOAS Implementation

Our API follows HATEOAS principles by including hypermedia links in responses:

```json
{
  "notes": [
    {
      "id": "6b7ee782-6ca4-4cc7-bd9e-d8b9467dae56",
      "title": "Catatan A",
      "body": "Isi dari catatan A",
      "tags": [
        "Android",
        "Web"
      ],
      "createdAt": "2024-09-27T07:12:40.591696Z",
      "updatedAt": "2024-09-27T07:12:40.591734Z",
      "_links": [
        {
          "rel": "self",
          "href": "http://127.0.0.1:8000/notes/6b7ee782-6ca4-4cc7-bd9e-d8b9467dae56/",
          "action": "GET",
          "types": [
            "application/json"
          ]
        },
        {
          "rel": "self",
          "href": "http://127.0.0.1:8000/notes/6b7ee782-6ca4-4cc7-bd9e-d8b9467dae56/",
          "action": "PUT",
          "types": [
            "application/json"
          ]
        },
        {
          "rel": "self",
          "href": "http://127.0.0.1:8000/notes/6b7ee782-6ca4-4cc7-bd9e-d8b9467dae56/",
          "action": "DELETE",
          "types": [
            "application/json"
          ]
        }
      ]
    }
  ]
}
```

### Key HATEOAS Features

1. **Resource Links**: Each resource includes related links
2. **Action Discovery**: Available actions are included in responses
3. **State Transitions**: Next possible states are provided
4. **Self-Documentation**: API is navigable through hypermedia

### Creating New Resources

1. Define model in `models.py`
2. Create serializer in `serializers.py`
3. Implement ViewSet in `views.py`
4. Add URLs in `urls.py`
5. Include HATEOAS links

Example resource implementation:

```python
# serializers.py
class ProductSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    def get__links(self, obj):
        request = self.context['request']
        return {
            'self': request.build_absolute_uri(
                reverse('product-detail', args=[obj.pk])
            ),
            'category': request.build_absolute_uri(
                reverse('category-detail', args=[obj.category.pk])
            )
        }
```


## 🔒 Security Features

- CORS configuration
- Input validation
- XSS protection

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 👥 Authors

- Arsy Opraza Akma - - [YourGithub](https://github.com/arasopraza)

## 🙏 Acknowledgments

- Django documentation
- Django REST Framework team
- HATEOAS principles and REST architecture guidelines
