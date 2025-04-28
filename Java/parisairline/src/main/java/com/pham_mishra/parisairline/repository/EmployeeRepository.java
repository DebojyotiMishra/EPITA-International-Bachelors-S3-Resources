package com.pham_mishra.parisairline.repository;

import com.pham_mishra.parisairline.model.Employee;
import org.springframework.data.jpa.repository.JpaRepository;

public interface EmployeeRepository extends JpaRepository<Employee, Long> {
}