from typing import TypeAlias

from .concrete_object_store_model import ConcreteObjectStoreModel
from .user_concrete_object_store_model import UserConcreteObjectStoreModel

__all__ = ["AnonymousArrayItem216"]

AnonymousArrayItem216: TypeAlias = ConcreteObjectStoreModel | UserConcreteObjectStoreModel
