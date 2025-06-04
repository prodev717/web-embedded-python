# WEP — Web Embedded Python

> **WEP** is a lightweight server-side template engine and micro-framework that lets you embed native Python directly inside HTML files using `.wep` files and `<wep>` tags. Inspired by PHP, it enables rapid prototyping and AI-powered dynamic web content without the complexity of separate frontend and backend layers.

---

## Features

* Embed Python code directly inside `.wep` HTML files using `<wep>...</wep>` blocks
* Simple `echo()` function to output HTML or text from Python code
* Built on Flask for routing and serving static assets
* Minimal setup — write Python and HTML in the same file, no API or frontend framework needed
* Great for rapid prototyping, AI demos, teaching, and simple server-rendered apps

---

## Getting Started

### Prerequisites

* Python 3.7 or newer installed
* `git` installed
* `pip` installed

### Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/prodev717/web-embedded-python.git
   ```

2. **Navigate into the project directory:**

   ```bash
   cd web-embedded-python
   ```

3. **Install the `uv` package manager if you haven’t already:**

   ```bash
   pip install uv
   ```

4. **Install project dependencies using `uv`:**

   ```bash
   uv add flask
   ```

5. **Run the WEP server:**

   ```bash
   uv run main.py
   ```

6. **Open your browser and visit:**

   ```
   http://localhost:8000
   ```

---

### Project Structure

```
wep/
├── public/
│   ├── index.wep
│   └── style.css
└── main.py
```

* `.wep` files contain HTML with embedded Python blocks.
* Static assets like CSS, JS, images live in `public/`.
* `main.py` runs the Flask-based WEP server.

---

### Writing `.wep` Files

Create `.wep` files that look like regular HTML, but with embedded Python inside `<wep>` tags:

```html
<!DOCTYPE html>
<html>
<head>
    <title>WEP Example</title>
</head>
<body>
    <h1>Welcome to WEP!</h1>

<wep>
echo("<p>Current Python version:</p>")
import sys
echo(f"<pre>{sys.version}</pre>")

for i in range(3):
    echo(f"<p>Loop iteration: {i}</p>")
</wep>
</body>
</html>
```

---

### Key Rules for `.wep` and `<wep>` Blocks

1. Python code inside `<wep>...</wep>` must have **zero indentation** (start from column 0).
2. Nested `<wep>` tags are **not supported**.
3. Use the global `echo()` function to send output to the HTML response.
4. Import Python modules as usual inside `<wep>` blocks.
5. Keep logic concise — `.wep` files are meant for presentation + lightweight server-side scripting.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Contribution

Found a bug or want a feature? Please open an issue or submit a pull request.

---

## Inspiration

This project was inspired by PHP’s simple embedded scripting approach and is tailored for Python developers who want fast, easy server-side rendering without the complexity of modern frontend frameworks or APIs.