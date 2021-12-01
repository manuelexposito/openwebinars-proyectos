package com.pruebasopenwebinars.proyectodesarrolloapirest.services;

import com.pruebasopenwebinars.proyectodesarrolloapirest.models.Categoria;
import com.pruebasopenwebinars.proyectodesarrolloapirest.repositories.CategoriaRepository;
import com.pruebasopenwebinars.proyectodesarrolloapirest.services.base.BaseService;

import org.springframework.stereotype.Service;

@Service
public class CategoriaService extends BaseService<Categoria, Long, CategoriaRepository> {
}
