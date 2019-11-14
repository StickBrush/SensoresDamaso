# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.status import Status  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsuarioController(BaseTestCase):
    """UsuarioController integration test stubs"""

    def test_change_status(self):
        """Test case for change_status

        Actualiza el estado actual del usuario
        """
        body = Status()
        response = self.client.open(
            '/sensorapi/userStatuses/current',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_curr_status(self):
        """Test case for get_curr_status

        Devuelve el estado actual del usuario
        """
        response = self.client.open(
            '/sensorapi/userStatuses/current',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_status(self):
        """Test case for get_status

        Devuelve el estado del usuario en el timestamp especificado
        """
        response = self.client.open(
            '/sensorapi/userStatuses/{timestamp}'.format(timestamp='2013-10-20T19:20:30+01:00'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_statuses(self):
        """Test case for get_statuses

        Devuelve el log de estados del usuario
        """
        response = self.client.open(
            '/sensorapi/userStatuses',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
