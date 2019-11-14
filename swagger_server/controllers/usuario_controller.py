import connexion
import six
from datetime import datetime

from swagger_server.models.status import Status  # noqa: E501
from swagger_server import util

from swagger_server.data.noDb import NotDB
from swagger_server.data.user import UserStatus

def change_status(body):  # noqa: E501
    """Actualiza el estado actual del usuario

    Permite actualizar el estado del usuario a nivel alto. # noqa: E501

    :param body: Nuevo estado
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        try:
            body = Status.from_dict(connexion.request.get_json())  # noqa: E501
        except Exception:
            return {}, 405
    ndb = NotDB()
    us = UserStatus()
    us.update_status(body)
    return {}, 200


def get_curr_status():  # noqa: E501
    """Devuelve el estado actual del usuario

    Facilita conocer el estado del usuario en el timestamp actual sin complicaciones. # noqa: E501


    :rtype: Status
    """
    return UserStatus().get_status(), 200


def get_status(timestamp):  # noqa: E501
    """Devuelve el estado del usuario en el timestamp especificado

    Permite consultar estados pasados # noqa: E501

    :param timestamp: Timestamp a consultar
    :type timestamp: str

    :rtype: Status
    """
    timestamp = util.deserialize_datetime(timestamp)
    timestamp = timestamp.replace(tzinfo=None)
    if timestamp > datetime.now():
        response = {}, 405
    else:
        ndb = NotDB()
        stats = ndb.get_collection(UserStatus().STATUSES_COLLECTION)
        if stats is None:
            response = {}, 404
        else:
            found = None
            for st in stats:
                if st.timestamp < timestamp:
                    found = st
                else:
                    break
            if found is None:
                response = {}, 404
            else:
                response = found, 200
    return response


def get_statuses():  # noqa: E501
    """Devuelve el log de estados del usuario

    Los estados se generan internamente y permiten entender la información más fácilmente. # noqa: E501


    :rtype: List[Status]
    """
    ndb = NotDB()
    stats = ndb.get_collection(UserStatus().STATUSES_COLLECTION)
    if stats is None:
        response= {}, 408
    else:
        response = stats, 200
    return response
