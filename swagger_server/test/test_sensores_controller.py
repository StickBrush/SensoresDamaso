# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.sensor_notification import SensorNotification  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSensoresController(BaseTestCase):
    """SensoresController integration test stubs"""

    def test_get_notification(self):
        """Test case for get_notification

        Devuelve el log de cambios de sensores de una habitación
        """
        response = self.client.open(
            '/sensorapi/notifications/{roomID}'.format(room_id='room_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_notification_log(self):
        """Test case for get_notification_log

        Obtiene el log de cambios de los sensores
        """
        response = self.client.open(
            '/sensorapi/notifications',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notify_change(self):
        """Test case for notify_change

        Notifica de un cambio en los sensores
        """
        body = SensorNotification()
        response = self.client.open(
            '/sensorapi/notifications',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
