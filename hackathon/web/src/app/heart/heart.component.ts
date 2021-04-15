import { Component, OnInit } from '@angular/core';
import {NgForm} from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-heart',
  templateUrl: './heart.component.html',
  styleUrls: ['./heart.component.css']
})
export class HeartComponent implements OnInit {

  constructor(private httpclient: HttpClient) { }
  onClickSubmit(formData) {console.log(formData.chest)
    var dis= document.querySelector("#results");
    globalThis.result="";
    console.log(formData.thalach)
    this.httpclient.get<any>('http://127.0.0.1:8000/heart/age='+formData.age+',sex='+formData.sex+',cp='+formData.cp+',trestbps='+formData.trestbps+',chol='+formData.chol+',fbs='+formData.fbs+',restecg='+formData.restecg+',thalach='+formData.thalach+',exang='+formData.exang+',oldpeak='+formData.oldpeak+',slope='+formData.slope+',ca='+formData.ca+',thal='+formData.thal).subscribe(data => {console.log("data",data);
    globalThis.result=data.result;
    dis.innerHTML="<h7>prediction : "+globalThis.result+" </h7>"
  });
    
    
} 
  ngOnInit(): void {
  }

}
