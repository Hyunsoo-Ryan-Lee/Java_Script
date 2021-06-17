import cx_Oracle
from dto import EmpDTO


class EmpDAO:

    # 직원정보 삭제
    def empdelete(self, dto):  # EmpDTO 객체를 통으로 매개변수 값으로 받을 예정
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("delete from emp01 where empno=:empno", empno=dto.getEmpno())
                conn.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

    # 직원정보 업데이트
    def empupdate(self, dto):  # EmpDTO 객체를 통으로 매개변수 값으로 받을 예정
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                    #update emp01 set ename='KIM', sal=1000 where empno=7000;
                cur.execute("update emp01 set ename=:ename, sal=:sal where empno=:empno", \
                            empno=dto.getEmpno(), ename=dto.getEname(), sal=dto.getSal())
                conn.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

    # 한명의 직원 등록
    def empinsert(self, dto):  # EmpDTO 객체를 통으로 매개변수 값으로 받을 예정
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("insert into emp01 values (:empno, :ename, :sal)",
                            empno=dto.getEmpno(), ename=dto.getEname(), sal=dto.getSal())
                conn.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

    def empone(self, empno):
        data = ''
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from emp01 where empno=:empno", empno=empno)
                row = cur.fetchone()
                print(row) #(7369, 'SMITH', 800.0)
                data = '{"empno":"' + str(row[0]) + '", "ename":"' + row[1] + '", "sal":' + str(row[2]) + '}'
                       
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

        return data #'{"ename":"SMITH", "sal":800}' 이런식으로 return 

if __name__ == "__main__":
    # dao = EmpDAO()
    # dto = EmpDTO(2, 't', 20)
    # dao.empinsert(dto)
    # pass
    a=EmpDAO()
    print(a.empone(7369))


