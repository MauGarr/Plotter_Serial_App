import { Component, ElementRef, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AnalizarService } from '../services/analizar.service';

@Component({
  selector: 'app-text-edit',
  standalone: true,
  imports: [CommonModule, FormsModule, ReactiveFormsModule],
  templateUrl: './text-edit.component.html',
})
export class TextEditComponent {
  fileContent: string = '';
  fileName: string = '';
  showDropdown = false;
  canSave: boolean = false;
  @ViewChild('fileInput', { static: false }) fileInputRef!: ElementRef<HTMLInputElement>;

  //constructor(private analizarService: AnalizarService) {}

  toggleDropdown() {
    this.showDropdown = !this.showDropdown;
  }

  hideDropdown() {
    this.showDropdown = false;
  }

  openFile() {
    this.fileInputRef.nativeElement.value = '';
    this.fileInputRef.nativeElement.click();
    this.canSave = true;
  }

  fileChange(event: Event) {
    const input = event.target as HTMLInputElement;
    const file = input.files?.[0];
    if (file) {
      this.fileName = file.name;
      const reader = new FileReader();
      reader.onload = () => {
        this.fileContent = reader.result as string;
      };
      reader.readAsText(file);
    } else {
      this.fileContent = 'Error: Por favor selecciona un archivo (.orga).';
    }
  }

  handleTextareaChange(event: Event) {
    const textarea = event.target as HTMLTextAreaElement;
    this.fileContent = textarea.value;
  }

  newFile() {
    this.fileContent = '';
    this.fileName = '';
  }

  saveasFile() {
    const fileName = window.prompt('Por favor ingresa el nombre del archivo');
    if (fileName) {
      this.downloadFile(`${fileName}.orga`, this.fileContent, false);
      this.fileContent = this.fileContent;
    }
    if (!this.canSave) return;
  }

  saveFile() {
    this.downloadFile(this.fileName, this.fileContent, true);
    this.fileContent = this.fileContent;
    if (!this.canSave) return;
  }

  private downloadFile(fileName: string, content: string, addCopy: boolean) {
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    const fileExtension = fileName.slice((fileName.lastIndexOf(".") -1 >>> 0) + 2);
    const baseName = fileName.slice(0, (fileName.lastIndexOf(".") >>> 0));
    link.download = addCopy ? `${baseName}_copia.${fileExtension}` : fileName;
    link.href = url;
    link.click();
    URL.revokeObjectURL(url);
  }

  exit() {
    this.fileContent = '';
    this.fileName = '';
    this.canSave = false;
  }

  /*analizarArchivo() {
    this.analizarService.analizarArchivo(this.fileContent)
      .subscribe(res => {
        // Maneja la respuesta del backend aquí
        console.log(res);
      });
  }*/
}
