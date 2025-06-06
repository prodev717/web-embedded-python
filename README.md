# WEP — Web Embedded Python

> **WEP** is a lightweight server-side template engine and micro-framework that lets you embed native Python directly inside HTML using `.wep` files and `<wep>` tags. Inspired by PHP, WEP enables rapid prototyping and AI-powered dynamic web content — without the complexity of separate frontend/backend stacks or REST APIs.

---

## 🚀 Features

* ✅ Write Python directly inside HTML using `<wep>...</wep>` blocks
* ✅ Output content using the simple `echo()` function
* ✅ Built with Flask under the hood
* ✅ Minimal setup — no frontend frameworks or build tools needed
* ✅ Ideal for quick demos, server-rendered sites, teaching, and prototyping AI apps
* ✅ Supports special variables like `_GET`, `_POST`, `GLOBAL`, and `SESSION` inside `<wep>` blocks for handling requests and session data


---

## 📦 Prerequisites

* Python 3.7+
* `git`
* `pip` (Python package manager)
* [`uv`](https://pypi.org/project/uv/) (modern Python package manager — install with `pip install uv`)

---

## ⚙️ Installation & Setup

1. **Clone this repository:**

   ```bash
   git clone https://github.com/prodev717/web-embedded-python.git
   ```

2. **Navigate to the project folder:**

   ```bash
   cd web-embedded-python
   ```

3. **Install `uv` if you don’t already have it:**

   ```bash
   pip install uv
   ```

4. **Install dependencies:**

   ```bash
   uv add flask
   ```

5. **Run the server:**

   ```bash
   uv run main.py
   ```

6. **Visit your app:**

   ```
   http://localhost:8000
   ```

---

## 📁 Project Structure

```
web-embedded-python/
├── public/
│   ├── index.wep         # Homepage with embedded Python
│   ├── demo.wep          # Optional additional demo
│   └── style.css         # Any static assets (CSS, JS, images)
└── main.py               # Flask-based server
```

---

## ✍️ Writing `.wep` Files

`.wep` files are HTML with embedded Python blocks inside `<wep>...</wep>` tags:

```html
<!DOCTYPE html>
<html>
<head><title>WEP Example</title></head>
<body>
  <h1>Hello from WEP</h1>

<wep>
echo("<p>This is Python inside HTML!</p>")

import sys
echo(f"<pre>Python version: {sys.version}</pre>")

for i in range(3):
    echo(f"<p>Loop: {i}</p>")
</wep>
</body>
</html>
```

---

## 📌 WEP Rules

1. Python code inside `<wep>` must be **zero-indented** (start from column 0).
2. **Nested `<wep>` tags** are not supported.
3. Use the global `echo()` function to write content to the HTML output.
4. Use standard Python imports as needed.
5. `.wep` files are best for **lightweight server-side logic**, not heavy lifting.

---

## 🧩 Adding More Dependencies

Need extra packages (e.g., `requests`, `openai`, `pandas`)?
Just run:

```bash
uv add package_name
```

---

## 🛠️ Contributing

Found a bug or have an idea?
Feel free to open an [issue](https://github.com/prodev717/web-embedded-python/issues) or submit a pull request. Contributions welcome!

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 💡 Inspiration

WEP is inspired by PHP's simplicity, adapted for the Python ecosystem.
It’s perfect for Python devs who want to prototype fast — without learning a new frontend stack.
