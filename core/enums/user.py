from dataclasses import dataclass, asdict
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


def convert_user_object_to_dict(user: User) -> dict:
    expected_date = asdict(user)
    expected_date["student_name"] = f"{user.first_name} {user.last_name}"
    if user.state and user.city:
        expected_date["state_and_city"] = f"{user.state} {user.city}"
    del expected_date["first_name"]
    del expected_date["last_name"]
    del expected_date["state"]
    del expected_date["city"]
    return expected_date
