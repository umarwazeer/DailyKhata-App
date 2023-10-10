/*
This is the file where i keep my db calls. It might not be necessary to use db.serialize before the
calls but I haven't had time to try
*/
import {db} from '../boot/sqlite'


export function queryAllUsers(){
    return new Promise((resolve, reject) => {
        db.serialize(() => {
            db.all('select id, name, surname, nickname, last_subscription from users', (err, rows) => {
                if (err) reject(err)
                console.log(rows)
                resolve(rows || [])
            });
        })
     })
}

export function insertUser(name, surname, nickname, last_subscription){
    return new Promise((resolve, reject) => {
        db.serialize(() => {
            db.run(`INSERT INTO users(name, surname, nickname, last_subscription) VALUES('${name}', '${surname}', '${nickname}','${last_subscription}' )`, function(err) {
                if (err) {
                    return console.log(err.message);
                }
                resolve(this.lastID);
            });
        });
    })
}

export function deleteUser(id){
  return new Promise((resolve, reject) => {
      db.serialize(() => {
          db.run(`delete from users where id = ${id}; `, function(err) {
              if (err) {
                  return console.log(err.message);
              }
              resolve("delete record successfully",this.lastID);
          });
      });
  })
}

export function updateUser(name, surname, nickname, last_subscription){
  return new Promise((resolve, reject) => {
      db.serialize(() => {
        // name, surname, nickname, last_subscription
          db.run(`update users
          SET name = '${name}', surname = '${surname}', nickname = '${nickname}', last_subscription = '${last_subscription}'
          WHERE id = ${id}`,
           function(err) {
              if (err) {
                  return console.log(err.message);
              }
              resolve(this.lastID);
          });
      });
  })
}


