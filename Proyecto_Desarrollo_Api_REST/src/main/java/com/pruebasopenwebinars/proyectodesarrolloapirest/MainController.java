package com.pruebasopenwebinars.proyectodesarrolloapirest;

import com.fasterxml.jackson.databind.JsonMappingException;
import com.pruebasopenwebinars.proyectodesarrolloapirest.error.ApiError;


import com.pruebasopenwebinars.proyectodesarrolloapirest.error.ProductoNotFoundException;
import com.pruebasopenwebinars.proyectodesarrolloapirest.models.*;
import com.pruebasopenwebinars.proyectodesarrolloapirest.services.CategoriaService;
import com.pruebasopenwebinars.proyectodesarrolloapirest.services.ProductoService;
import com.sun.istack.NotNull;
import lombok.RequiredArgsConstructor;
import lombok.extern.java.Log;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@RestController
@RequiredArgsConstructor
@Log
public class MainController {

    private final ProductoService productoService;
    private final ProductoDtoConverter productoDtoConverter;
    private final CategoriaService categoriaService;

    //@GetMapping()
    //public List<GetProductoDto> findAllProductos()

    @GetMapping("/producto/{id}")
    public GetProductoDto getProducto(@PathVariable Long id) {

        return productoService.findById(id).map(productoDtoConverter::convertToDto).orElseThrow(() -> new ProductoNotFoundException(id));

    }


    //TODO: Ver como mejorar este código (no funciona)
    @PostMapping("/producto")
    public ResponseEntity<GetProductoDto> createProducto(CreateProductoDto newProducto) {


        Producto savedProducto = productoService.saveProducto(newProducto, productoDtoConverter);

        Optional<Categoria> categoriaSelected = categoriaService.findById(newProducto.getCategoriaId());
        Categoria c = categoriaSelected.get();
        productoService.addCategoriaToProducto(savedProducto, c, categoriaService);

        return ResponseEntity.status(HttpStatus.CREATED).body(productoDtoConverter.convertToDto(savedProducto));

    }


}
