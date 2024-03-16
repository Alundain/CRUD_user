from mysqlconnection import connectToMySQL
class User:
    def __init__(self, data):
        self.first_name =data['first_name']
        self.last_name =data['last_name']
        self.email =data['email']
        self.created_at =data['created_at']
    
    def full_Name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s,%(last_name)s, %(email)s);"
        result = connectToMySQL('users').query_db(query,data)
        print("Resultado de la inserción:", result)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for u in results: 
            users.append(cls(u))
        return users
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users').query_db(query,data)
        return cls(result[0])