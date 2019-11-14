import connexion
import six

from swagger_server.models.sensor_notification import SensorNotification  # noqa: E501
from swagger_server import util


def get_notification(room_id):  # noqa: E501
    """Devuelve el log de cambios de sensores de una habitación

    Se devuelve el log con sus cambios completos, habitación incluida. # noqa: E501

    :param room_id: Habitación de la que obtener el cambio
    :type room_id: str

    :rtype: List[SensorNotification]
    """
    return 'do some magic!'


def get_notification_log():  # noqa: E501
    """Obtiene el log de cambios de los sensores

    El log se obtiene completo, salvo en caso de estar vacío # noqa: E501


    :rtype: List[SensorNotification]
    """
    return 'do some magic!'


def notify_change(body):  # noqa: E501
    """Notifica de un cambio en los sensores

    Se notifica de un cambio concreto en un timestamp concreto # noqa: E501

    :param body: Cambio en el sensor
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SensorNotification.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
