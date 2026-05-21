class Member:
    def __init__(self, member_id, name, email, phone):
        self._member_id = member_id
        self._name = name
        self.email = email 
        self._phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Email needs @")
        self._email = value.lower()