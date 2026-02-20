from abc import ABC, abstractmethod
from ...dto.transaction_dto import TransactionDTO
from tempfile import TemporaryFile

class BaseParser(ABC):

    @abstractmethod
    def parser(self, file: TemporaryFile) -> list[TransactionDTO]:
        raise NotImplementedError