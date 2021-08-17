import {Confirm_St, Confirm_Tr} from "./connect.js";

export function goPage(role, uname, psw){
  if(role == "st"){
    if(Confirm_St(uname, psw)){
      return "st_main.html";
    }else {
      return -1;
    }
  }else {
    if(Confirm_Tr(uname, psw)){
      return "tr_main.html";
    }else {
      return -2;
    }
  }
}
