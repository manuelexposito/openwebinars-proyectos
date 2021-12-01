package com.pruebasopenwebinars.proyectodesarrolloapirest.models;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class GetProductoDto {

    private String nombre;
    private double precio;
    private String categoriaNombre;

}
