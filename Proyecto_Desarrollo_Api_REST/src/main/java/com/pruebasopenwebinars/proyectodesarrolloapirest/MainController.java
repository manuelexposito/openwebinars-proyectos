package com.pruebasopenwebinars.proyectodesarrolloapirest;

import com.pruebasopenwebinars.proyectodesarrolloapirest.error.CategoriaNotFoundException;
import com.pruebasopenwebinars.proyectodesarrolloapirest.error.ProductoBadRequestException;
import com.pruebasopenwebinars.proyectodesarrolloapirest.error.ProductoNotFoundException;
import com.pruebasopenwebinars.proyectodesarrolloapirest.models.*;
import com.pruebasopenwebinars.proyectodesarrolloapirest.services.CategoriaService;
import com.pruebasopenwebinars.proyectodesarrolloapirest.services.ProductoService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Optional;

@RestController
@RequiredArgsConstructor
public class MainController {

    private final ProductoService productoService;
    private final ProductoDtoConverter productoDtoConverter;
    private final CategoriaService categoriaService;

    //@GetMapping()
    //public List<GetProductoDto> findAllProductos()

    @GetMapping("/producto/{id}")
    public GetProductoDto getProducto(@PathVariable Long id){

        return productoService.findById(id).map(productoDtoConverter::convertToDto).orElseThrow(() -> new ProductoNotFoundException(id));

    }


    //TODO: Ver como mejorar este código (no funciona)
    @PostMapping("/producto")
    public GetProductoDto createProducto(CreateProductoDto newProducto){

        Optional<Categoria> categoriaSelected = categoriaService.findById(newProducto.getCategoriaId());
        Producto p = productoDtoConverter.convertCreateDtoToProducto(newProducto);
        productoService.save(p);
        Categoria c = categoriaSelected.get();
        productoService.addCategoriaToProducto(p, c);
        productoService.edit(p);
        categoriaService.edit(c);

        return productoService.findById(p.getId()).map(productoDtoConverter::convertToDto).orElseThrow(()-> new ProductoBadRequestException());

    }

}
