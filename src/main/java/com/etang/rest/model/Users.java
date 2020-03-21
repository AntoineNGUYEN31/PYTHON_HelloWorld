package com.etang.rest.model;

import java.util.ArrayList;
import java.util.List;

public class Users
{
    private List<User> database;
    
    public List<User> getUserList() {
        if(database == null) {
            database = new ArrayList<>();
        }
        return database;
    }
 
    public void setUserList(List<User> userlist) {
        this.database = userlist;
    }

    public void addUser(User user) {
        this.getUserList().add(user);
    }
}
