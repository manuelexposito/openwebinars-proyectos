package com.pruebasopenwebinars.proyectodesarrolloapirest.error;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonFormat.Shape;
import lombok.*;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ExceptionHandler;

import java.time.LocalDateTime;

@Getter
@Setter
public class ApiError {

    private HttpStatus estado;
    @JsonFormat(shape = Shape.STRING, pattern = "dd/MM/yyyy hh:mm:ss")
    private LocalDateTime fecha;
    private String mensaje;


}
