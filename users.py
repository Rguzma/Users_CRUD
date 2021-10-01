from mysqlconnection import connectToMySQL              #3RD STEP

class User:                                            #3RD STEP
    def __init__(self, data):
        self.id=data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod                                        #3RD STEP
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in results:
            users.append (cls (u))
        return users

