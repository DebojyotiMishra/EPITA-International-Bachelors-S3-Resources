package com.pham_mishra.parisairline.repository;

import com.pham_mishra.parisairline.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}