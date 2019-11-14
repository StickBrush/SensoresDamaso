from singleton_decorator import singleton
import pickle
from os.path import exists
from threading import Lock

@singleton
class NotDB:

    def __init__(self):
        self.__PICKLE_FILE = "database.pickle"
        self._database={}
        self._save_lock = Lock()
        self.__load()

    def __load(self) -> bool:
        if exists(self.__PICKLE_FILE):
            with open(self.__PICKLE_FILE, 'rb') as file:
                self._database=pickle.load(file)
            return True
        else:
            return False

    def __save(self) -> None:
        self._save_lock.acquire()
        try:
            with open(self.__PICKLE_FILE, 'wb') as file:
                pickle.dump(self._database, file)
        finally:
            self._save_lock.release()

    def create_collection(self, name: str) -> bool:
        if name not in self._database:
            self._database[name] = []
            self.__save()
            return True
        else:
            return False

    def get_collection(self, name: str) -> list:
        if name not in self._database:
            return None
        else:
            return self._database[name]

    def update_collection(self, name: str, new_list: list) -> None:
        self._database[name] = new_list
        self.__save()

    def append_to_collection(self, name: str, new_object) -> None:
        if name not in self._database:
            self.create_collection(name)
        self._database[name].append(new_object)
        self.__save()

    def remove_collection(self, name: str) -> bool:
        if name not in self._database:
            return False
        else:
            self._database.pop(name)
            self.__save()
            return True


