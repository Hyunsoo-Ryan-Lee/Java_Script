from typing import Counter
import cx_Oracle
from dto import EmpDTO
import json
import collections

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

    # 모든 직원 검색해서 반환
    # 동기 방식으로 요청
    # 모든 직원 정보 응답시 구조는 보편적으로 선호되는 JSON 포맷
    # Rest API - url 정보가 요청처리 리소스 + JSON 포맷으로 응답 + 비동기 
    # python에서 json 포맷 지원해주는 모듈인 json 사용하여 return 

    def empall(self):

        data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from emp01")
                rows = cur.fetchall()
                # json 포맷으로 가공 : empno,ename,sal을 key로 사용
                # data가 여러개이므로 json 배열!
                v = []
                for row in rows:
                    d = collections.OrderedDict())
                    d['empno'] = row[0]
                    d['ename'] = row[1]
                    d['sal'] = row[2]
                    v.append(d)
                data = json.dumps(v, ensure_ascii=False) #json 포맷으로 자동 변환!!!

            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

        return data #'{"ename":"SMITH", "sal":800}' 이런식으로 return 

if __name__ == "__main__":

    a=EmpDAO()
    print(a.empall())




