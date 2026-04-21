if (inputPassword.equals(user.getPassword())) { 
    // Login success
}

#fix
BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();

if (encoder.matches(inputPassword, user.getPassword())) {
    // Login success
}