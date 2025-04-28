package com.pham_mishra.parisairline.repository;

import com.pham_mishra.parisairline.model.Airport;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AirportRepository extends JpaRepository<Airport, Long> {
}