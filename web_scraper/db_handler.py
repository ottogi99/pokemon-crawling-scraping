import psycopg2 as psycopg2


class DBHandler:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()

        if self.conn is not None:
            self.conn.close()

    def connect(self, host, dbname, user, password, port):
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()

    def insert(self, schema, table, columns, values):
        sql = "INSERT INTO {schema}.{table}({columns}) VALUES ({values})".format(
            schema=schema, table=table, columns=columns, values=values
        )
        print(sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("Error occurred during insert: {0}".format(e))

    def select(self, schema, table, columns):
        result = None
        sql = "SELECT {columns} from {schema}.{table}".format(
            schema=schema, table=table, columns=columns
        )
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e:
            print("Error occurred during select: {0}".format(e))

        return result

    def update(self, schema, table, column, value, condition):
        sql = "UPDATE {schema}.{table} SET {column}='{value}' WHERE {column}='{condition}'".format(
            schema=schema, table=table, column=column, value=value, condition=condition
        )
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("Error occurred during update: {0}".format(e))

    def delete(self, schema, table, condition):
        sql = "DELETE FROM {schema}.{table} where {condition};".format(
            schema=schema, table=table, condition=condition
        )
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("Error occurred during update: {0}".format(e))
