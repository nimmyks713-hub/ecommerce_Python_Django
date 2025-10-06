# 🛍️ Django E-Commerce Web Application

A fully functional **E-Commerce web application** built using **Python Django**, featuring user authentication, product listings, detailed product views, and a simple cart management system.  
This project demonstrates the core concepts of **web development, database integration, and backend logic** using Django and PostgreSQL.

---

## 🚀 Features

### 🧑‍💻 User Management
- User **Signup** and **Login** using Django’s built-in authentication system.  
- Secure password validation and user-friendly forms.  

### 🛒 Product Management
- Displays all available **products** in a clean, responsive layout.
- Each product includes:
  - Image  
  - Title  
  - Price  
  - Rating  
  - Description  
  - Offers and details  

### 📦 Shopping Cart
- Add products to the **cart** from the product detail page.  
- View all cart items in a dedicated cart page with a clean layout.  
- Option to **delete items** from the cart.  
- Data stored persistently in **PostgreSQL database**.

### 🏠 Home Page
- A simple and elegant home page introducing the store.  
- Links to categories, product listing, and login/signup pages.




---

## 🧩 Technologies Used

| Category | Technology |
|-----------|-------------|
| Backend Framework | Django (Python) |
| Frontend | HTML, CSS, Bootstrap |
| Database | PostgreSQL |
| Template Engine | Django Templates |
| Authentication | Django Auth System |
| Version Control | Git & GitHub |

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ecommerce-django.git
   cd ecommerce-django
2. **Create and activate virtual environment**
```bash
    python -m venv env
    source env/bin/activate        # On macOS/Linux
    env\Scripts\activate           # On Windows

```

3. **Install dependencies**
```bash
   pip install -r requirements.txt

```
4. **Database setup**

Configure your PostgreSQL credentials in settings.py

Then run:
```bash
   python manage.py makemigrations
   python manage.py migrate
```

5. **Create superuser**
```bash
   python manage.py createsuperuser
```

6. **Run the server**
```bash
   python manage.py runserver

```
7. **Open your browser and visit:**

   http://127.0.0.1:8000/
