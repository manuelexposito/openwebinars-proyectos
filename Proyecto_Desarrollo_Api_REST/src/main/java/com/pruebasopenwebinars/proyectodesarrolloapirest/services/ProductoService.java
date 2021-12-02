package com.pruebasopenwebinars.proyectodesarrolloapirest.services;

import com.pruebasopenwebinars.proyectodesarrolloapirest.models.Categoria;
import com.pruebasopenwebinars.proyectodesarrolloapirest.models.CreateProductoDto;
import com.pruebasopenwebinars.proyectodesarrolloapirest.models.Producto;
import com.pruebasopenwebinars.proyectodesarrolloapirest.models.ProductoDtoConverter;
import com.pruebasopenwebinars.proyectodesarrolloapirest.repositories.ProductoRepository;
import com.pruebasopenwebinars.proyectodesarrolloapirest.services.base.BaseService;
import org.springframework.stereotype.Service;

@Service
public class ProductoService extends BaseService<Producto, Long, ProductoRepository> {


    public Producto saveProducto(CreateProductoDto dto, ProductoDtoConverter productoDtoConverter){

        Producto p = productoDtoConverter.convertCreateDtoToProducto(dto);

        return save(p);

    }


    public Producto addCategoriaToProducto(Producto p, Categoria c, CategoriaService categoriaService){

        p.addCategoriaToProducto(c);
        categoriaService.edit(c);
        return save(p);

    }

}
