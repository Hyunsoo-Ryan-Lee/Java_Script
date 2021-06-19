from flask import Flask, request, render_template
#class 소환
from dao import EmpDAO 
from dto import EmpDTO

app = Flask(__name__)


@app.route('/',methods=['get'])
def get():
    return render_template('reqres.html')

# @app.route('/getdata',methods=['get'])
# def getdata():
#     print("-----------------------------")
#     return '{"name":"현수", "age":30}'


@app.route('/camera',methods=['get'])
def getdata():
    print("-----------------------------")
    return '{"brand":"nikon", "model":"FM2"}'



@app.route('/getemp',methods=['post'])
def getemp():
    return EmpDAO().empone(request.form.get("empno")) \
    # get("empno") 여기서 empno는 >>>> xhttp.send("empno=" + document.getElementById("empno").value); 이 친구로부터 받은 친구

    #'{"ename":"SMITH", "sal":800}' 이런식으로 return 



@app.route('/insert',methods=['post'])
def insertemp():

    dao = EmpDAO()
    dto = EmpDTO(request.form.get('empno'),request.form.get('ename'),request.form.get('sal'))
    dao.empinsert(dto) #EmpDTO class의 객체를 변수로 집어넣음
    #이 과정이 끝나면 DB에 직원 내용이 추가됨

    return dao.empone(request.form.get('empno'))

@app.route('/update',methods=['put'])
def updateemp():

    dao = EmpDAO()
    dto = EmpDTO(request.form.get('empno'),request.form.get('ename'),request.form.get('sal'))
    dao.empupdate(dto) #update가 발생!

    return dao.empone(request.form.get('empno'))

@app.route('/delete',methods=['delete'])
def deleteemp():
    dao = EmpDAO()
    dto = EmpDTO(request.form.get('empno'),"",0)
    dao.empdelete(dto)
    return dao.empone(request.form.get('empno'))

# 모든 직원정보를 요청 및 응답하는 함수
@app.route('/emplist',methods=['get'])
def emplist():
    dao = EmpDAO()
    return dao.empall()


    

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
