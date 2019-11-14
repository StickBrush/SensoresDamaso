import connexion
import six

from swagger_server.models.sensor_notification import SensorNotification  # noqa: E501
from swagger_server import util

from swagger_server.data.noDb import NotDB
from swagger_server.data.user import UserStatus
from swagger_server.models.status import Status

NOTIFICATIONS_COLLECTION_NAME = "notifications"
VALID_ROOMS = ["Salón", "Dormitorio", "Cocina"]

def get_notification(room_id):  # noqa: E501
    """Devuelve el log de cambios de sensores de una habitación

    Se devuelve el log con sus cambios completos, habitación incluida. # noqa: E501

    :param room_id: Habitación de la que obtener el cambio
    :type room_id: str

    :rtype: List[SensorNotification]
    """
    ndb = NotDB()
    nots = ndb.get_collection(NOTIFICATIONS_COLLECTION_NAME)
    if room_id not in VALID_ROOMS:
        response = {}, 404
    else:
        if nots is None:
            response = {}, 408
        else:
            nots = list(filter(lambda x: x.room==room_id, nots))
            if len(nots) == 0:
                response = {}, 408
            else:
                response = nots, 200
    return response

def get_notification_log():  # noqa: E501
    """Obtiene el log de cambios de los sensores

    El log se obtiene completo, salvo en caso de estar vacío # noqa: E501


    :rtype: List[SensorNotification]
    """
    ndb = NotDB()
    nots = ndb.get_collection(NOTIFICATIONS_COLLECTION_NAME)
    if nots == None or len(nots) == 0:
        response = {}, 408
    else:
        response = nots, 200
    return response

def notify_change(body):  # noqa: E501
    """Notifica de un cambio en los sensores

    Se notifica de un cambio concreto en un timestamp concreto # noqa: E501

    :param body: Cambio en el sensor
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        try:
            body = SensorNotification.from_dict(connexion.request.get_json())  # noqa: E501
        except Exception:
            return {}, 405
    ndb = NotDB()
    nots = ndb.get_collection(NOTIFICATIONS_COLLECTION_NAME)
    if nots is not None:
        nots = list(filter(lambda x: x.timestamp == body.timestamp, nots))
        if len(nots) > 0:
            response = {}, 406
    else:
        ndb.append_to_collection(NOTIFICATIONS_COLLECTION_NAME, body)
        response = {}, 200
        us = UserStatus()
        stat = Status(is_sitting=body.notif_type, room=body.room, timestamp=body.timestamp)
        us.update_status(stat)
    return response

