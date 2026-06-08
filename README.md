# Sector Intelligence Analytics API

A high-performance FastAPI backend service for strategic sector intelligence and market insights. Built with modern async/await patterns, featuring MongoDB integration, comprehensive data validation, and RESTful API endpoints for intelligence data management and visualization.

## 🚀 Features

- **Async FastAPI Framework** - Built on FastAPI with async/await support for high throughput
- **MongoDB Integration** - Native async MongoDB connectivity with PyMongo
- **Pydantic Validation** - Strong type validation with automatic data coercion
- **RESTful API** - Clean, documented API endpoints with OpenAPI/Swagger support
- **Intelligent Data Models** - Sector model with built-in validators for:
  - DateTime parsing from multiple formats
  - Integer type coercion
  - String normalization
  - ObjectId to string conversion
- **Hot Reload Development** - Automatic reloading on file changes
- **Production Ready** - Proper error handling and lifespan management

## 📋 Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | FastAPI 0.104+ |
| Server | Uvicorn ASGI |
| Database | MongoDB with PyMongo (async) |
| Validation | Pydantic v2 |
| Python | 3.10+ |

## 🔧 Installation

### Prerequisites
- Python 3.10 or higher
- MongoDB 4.4+
- pip or conda

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd backend
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your MongoDB connection string and database name
```

5. **Start the server**
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## 📚 API Documentation

### Interactive API Docs
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Endpoints

#### Get Sector Data
```http
GET /insights/
```
Returns a list of all sectors sorted by newest first (limit 100).

**Response:**
```json
[
  {
    "id": "6a26d3d7e66bc49cf89ec5a2",
    "sector": "Energy",
    "topic": "gas",
    "region": "Northern America",
    "country": "United States of America",
    "title": "U.S. natural gas consumption is expected to increase...",
    "intensity": 6,
    "relevance": 2,
    "likelihood": 3,
    "source": "EIA",
    "published": "2017-01-09T00:00:00"
  }
]
```

#### Save New Sector
```http
POST /insights/
Content-Type: application/json

{
  "sector": "Energy",
  "topic": "renewable",
  "insight": "Solar energy growth",
  "region": "Europe",
  "country": "Germany",
  "intensity": 8,
  "relevance": 3,
  "likelihood": 4,
  "source": "Bloomberg",
  "title": "Solar adoption increases in Europe"
}
```

**Response:** Returns the created sector with generated `id`.

## 🏗️ Project Structure

```
backend/
├── main.py                 # FastAPI app initialization & lifespan
├── config.py               # Configuration management
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── model/
│   ├── __init__.py
│   └── sector.py          # Sector model with validators
└── Routers/
    ├── __init__.py
    └── insights.py        # Insights API routes
```

## 📦 Dependencies

- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **pymongo** - MongoDB async driver
- **pydantic** - Data validation
- **python-dateutil** - DateTime parsing utilities

## 🔐 Environment Variables

Create a `.env` file with:

```env
MONGODB_URL=mongodb://localhost:27017/
DATABASE_NAME=insights_db
```

## 💡 Model Features

The `Sector` model includes intelligent validators:

- **DateTime Fields** (`start_year`, `end_year`, `added`, `published`)
  - Accepts ISO strings, timestamps, or empty strings
  - Gracefully handles parsing errors
  
- **Integer Fields** (`intensity`, `relevance`, `likelihood`)
  - Coerces strings to integers
  - Handles empty/null values
  
- **String Fields** (`title`, `insight`, `source`, `impact`)
  - Normalizes input to string format
  - Handles empty values

## 🚀 Performance Optimizations

- ✅ Async/await throughout for non-blocking I/O
- ✅ MongoDB connection pooling via lifespan management
- ✅ Efficient cursor sorting before data retrieval
- ✅ Request-scoped database access

## 📖 Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black .
```

### Linting
```bash
pylint Routers/ model/
```

## 🐛 Troubleshooting

**MongoDB Connection Error**
- Ensure MongoDB is running
- Check `MONGODB_URL` in `.env`
- Verify network connectivity

**Port Already in Use**
```bash
uvicorn main:app --reload --port 8001
```

**Validation Errors**
- Check request payload matches schema (see `/docs`)
- Ensure date formats are ISO 8601 compliant

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Built with ❤️ for intelligent data visualization.

---

**Status**: ✅ Production Ready | **Version**: 1.0.0