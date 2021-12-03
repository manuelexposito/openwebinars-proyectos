package com.pruebasopenwebinars.proyectodesarrolloapirest.error;

import com.fasterxml.jackson.databind.JsonMappingException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.time.LocalDateTime;

@RestControllerAdvice
public class GlobalControllerAdvice {


    @ExceptionHandler(ProductoNotFoundException.class)
    public ResponseEntity<ApiError> handleProductoNoEncontrado(ProductoNotFoundException exception){
    ApiError error = new ApiError(HttpStatus.NOT_FOUND, exception.getMessage());

    return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }

    @ExceptionHandler(JsonMappingException.class)
    public ResponseEntity<ApiError> handleJsonMappingException(JsonMappingException exception){

       ApiError error = new ApiError(HttpStatus.BAD_REQUEST, exception.getMessage());

       return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);

    }




}
