import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { HeartComponent } from './heart/heart.component';

const routes: Routes = [{ path: '', component: HomeComponent },
{ path: 'heart-disease', component: HeartComponent }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
