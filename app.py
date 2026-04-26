from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML = '''
<h1>Admin Portal Mirror</h1>
<p>Status: {{ status }}</p>
<form method="POST">
    Target URL: <input type="text" name="url" placeholder="http://localhost:5000/info">
    <input type="submit" value="Fetch">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    status = "Waiting for input..."
    if request.method == 'POST':
        if request.headers.get('X-Forwarded-For') != '127.0.0.1':
            return "Error: External Access Denied. Only localhost allowed.", 403
        
        target = request.form.get('url')
        try:
            r = requests.get(target, timeout=2)
            return r.text
        except:
            return "Connection Failed."
    return render_template_string(HTML, status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
