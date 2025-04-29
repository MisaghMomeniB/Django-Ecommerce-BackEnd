# 🛍️ Django E-commerce Backend

A fully functional E-commerce backend built with **Django**, complete with user authentication, product management, shopping cart, and order checkout — plus a clean, responsive HTML/CSS frontend.

---

## 🔧 Features

### 🧑‍💼 User System
- User registration and login via HTML forms
- Django's built-in `User` model (customizable)
- Login/logout using Django session auth
- JWT authentication also supported via DRF SimpleJWT (for future API integration)

### 🛒 Cart System
- Add products to cart
- Update quantity
- Remove products
- One cart per user (auto-created)
- Fully persistent via database

### 📦 Order & Checkout
- Convert cart to order
- Create order items from cart items
- View order history
- Mark orders as paid (mock payment API included)

### 🛠️ Admin Panel
- Full Django admin customization
- Manage products, categories, orders
- Inline order items view
- Change order status to paid manually

### 🎨 Frontend
- Built-in UI using Django templates
- Pure HTML + CSS (RTL support for Persian layout)
- Minimal and clean design
- Responsive and usable out-of-the-box

---

## 🚀 Technologies

| Stack       | Tool              |
|-------------|-------------------|
| Backend     | Django 4.x        |
| Auth        | Django Auth, JWT  |
| Templates   | Django Templating |
| Database    | SQLite3 (default) |
| Styling     | HTML5, CSS3       |

---

## 📂 Project Structure

```
ecommerce_backend/
├── config/               # Django project config
├── shop/                 # Product, cart, order logic
├── accounts/             # Auth views and registration
├── templates/            # HTML files
├── static/               # CSS and assets
├── media/                # Uploaded product images
└── manage.py
```

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/django-ecommerce-backend.git
cd django-ecommerce-backend
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

> ✅ Admin login: go to `/admin/` and create superuser:
```bash
python manage.py createsuperuser
```

---

## 🔐 Authentication

### Form-based Login:
- `/login/` and `/register/`

### API-based JWT (Optional):
```http
POST /api/accounts/login/   → access + refresh token
POST /api/accounts/register/
GET  /api/shop/protected/   → JWT protected route
```

---

## 🖼️ UI Routes (Frontend)

| Route             | Purpose                     |
|------------------|-----------------------------|
| `/`              | Home / Product listing      |
| `/product/<id>/` | Product detail + Add to cart |
| `/cart/`         | View cart, update, remove   |
| `/checkout/`     | Place order from cart       |
| `/orders/`       | View previous orders        |
| `/login/`        | Login page                  |
| `/register/`     | Register new user           |

---

## 💳 Mock Payment System

Simulate successful payment for an order:

```http
POST /api/shop/orders/<order_id>/pay/
```

> Sets `is_paid = True`

---

## 📸 Screenshots

> (Add screenshots here of home, cart, checkout, and admin)

---

## 🧪 Optional Improvements

- Integrate real payment gateways like **Zarinpal** or **Pay.ir**
- Add product search & filters
- RESTful API (DRF) with Swagger docs
- Frontend upgrade to React / Vue
- Dashboard for admins (total sales, orders, etc.)
- Test coverage with `pytest` or Django TestCase

---

## 📜 License

MIT License – feel free to fork and build upon this project for learning or professional use!

---

## ✨ Author

Built with ❤️ by **Misagh**

> Feel free to connect via [LinkedIn](https://www.linkedin.com/in/misaghmomenib/) or check out my portfolio!

```
