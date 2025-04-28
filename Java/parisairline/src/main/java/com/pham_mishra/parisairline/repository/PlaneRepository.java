package com.pham_mishra.parisairline.repository;

import com.pham_mishra.parisairline.model.Plane;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PlaneRepository extends JpaRepository<Plane, Long> {
}