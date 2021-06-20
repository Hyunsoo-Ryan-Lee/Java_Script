import cx_Oracle
from DTO import CameraDTO
import json
import collections

class CameraDAO:
    def allCams(self, brand):
        cam_data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from camera where brand=:brand", brand=brand)
                rows = cur.fetchall()
                v = []
                for row in rows:
                    d = collections.OrderedDict()
                    d['brand'] = row[0]
                    d['model'] = row[1]
                    d['price'] = row[2]
                    d['format'] = row[3]
                    v.append(d)
                print(v)
                cam_data = json.dumps(v,ensure_ascii=False)
                       
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)

        finally:
            cur.close()
            conn.close()

        return cam_data 

    def addCams(self, dto):  # EmpDTO 객체를 통으로 매개변수 값으로 받을 예정
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("insert into camera values (:brand, :model, :price, :format)",
                            brand=dto.getBrand(), model=dto.getModel(), price=dto.getPrice(), format=dto.getFormat())
                conn.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    def delCams(self, dto):  # EmpDTO 객체를 통으로 매개변수 값으로 받을 예정
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("delete from camera where brand=:brand and model=:model",
                            brand=dto.getBrand(), model=dto.getModel())
                conn.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

    def showall(self): 

        cam_data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from camera")
                rows = cur.fetchall()
                v = []
                for row in rows:
                    d = collections.OrderedDict()
                    d['brand'] = row[0]
                    d['model'] = row[1]
                    d['price'] = row[2]
                    d['format'] = row[3]
                    v.append(d)
                cam_data = json.dumps(v,ensure_ascii=False)

            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

        return cam_data


if __name__ == "__main__":
    cam = CameraDAO()
    cam.showall()
    


# cam_data = '{"brand":"' + row[0] + '", "model":"' + row[1] + '", "price":' + str(row[2]) + '", "format":' + str(row[3]) + '}'
