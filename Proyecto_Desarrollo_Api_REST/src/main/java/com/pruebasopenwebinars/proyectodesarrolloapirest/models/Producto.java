package com.pruebasopenwebinars.proyectodesarrolloapirest.models;

import lombok.*;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class Producto implements Serializable {

    @Id
    @GeneratedValue
    private Long id;

    private String nombre;
    private double precio;

    @ManyToOne
    @JoinColumn(name="categoria_id")
    private Categoria categoria;


}
