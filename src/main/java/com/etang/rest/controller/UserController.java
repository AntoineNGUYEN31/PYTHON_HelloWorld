package com.etang.rest.controller;

import java.net.URI;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import com.etang.rest.model.User;
import com.etang.rest.model.Users;

@RestController
@RequestMapping(path = "/database")
public class UserController 
{
    
    private Users users=new Users();

    @GetMapping(path="/", produces = "application/json")
    public Users getUsers() 
    {
        return users;
    }
    
    @PostMapping(path= "/", consumes = "application/json", produces = "application/json")
    public User addUser(
                        @RequestBody User user) 
                 throws Exception 
    {       
        
        //add resource
        users.addUser(user);
        return user;
    }
}
