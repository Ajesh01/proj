import { Component, OnInit } from '@angular/core';
import {NgForm} from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private httpclient: HttpClient) { }
  onClickSubmit(formData) {
    var dis= document.querySelector("#results");
    globalThis.result="";
    console.log(formData.name)
    this.httpclient.get<any>('http://127.0.0.1:8000/diabetes/name='+formData.name+',gluc='+formData.gluc+',bp='+formData.bp+',tri='+formData.triceps+',ins='+formData.insulin+',bmi='+formData.bmi).subscribe(data => {console.log("data",data);
    globalThis.result=data.result;
    dis.innerHTML="<h7>prediction : "+globalThis.result+" </h7>"
  });
    
    
} 

  ngOnInit(): void {
  }

}
