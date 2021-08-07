import {Confirm_St, Confirm_Tr} from "./connect.js";

export function goPage(){
  if(role == "st"){
    if(Confirm_St(uname, psw)){
      return Confirm_St(uname, psw);
    }else {
      return -1;
    }
  }else {
    if(Confirm_Tr(uname, psw)){
      return Confirm_Tr(uname, psw);
    }else {
      return -1;
    }
  }
}
