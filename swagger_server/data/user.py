from singleton_decorator import singleton
from swagger_server.models.status import Status
from datetime import datetime
from swagger_server.data.noDb import NotDB

@singleton
class UserStatus:

    def __init__(self):
        self.STATUSES_COLLECTION = "userstatuses"
        self._DEFAULT_ROOM = "Salón"
        self._DEFAULT_SITTING = False
        self._room = self._DEFAULT_ROOM
        self._sitting = self._DEFAULT_SITTING

    def get_status(self) -> Status:
        return Status(is_sitting=self._sitting, room=self._room, timestamp=datetime.now())

    def change_room(self, room: str) -> None:
        NotDB().append_to_collection(self.STATUSES_COLLECTION, self.get_status())
        self._room = room

    def change_sitting(self, sitting: bool) -> None:
        NotDB().append_to_collection(self.STATUSES_COLLECTION, self.get_status())
        self._sitting = sitting

    def update_status(self, new_status: Status) -> None:
        if new_status.room != self._room:
            if self._sitting:
                self.change_sitting(False)
            self.change_room(new_status.room)
            if new_status.is_sitting:
                self.change_sitting(True)
        else:
            if new_status.is_sitting != self._sitting:
                self.change_sitting(new_status.is_sitting)
