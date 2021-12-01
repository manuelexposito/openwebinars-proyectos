package com.pruebasopenwebinars.proyectodesarrolloapirest.services;

import com.pruebasopenwebinars.proyectodesarrolloapirest.models.Categoria;
import com.pruebasopenwebinars.proyectodesarrolloapirest.models.Producto;
import com.pruebasopenwebinars.proyectodesarrolloapirest.models.ProductoDtoConverter;
import com.pruebasopenwebinars.proyectodesarrolloapirest.repositories.ProductoRepository;
import com.pruebasopenwebinars.proyectodesarrolloapirest.services.base.BaseService;
import org.springframework.stereotype.Service;

@Service
public class ProductoService extends BaseService<Producto, Long, ProductoRepository> {

    public void addCategoriaToProducto(Producto p, Categoria c){
        p.addCategoriaToProducto(c);
    }

}
