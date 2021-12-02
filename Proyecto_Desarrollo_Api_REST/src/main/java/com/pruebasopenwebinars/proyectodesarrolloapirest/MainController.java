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
    public GetProductoDto getProducto(@PathVariable Long id){

        return productoService.findById(id).map(productoDtoConverter::convertToDto).orElseThrow(() -> new ProductoNotFoundException(id));

    }


    //TODO: Ver como mejorar este código (no funciona)
    @PostMapping("/producto")
    public ResponseEntity<GetProductoDto> createProducto(@NotNull CreateProductoDto newProducto){

        Optional<Categoria> categoriaSelected = categoriaService.findById(newProducto.getCategoriaId());

        if(categoriaSelected.isPresent()){
            Categoria c = categoriaSelected.get();
            Producto savedProducto = productoService.saveProducto(newProducto, productoDtoConverter);
            productoService.addCategoriaToProducto(savedProducto, c, categoriaService);

            return ResponseEntity.status(HttpStatus.CREATED).body(productoDtoConverter.convertToDto(savedProducto));
        }

       return ResponseEntity.status(HttpStatus.BAD_REQUEST).build();

    }


    @ExceptionHandler(ProductoNotFoundException.class)
    public ResponseEntity<ApiError> handleProductoNoEncontrado(ProductoNotFoundException exception){

        ApiError error = new ApiError();

        error.setEstado(HttpStatus.NOT_FOUND);
        error.setFecha(LocalDateTime.now());
        error.setMensaje(exception.getMessage());

        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);

    }

    public ResponseEntity<ApiError> handleJsonMappingException(JsonMappingException exception){

        ApiError error = new ApiError();

        error.setEstado(HttpStatus.BAD_REQUEST);
        error.setFecha(LocalDateTime.now());
        error.setMensaje(exception.getMessage());

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);

    }


}
