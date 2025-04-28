package com.pham_mishra.parisairline.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@EqualsAndHashCode
@Entity
public class Employee {
    @Id
    private String employeeNum;

    public void setId(Long id) {
        this.employeeNum = String.valueOf(id);
    }
}
