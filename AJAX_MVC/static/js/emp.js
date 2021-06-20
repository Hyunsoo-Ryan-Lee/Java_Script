//전직원 조회
function allEmp() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert("모든 직원 정보 불러오기")
            data = this.responseText;
            data = JSON.parse(data);
            //document.getElementById("demo4").innerText = data;
            tab = `
            <table border="1">
                <tr><th>사번</th><th>이름</th><th>급여</th></tr>`;
                let empno;
                let ename;
                let sal;
                for (i in data) {
                    empno = data[i].empno;
                    ename = data[i].ename;
                    sal = data[i].sal;

                tab = tab + `<tr>
                    <td>${empno}</td>
                    <td>${ename}</td>
                    <td>${sal}</td> 
                </tr>`;
                //벡틱 내의 문자열 인터폴레이션은 ${ … }으로 표현식을 감싼다. 
                }
            tab = tab + `</table>`;
            document.getElementById("demo4").innerHTML=tab;
        }

    };
    xhttp.open("GET", "emplist");
    xhttp.send();
};



//삭제
function deleteEmp() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            alert("직원 정보가 삭제되었습니다.")
            data = this.responseText;
            data = JSON.parse(data);
        }
    };
    xhttp.open("DELETE", "delete");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    queryString = "empno=" + document.getElementById("delempno").value; //delete를 위해선 empno 정보만 알면됨
    xhttp.send(queryString);
};

//수정
function updateEmp() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            data = this.responseText;
            document.getElementById("demo3").innerText = data;
            alert("직원 정보가 수정되었습니다.")
            data = JSON.parse(data);
            document.getElementById("ename").value = document.getElementById("upename").value;
            document.getElementById("sal").value = document.getElementById("upsal").value;
            document.getElementById("empno").value = document.getElementById('upempno').value;
        }
    };
    xhttp.open("PUT", "update");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    queryString = "empno=" + document.getElementById("upempno").value
        + "&ename=" + document.getElementById("upename").value
        + "&sal=" + document.getElementById("upsal").value;
    xhttp.send(queryString);

}

//등록
function insertEmp() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            data = this.responseText;
            alert("직원 정보가 등록되었습니다.")
            document.getElementById("demo3").innerText = data;
            data = JSON.parse(data);
            document.getElementById("empno").value = document.getElementById('newEmpno').value;
            document.getElementById("ename").value = document.getElementById("newEname").value;
            document.getElementById("sal").value = document.getElementById("newSal").value;
        }
    };
    xhttp.open("POST", "insert");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    queryString = "empno=" + document.getElementById("newEmpno").value
        + "&ename=" + document.getElementById("newEname").value
        + "&sal=" + document.getElementById("newSal").value;

    xhttp.send(queryString);
};


//---------------------------------------------------------------------------
function myAjax() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {

            data = this.responseText;
            document.getElementById("demo1").innerText = data;
            data = JSON.parse(data);
            document.getElementById('brand').value = data.brand;
            document.getElementById('model').value = data.model;
        }
    };
    xhttp.open("GET", "camera");
    xhttp.send();
};


function myAjax2() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {

            data = this.responseText; // data = '{"ename":"SMITH", "sal":800}' 
            alert("직원 정보 호출!")
            data = JSON.parse(data);
            document.getElementById("demo2").innerHTML
                = "사번 : " + data.empno + "\n\n이름 : " + data.ename + "\n\n급여 : " + data.sal;
            document.getElementById("empno").value = data.empno;
            document.getElementById("ename").value = data.ename;
            document.getElementById("sal").value = data.sal;
        }
    };
    xhttp.open("POST", "getemp");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("empno=" + document.getElementById("empno").value);

};