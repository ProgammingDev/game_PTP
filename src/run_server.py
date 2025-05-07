import sys
sys.path.append("src")  # 👈 para que reconozca el paquete ppt

from ppt.api.main import app

if __name__ == "__main__":
    app.run(debug=True, port=4000)