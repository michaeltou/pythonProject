

class Query(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print("Entering Query")
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        print("Exiting Query")
        if exc_type is not None:
            print("Exception occurred: ",exc_type,exc_val,exc_tb)
        else:
            print("Query executed successfully")

    def query(self):
        print("Executing query on database")
        raise Exception("Error occurred while executing query")


with Query("Database") as q:
    q.query()

