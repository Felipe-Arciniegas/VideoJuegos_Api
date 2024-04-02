from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

    def model_dump(self):
        return {
            "email": self.email,
            "password": self.password
        }
    
    def model_dict(self):
        return {
            "email": self.email,
            "password": self.password
        }
    
    def model_json(self):
        return {
            "email": self.email,
            "password": self.password
        }
    
    def model_list(self):
        return [self.email, self.password]