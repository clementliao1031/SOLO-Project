from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Collect:
    db_name = 'collects'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.review = db_data['review']
        self.pro_con = db_data['pro_con']
        self.pass_buy = db_data['pass_buy']
        self.date_purchase = db_data['date_purchase']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO collects (name, review, pro_con, pass_buy, date_purchase, user_id) VALUES (%(name)s,%(review)s,%(pro_con)s,%(pass_buy)s,%(date_purchase)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM collects;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_collects = []
        for row in results:
            print(row['date_purchase'])
            all_collects.append( cls(row) )
        return all_collects
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM collects WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE collects SET name=%(name)s, review =%(review)s, pro_con=%(pro_con)s, pass_buy=%(pass_buy)s, date_purchase=%(date_purchase)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM collects WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_collect(collect):
        is_valid = True
        if len(collect['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters","collect")
        if len(collect['review']) < 3:
            is_valid = False
            flash("Review must be at least 3 characters","collect")
        if len(collect['pro_con']) < 3:
            is_valid = False
            flash("Pros/Cons must be at least 3 characters","collect")
        if collect['date_purchase'] == "":
            is_valid = False
            flash("Please enter a date","collect")
        return is_valid
