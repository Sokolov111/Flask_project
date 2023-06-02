class DataBase:
    def __init__(self,db):
        self.__db = db
        self.__cur = db.cursor()

    def getHeader(self):
        sql = ''' SELECT * FROM header '''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
                print("Ошибка чтения")
        return []

    def getContent(self):
        sql = ''' SELECT name , text FROM pages '''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Ошибка чтения")
        return []

