from abc import ABC, abstractmethod
from ...dto.transaction_dto import TransactionDTO

class BaseParser(ABC):

    @abstractmethod
    def parser(self, file_path: str) -> list[TransactionDTO]:
        raise NotImplementedError