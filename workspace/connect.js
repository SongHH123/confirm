const mysql = require('mysql');
const connection = mysql.createConnection({
  host:'localhost',
  user:'root',
  password:'1234',
  database: 'school',
  port: '3306',
});

connection.connect();
//서버 실행시 삭제
export function Confirm_St(uname, psw){
  connection.query('SELECT stu_id, user_pw from student_info', (error, results, fields) => {
    if(error) throw error;
    var len = results.length;

    for(var i = 0; i<len; i++){
      let info = Object.values(results[i]);
      if(uname == info[0] && psw == info[1]){
        return i;
      }
    }
    return -1;
  });
}

export function Confirm_Tr(uname, psw){
  connection.query('SELECT tch_id, user_pw from teacher_info', (error, results, fields) => {
    if(error) throw error;
    var len = results.length;

    for(var i = 0; i<len; i++){
      let info = Object.values(results[i]);
      if(uname == info[0] && psw == info[1]){
        return i;
      }
    }
    return -1;
  });
}


//connection.end();
