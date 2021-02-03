# Teste com proxy entre client e server

## Containers envolvidos

- webapp: simula uma webapplication com flask + gunicorn e no / printa o request.remote_addr e a lista de  x-forwarded-forwarded
```python
@app.route("/")
def hello():
    ip_x_for = ""
    if request.headers.getlist("X-Forwarded-For"):
        list_for = request.headers.getlist("X-Forwarded-For")
        for x in list_for:
            ip_x_for += "," + x
    ip_default = request.remote_addr
    return f"IP default: {ip_default} IP X for: {ip_x_for}"
```
- proxy: repassa a porta 5000 do webapp para a porta 80 desse container.

- testapp: para fazer curl via bash e saber dos comportamentos.
