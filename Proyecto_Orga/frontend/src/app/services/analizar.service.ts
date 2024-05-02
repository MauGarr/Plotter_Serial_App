import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AnalizarService {

  constructor(private http: HttpClient) { }

  analizarArchivo(contenido: string) {
    return this.http.post('ruta, backend', { contenido });
  }
}