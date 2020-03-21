package com.etang.rest.model;

public class User {

    public User() {

    }

    public User(String userLogin, String userData) {
        super();
        this.userLogin = userLogin;
        this.userData = userData;
    }
 
    private String userLogin;
    private String userData;

    public String getUserLogin() {
        return userLogin;
    }

    public void setUserLogin(String userLogin) {
        this.userLogin = userLogin;
    }

    public String getUserData() {
        return userData;
    }

    public void setUserData(String userData) {
        this.userData = userData;
    }

    @Override
    public String toString() {
        return "Employee [login=" + userLogin + ", data=" + userData +"]";
    }
}
