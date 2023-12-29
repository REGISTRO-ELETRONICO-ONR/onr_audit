from flask import Flask
from flask_restx import Api
from .namespaces.request_details import RD_ns
from .namespaces.credential import Credential_ns
import config
import os

scenario_options = {
    'development': config.DevelopmentConfig,
    'production': config.ProductionConfig
}


def create_app(scenario=None):
    app = Flask(__name__)
    scenario = scenario or os.getenv("FLASK_CONFIG", "development")
    app.config.from_object(scenario_options[scenario])
    app.config['USE_ASYNCIO'] = True

    api = Api(app, title='ONR AUDIT',
              version='1.0',
              description='API para auditoria de processos da ONR')

    api.add_namespace(RD_ns, path='/request-details')
    api.add_namespace(Credential_ns, path='/credential')

    return app
