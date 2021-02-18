import pickle


class DataFile:
    def __init__(self, name):
        self.name = name

    def add_record(self, record):
        file = open(self.name, "ab")
        pickle.dump(record, file)
        file.close()

    def get_records(self):
        records = []
        try:
            file = open(self.name, "rb")
        except FileNotFoundError:
            return records
        while True:
            try:
                record = pickle.load(file)
                records.append(record)
            except EOFError:
                break
        file.close()
        return records

    def overwrite(self, records):
        file = open(self.name, "wb")
        for record in records:
            pickle.dump(record, file)
        file.close()
