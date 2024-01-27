from dataclasses import dataclass
from typing import List

from core.enums.gender import Gender
from core.enums.hobby import Hobby


@dataclass
class User:
    first_name: str
    last_name: str
    phone: str
    gender: Gender
    email: str = None
    date_of_birth: str = None
    subjects: str = None
    hobbies: List[Hobby] = None
    current_address: str = None
    state: str = None
    city: str = None
