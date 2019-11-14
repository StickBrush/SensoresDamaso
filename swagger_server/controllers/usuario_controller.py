import connexion
import six

from swagger_server.models.status import Status  # noqa: E501
from swagger_server import util


def change_status(body):  # noqa: E501
    """Actualiza el estado actual del usuario

    Permite actualizar el estado del usuario a nivel alto. # noqa: E501

    :param body: Nuevo estado
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Status.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_curr_status():  # noqa: E501
    """Devuelve el estado actual del usuario

    Facilita conocer el estado del usuario en el timestamp actual sin complicaciones. # noqa: E501


    :rtype: Status
    """
    return 'do some magic!'


def get_status(timestamp):  # noqa: E501
    """Devuelve el estado del usuario en el timestamp especificado

    Permite consultar estados pasados # noqa: E501

    :param timestamp: Timestamp a consultar
    :type timestamp: str

    :rtype: Status
    """
    timestamp = util.deserialize_datetime(timestamp)
    return 'do some magic!'


def get_statuses():  # noqa: E501
    """Devuelve el log de estados del usuario

    Los estados se generan internamente y permiten entender la información más fácilmente. # noqa: E501


    :rtype: List[Status]
    """
    return 'do some magic!'
