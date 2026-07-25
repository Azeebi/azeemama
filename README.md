# Oyeleke Azeezat Bisola — Portfolio (Flask)

A modern, responsive personal portfolio website for **Oyeleke Azeezat Bisola**, an Administrative Professional and B.Sc. Agriculture (Fisheries) graduate.

Built with **Python + Flask + Jinja2 + Tailwind CSS (Play CDN)**.

## Features

- Clean, professional corporate design (navy blue, white & gold palette)
- Fully responsive (desktop, tablet, mobile)
- Smooth scrolling, scroll progress bar, and scroll-reveal animations (vanilla JS `IntersectionObserver`)
- SEO meta tags & accessible markup
- Reusable Jinja2 templates and macros
- Sections: Hero, About, Education, Experience (timeline), Skills, Achievements & Leadership, Interests, Contact
- Server-side contact form (`POST /contact`) with flash messages
- Printable CV page (`/cv`)

## Project Structure

```
app.py                 # Flask application & routes
data.py                # All portfolio content
requirements.txt       # Python dependencies
templates/
  base.html            # Layout, meta tags, Tailwind config
  index.html           # Main single-page portfolio
  cv.html              # Printable CV
  _icons.html          # Inline SVG icon macro
  _macros.html         # Section heading macro
static/
  css/style.css        # Custom styles + animations
  js/main.js           # Navbar, menu, scroll reveal, skill bars
  favicon.svg
venv/                  # Virtual environment
```

## Getting Started (Windows / PowerShell)

The virtual environment is already created. Activate and run:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Or run directly without activating:

```powershell
.\venv\Scripts\python.exe app.py
```

Then open http://127.0.0.1:5000

## Customization

- Edit all content in `data.py`.
- Update the LinkedIn URL in `data.py`.
- The "Download CV" buttons open `/cv` — use the browser's *Print → Save as PDF* to export.
- Set a real `app.secret_key` in `app.py` before deploying.

## Deployment

Use a production WSGI server (e.g. `waitress`) instead of the built-in dev server:

```powershell
pip install waitress
waitress-serve --port=8000 app:app
```
