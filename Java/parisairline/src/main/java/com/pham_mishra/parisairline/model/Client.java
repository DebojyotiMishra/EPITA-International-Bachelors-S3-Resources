package com.pham_mishra.parisairline.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.ToString;

@Getter
@ToString
@Entity
public class Client {
    @Id
    private String passportNum;

    public void setId(Long id) {
        this.passportNum = id.toString();
    }
}
