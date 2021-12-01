package com.pruebasopenwebinars.proyectodesarrolloapirest.repositories;

import com.pruebasopenwebinars.proyectodesarrolloapirest.models.Categoria;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CategoriaRepository extends JpaRepository<Categoria, Long> {
}
