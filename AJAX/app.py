from flask import Flask, request, render_template
from dao import EmpDAO #class 소환

app = Flask(__name__)


@app.route('/',methods=['get'])
# method 속성 생략시 get 방식이 default
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
    empno = request.form.get('empno')
    # reqres.html 에서 넘어온 xhttp.send("empno="+document.getElementById("empno").value); 값 받음

    dao = EmpDAO() # empone() 메소드 보유한 객체 생성
    data = dao.empone(empno) # select후 json 포맷의 문자열로 가공해서 반환하는 메소드 호출
    return data # html 파일로 data값 넘김!(거의 마지막)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
