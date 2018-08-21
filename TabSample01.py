import StatX
import json

class TabSample01(StatX)

    def __init__(self):
        StatX.__init__(self)

    # connect database

"""
def case1(somearg):
    pass
def case2(somearg):
    pass
def case3(somearg):
    pass

switch={
1: case1,
2: case2,
3: case3
}

switch[case](arg)
"""

    def querydb(db):

        myStat = StatX(X, Y)

        cursor = db.cursor()
        sql = "SELECT * FROM Student"

        try:
            cursor.execute(sql)
            results = cursor.fetchall()

            for row in results:
                ID = row[0]
                Name = row[1]
                Grade = row[2]

                if x0:
                    myStat.statX(0)
                if x1:
                    myStat.statX(1)

                if y0:
                    myStat.statY(0)

                myStat.resetX()
        except:
            print "Error: unable to fecth data"

        json_str = myStat.getResult()
        return json.dumps(json_str)

