from flask import Flask,Response,send_from_directory
import re
import os
import traceback

ROOT = "public"
OUTPUT = ""

def echo(tag):
    global OUTPUT
    OUTPUT += tag
    
def webembeddedpython(fn):
    global OUTPUT
    file_path = os.path.join(ROOT,fn)
    if not os.path.exists(file_path):
        return Response(f"Error: File '{fn}' not found.", status=404, mimetype="text/plain")
    try:
        with open(ROOT + "/" + fn, "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        return Response(f"Error reading file: {e}", status=500, mimetype="text/plain")
    def replace_wep(match):
        global OUTPUT
        OUTPUT = ""
        code = match.group(1)
        try:
            exec(code, globals())
            return OUTPUT
        except Exception:
            error = traceback.format_exc()
            print("Execution Error in <wep> block:\n", error)
            return f"<pre style='background-color:#7f1d1d; color:#fca5a5; padding:1rem; border-radius:0.5rem;'>Execution Error:\n{error}</pre>"
    try:
        processed_html = re.sub(r"<wep>(.*?)</wep>", replace_wep, html, flags=re.DOTALL)
    except re.error as re_err:
        return Response(f"Regex Error: {re_err}", status=500, mimetype="text/plain")
    return Response(processed_html, mimetype="text/html; charset=utf-8")

app = Flask(__name__)

@app.route("/")
def index():
    wep_path = os.path.join(ROOT, "index.wep")
    html_path = os.path.join(ROOT, "index.html")
    if os.path.exists(wep_path):
        return webembeddedpython("index.wep")
    elif os.path.exists(html_path):
        return send_from_directory(ROOT, "index.html")
    else:
        return Response("Neither index.wep nor index.html found.", status=404, mimetype="text/plain")

@app.route("/<filename>")
def serve(filename):
    if filename.endswith(".wep"):
        return webembeddedpython(filename)
    file_path = os.path.join(ROOT, filename)
    if not os.path.exists(file_path):
        return Response(f"File '{filename}' not found.", status=404, mimetype="text/plain")
    return send_from_directory(ROOT,filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)
