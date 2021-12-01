package com.pruebasopenwebinars.proyectodesarrolloapirest.models;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class CreateProductoDto {

    private String nombre;
    private double precio;
    private Long categoriaId;
}
