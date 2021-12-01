package com.pruebasopenwebinars.proyectodesarrolloapirest.models;

import lombok.RequiredArgsConstructor;
import org.modelmapper.ModelMapper;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class ProductoDtoConverter {

    private final ModelMapper modelMapper;


    public GetProductoDto convertToDto(Producto producto){

        return modelMapper.map(producto, GetProductoDto.class);

    }

    public Producto convertCreateDtoToProducto(CreateProductoDto productoDto){

        return Producto.builder()
                .nombre(productoDto.getNombre())
                .precio(productoDto.getPrecio())
                .build();


    }

}
