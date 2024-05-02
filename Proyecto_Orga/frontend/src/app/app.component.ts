import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from "./navbar/navbar.component";
import { TextEditComponent } from "./text-edit/text-edit.component";
import { FigurasComponent } from "./figuras/figuras.component";

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.css',
    imports: [RouterOutlet, NavbarComponent, TextEditComponent, FigurasComponent]
})
export class AppComponent {
  title = 'Plotter App';
}
