import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-figuras',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './figuras.component.html',
})
export class FigurasComponent {
  matriz = Array(3).fill(Array(3).fill(''));
}