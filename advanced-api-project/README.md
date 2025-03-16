# Advanced API Project

## API Endpoints

### Books
- `GET /api/books/` - List all books (Public)
- `GET /api/books/<int:pk>/` - Retrieve book details (Public)
- `POST /api/books/create/` - Create a new book (🔒 Auth Required)
- `PUT /api/books/<int:pk>/update/` - Update a book (🔒 Auth Required)
- `DELETE /api/books/<int:pk>/delete/` - Delete a book (🔒 Auth Required)

## Authentication
To access protected endpoints, include a **Token** in the request:



---

### **✅ Final Deliverables**
1. **Updated `views.py`**: Implements generic views.
2. **Updated `urls.py`**: Maps API endpoints.
3. **Updated `serializers.py`**: Validates data.
4. **Permissions applied**: Auth required for modifying endpoints.
5. **Tested with Postman/cURL**: Works correctly.
6. **Added `README.md`**: Documents API usage.

---

### **🎯 Next Steps**
Now that your API supports CRUD operations with authentication, you can:
- **Enhance filtering** (e.g., search books by title).
- **Add pagination** for large datasets.
- **Implement API versioning** for future upgrades.

Let me know if you need help with the next steps! 🚀
