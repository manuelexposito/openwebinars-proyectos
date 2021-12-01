package com.pruebasopenwebinars.proyectodesarrolloapirest.config;

import org.modelmapper.ModelMapper;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MiConfig {

    @Bean
    public ModelMapper modelMapper(){

        return new ModelMapper();

    }
}
