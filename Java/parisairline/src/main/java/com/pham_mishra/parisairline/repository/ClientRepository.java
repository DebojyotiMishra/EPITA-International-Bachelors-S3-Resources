package com.pham_mishra.parisairline.repository;

import com.pham_mishra.parisairline.model.Client;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ClientRepository extends JpaRepository<Client, Long> {
}
