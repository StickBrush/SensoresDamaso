#!/usr/bin/env python3

import connexion
import os

from swagger_server import encoder
from swagger_server.metrics.utils import Uptimer


def main():
    port = int(os.environ.get("PORT", 8080))
    uptimer = Uptimer()
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Dámaso sensorización API'}, pythonic_params=True)
    app.run(port=port)


if __name__ == '__main__':
    main()
