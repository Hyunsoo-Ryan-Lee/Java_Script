#emp01 table의 crud 로직을 전달하는 class
import cx_Oracle

class EmpDAO:
    # 사번으로 직원명, 급여를 검색해서 반환 
    def empone(self, empno):  
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from emp01 where empno=:empno", empno=empno) 
                    # app.py의 def getemp(): 함수에서 넘어온 empno값이 들어옴
                row = cur.fetchone() 

                #json 포맷으로 편집
                # data = '{"ename":"SMITH","sal":800}'
                data = '{"ename":"' + row[0] + '", "sal":' + str(row[2]) +'}'
                # data를 app.py로 넘겨줌

            except Exception as e: # 예외..
                print(e) # print e
        finally:
            cur.close() # 자원 반환
            conn.close()
            
        return data

if __name__ == "__main__":
    dao = EmpDAO()
    print(dao.empone(7369))
