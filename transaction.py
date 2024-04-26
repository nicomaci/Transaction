from collections import defaultdict

class Database:

    history = []
    current_commit = {}
    transaction = False

    def begin_transaction(self):
        if self.transaction:
            raise Exception("Error: Transaction already in progress")

        self.current_commit = {}
        self.transaction = True
        
        return self.transaction
    
    def put(self, key, value):
        if not self.transaction:
            raise Exception("Error: Transaction not in progress")

        self.current_commit[key] = value

        return key + " : " + str(value)
        
    def commit(self):
        if not self.transaction:
            raise Exception("Error: Transaction not in progress")

        if len(self.history) > 0:
            self.history.append(self.history[-1].copy())
        else:
            self.history.append({})
        
        for k in self.current_commit:
            self.history[-1][k] = self.current_commit[k]

        self.transaction = False

        return "Commit Complete"
    
    def rollback(self):
        if not self.transaction:
            raise Exception("Error: Transaction not in progress")
              
        self.history.pop()

        return "Rollback Complete"

    
    def get(self, key):
        if len(self.history) == 0:
            return None

        if key not in self.history[-1]:
            return None

        return self.history[-1][key]


if __name__ == "__main__":
    db = Database

    print("Expected: Null/None")
    print(db.get(db, "A"))
    print()

    # Error
    # db.put(db, "A", 5)

    print("Expected: True")
    print(db.begin_transaction(db))
    print()

    print("Expected: A : 5")
    print(db.put(db, "A", 5))
    print()

    print("Expected: Null/None")
    print(db.get(db, "A"))
    print()
    
    print("Expected: A : 6")
    print(db.put(db, "A", 6))
    print()

    print("Expected: Commit Complete")
    print(db.commit(db))
    print()

    print("Expected: 6")
    print(db.get(db, "A"))
    print()

    # Error
    # print(db.commit(db))

    # Error
    # print(db.rollback(db))

    print("Expected: Null/None")
    print(db.get(db, "B"))
    print()

    print("Expected: True")
    print(db.begin_transaction(db))
    print()

    print("Expected: B : 10")
    print(db.put(db, "B", 10))
    print()

    db.commit(db)

    print("Expected: 10")
    print(db.get(db, "B"))
    print()

    db.begin_transaction(db)

    print("Excpected: Rollback Complete")
    print(db.rollback(db))
    print()

    print("Excpected: Null/None")
    print(db.get(db, "B"))
    print()
