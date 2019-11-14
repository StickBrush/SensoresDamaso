# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SensorNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, notif_type: bool=None, timestamp: datetime=None, room: str=None):  # noqa: E501
        """SensorNotification - a model defined in Swagger

        :param notif_type: The notif_type of this SensorNotification.  # noqa: E501
        :type notif_type: bool
        :param timestamp: The timestamp of this SensorNotification.  # noqa: E501
        :type timestamp: datetime
        :param room: The room of this SensorNotification.  # noqa: E501
        :type room: str
        """
        self.swagger_types = {
            'notif_type': bool,
            'timestamp': datetime,
            'room': str
        }

        self.attribute_map = {
            'notif_type': 'notifType',
            'timestamp': 'timestamp',
            'room': 'room'
        }
        self._notif_type = notif_type
        self._timestamp = timestamp
        self._room = room

    @classmethod
    def from_dict(cls, dikt) -> 'SensorNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SensorNotification of this SensorNotification.  # noqa: E501
        :rtype: SensorNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notif_type(self) -> bool:
        """Gets the notif_type of this SensorNotification.

        Tipo de notificación. True si es de presencia, false en caso contrario  # noqa: E501

        :return: The notif_type of this SensorNotification.
        :rtype: bool
        """
        return self._notif_type

    @notif_type.setter
    def notif_type(self, notif_type: bool):
        """Sets the notif_type of this SensorNotification.

        Tipo de notificación. True si es de presencia, false en caso contrario  # noqa: E501

        :param notif_type: The notif_type of this SensorNotification.
        :type notif_type: bool
        """
        if notif_type is None:
            raise ValueError("Invalid value for `notif_type`, must not be `None`")  # noqa: E501

        self._notif_type = notif_type

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this SensorNotification.

        Timestamp de la notificación  # noqa: E501

        :return: The timestamp of this SensorNotification.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this SensorNotification.

        Timestamp de la notificación  # noqa: E501

        :param timestamp: The timestamp of this SensorNotification.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def room(self) -> str:
        """Gets the room of this SensorNotification.

        Habitación sensorizada  # noqa: E501

        :return: The room of this SensorNotification.
        :rtype: str
        """
        return self._room

    @room.setter
    def room(self, room: str):
        """Sets the room of this SensorNotification.

        Habitación sensorizada  # noqa: E501

        :param room: The room of this SensorNotification.
        :type room: str
        """
        if room is None:
            raise ValueError("Invalid value for `room`, must not be `None`")  # noqa: E501

        self._room = room