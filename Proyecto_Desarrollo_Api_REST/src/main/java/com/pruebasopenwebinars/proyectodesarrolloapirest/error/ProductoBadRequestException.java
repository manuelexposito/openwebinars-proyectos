package com.pruebasopenwebinars.proyectodesarrolloapirest.error;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.BAD_REQUEST)
public class ProductoBadRequestException extends RuntimeException{

    public ProductoBadRequestException(){
        super("No ha podido registrarse el producto. Compruebe si la categoría existe o los datos son correctos.");
    }

}
