from app import create_app

port = 5000
host = '0.0.0.0'

app = create_app(scenario='production')

# se for local ou em VM
if __name__ == '__main__':
    app.run(host=host, port=port)
